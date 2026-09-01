#!/usr/bin/env python3
"""Roadside lead triage — is this business's website missing, weak, or fine?

Harry sees a truck with a domain or an email on the door and texts it to his
agent. This does the objective measuring so the verdict is the same every time
instead of whatever the model felt like that morning.

    python3 sitecheck.py joesplumbing.com
    python3 sitecheck.py info@joesplumbing.com --log
    python3 sitecheck.py https://joesplumbing.com --json

Stdlib only, same as check.py — a triage tool that needs `pip install` is a
triage tool that stops working in six months.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
from html import unescape
from pathlib import Path
from typing import Any

LEADS_FILE = Path(__file__).resolve().parent / "leads.md"
TIMEOUT = 12
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " \
     "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"

# Text that means the domain resolves but there is no real site behind it.
PARKED_MARKERS = (
    "this domain is for sale", "domain for sale", "buy this domain",
    "future home of", "parked free", "courtesy of godaddy",
    "website coming soon", "under construction", "site not found",
    "default web site page", "welcome to nginx", "apache2 ubuntu default",
    "this site can't be reached", "account suspended",
)

# Site builders whose default output is the pitch: Harry rebuilds these.
BUILDERS = {
    "wix": "Wix", "squarespace": "Squarespace", "godaddy": "GoDaddy Builder",
    "weebly": "Weebly", "duda": "Duda", "webflow": "Webflow",
    "wordpress": "WordPress", "shopify": "Shopify", "joomla": "Joomla",
}

PHONE_RE = re.compile(r"\(?\b\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
COPYRIGHT_RE = re.compile(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?(\d{4})", re.I)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
GENERATOR_RE = re.compile(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', re.I)
VIEWPORT_RE = re.compile(r'<meta[^>]+name=["\']viewport["\']', re.I)


def normalize(raw: str) -> str:
    """Turn a domain, URL, or email address into a bare hostname."""
    raw = raw.strip().strip("<>,;").lower()
    if "@" in raw and "://" not in raw:
        raw = raw.split("@", 1)[1]
    raw = re.sub(r"^https?://", "", raw)
    raw = raw.split("/", 1)[0].split("?", 1)[0].split(":", 1)[0]
    return raw.strip(".")


def resolves(host: str) -> list[str]:
    for candidate in (host, f"www.{host}") if not host.startswith("www.") else (host,):
        try:
            infos = socket.getaddrinfo(candidate, None)
            return sorted({i[4][0] for i in infos})
        except socket.gaierror:
            continue
    return []


def fetch(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    started = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read(400_000)
            return {
                "ok": True,
                "status": resp.status,
                "final_url": resp.geturl(),
                "elapsed_ms": int((time.time() - started) * 1000),
                "bytes": len(body),
                "html": body.decode("utf-8", errors="replace"),
            }
    except urllib.error.HTTPError as exc:
        return {"ok": False, "status": exc.code, "error": f"HTTP {exc.code}",
                "elapsed_ms": int((time.time() - started) * 1000)}
    except (urllib.error.URLError, ssl.SSLError, socket.timeout, OSError) as exc:
        reason = getattr(exc, "reason", exc)
        return {"ok": False, "status": None, "error": str(reason),
                "elapsed_ms": int((time.time() - started) * 1000)}


def tls_days_left(host: str) -> int | None:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=TIMEOUT) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as tls:
                not_after = tls.getpeercert().get("notAfter")
        expiry = dt.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(
            tzinfo=dt.timezone.utc
        )
        return (expiry - dt.datetime.now(dt.timezone.utc)).days
    except Exception:
        return None


def strip_tags(html: str) -> str:
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return unescape(re.sub(r"<[^>]+>", " ", html))


def analyse(host: str) -> dict[str, Any]:
    out: dict[str, Any] = {"input_host": host, "checked_at": dt.datetime.now().isoformat(timespec="seconds")}

    ips = resolves(host)
    out["dns"] = ips
    if not ips:
        out["verdict"] = "NO_SITE"
        out["reasons"] = ["domain does not resolve — no website at all"]
        return out

    https = fetch(f"https://{host}")
    page = https
    out["https_ok"] = bool(https.get("ok"))
    if not https.get("ok"):
        page = fetch(f"http://{host}")
        out["http_fallback_ok"] = bool(page.get("ok"))

    out["status"] = page.get("status")
    out["elapsed_ms"] = page.get("elapsed_ms")
    out["bytes"] = page.get("bytes")
    out["final_url"] = page.get("final_url")

    if not page.get("ok"):
        out["verdict"] = "NO_SITE"
        out["reasons"] = [f"domain resolves but nothing serves a page ({page.get('error')})"]
        return out

    html = page.get("html", "")
    text = strip_tags(html)
    lowered = text.lower()

    title = TITLE_RE.search(html)
    out["title"] = " ".join(unescape(title.group(1)).split())[:120] if title else ""

    generator = GENERATOR_RE.search(html)
    out["generator"] = generator.group(1)[:60] if generator else ""

    haystack = (html[:200_000] + out["generator"]).lower()
    out["builder"] = next((label for key, label in BUILDERS.items() if key in haystack), "")

    out["mobile_ready"] = bool(VIEWPORT_RE.search(html))
    out["tls_days_left"] = tls_days_left(host) if out.get("https_ok") else None

    years = [int(y) for y in COPYRIGHT_RE.findall(text)]
    out["copyright_year"] = max(years) if years else None

    out["phones"] = sorted(set(PHONE_RE.findall(text)))[:3]
    out["emails"] = sorted({e for e in EMAIL_RE.findall(text)
                            if not e.endswith((".png", ".jpg", ".gif"))})[:3]

    # --- verdict ----------------------------------------------------------
    reasons: list[str] = []
    parked = next((m for m in PARKED_MARKERS if m in lowered), "")
    if parked:
        out["verdict"] = "NO_SITE"
        out["reasons"] = [f"parked or placeholder page (matched \"{parked}\")"]
        return out

    if out["bytes"] and out["bytes"] < 3000:
        reasons.append(f"almost no content ({out['bytes']} bytes)")
    if not out.get("https_ok"):
        reasons.append("no working HTTPS — browsers flag it as not secure")
    if not out["mobile_ready"]:
        reasons.append("no mobile viewport — breaks on phones")
    this_year = dt.date.today().year
    if out["copyright_year"] and out["copyright_year"] <= this_year - 2:
        reasons.append(f"copyright still says {out['copyright_year']} — visibly stale")
    if out["elapsed_ms"] and out["elapsed_ms"] > 4000:
        reasons.append(f"slow to load ({out['elapsed_ms']}ms)")
    if out["builder"] in {"Wix", "GoDaddy Builder", "Weebly"}:
        reasons.append(f"{out['builder']} template")
    if out["tls_days_left"] is not None and out["tls_days_left"] < 14:
        reasons.append(f"TLS certificate expires in {out['tls_days_left']} days")

    out["reasons"] = reasons
    out["verdict"] = "WEAK" if reasons else "SOLID"
    return out


def one_liner(r: dict[str, Any]) -> str:
    host = r["input_host"]
    verdict = r["verdict"]
    if verdict == "NO_SITE":
        return f"{host} — NO SITE. {r['reasons'][0]}. Strong lead."
    if verdict == "WEAK":
        return f"{host} — WEAK site. {'; '.join(r['reasons'][:3])}. Worth a call."
    bits = []
    if r.get("builder"):
        bits.append(r["builder"])
    if r.get("elapsed_ms"):
        bits.append(f"{r['elapsed_ms']}ms")
    return f"{host} — SOLID site{' (' + ', '.join(bits) + ')' if bits else ''}. Skip."


def log_lead(r: dict[str, Any]) -> None:
    if not LEADS_FILE.exists():
        LEADS_FILE.write_text(
            "# Roadside leads\n\n"
            "Domains Harry captured from the road, triaged by `sitecheck.py`.\n"
            "NO SITE and WEAK are the ones worth a call. Nothing here has been\n"
            "contacted — that is Harry's job, in his own words.\n\n"
            "| Captured | Domain | Verdict | Why | Phone | Email |\n"
            "|---|---|---|---|---|---|\n",
            encoding="utf-8",
        )
    row = "| {when} | {host} | {verdict} | {why} | {phone} | {email} |\n".format(
        when=r["checked_at"][:16].replace("T", " "),
        host=r["input_host"],
        verdict=r["verdict"].replace("_", " "),
        why="; ".join(r.get("reasons", [])) or "—",
        phone=", ".join(r.get("phones", [])) or "—",
        email=", ".join(r.get("emails", [])) or "—",
    )
    with LEADS_FILE.open("a", encoding="utf-8") as fh:
        fh.write(row)


def main() -> int:
    ap = argparse.ArgumentParser(description="Triage a roadside lead's website")
    ap.add_argument("target", help="domain, URL, or email address")
    ap.add_argument("--json", action="store_true", help="full JSON instead of one line")
    ap.add_argument("--log", action="store_true", help="append the result to leads.md")
    args = ap.parse_args()

    host = normalize(args.target)
    if "." not in host:
        print(f"'{args.target}' is not a domain — need something like joesplumbing.com")
        return 2

    result = analyse(host)
    if args.log:
        log_lead(result)
    print(json.dumps(result, indent=2) if args.json else one_liner(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
