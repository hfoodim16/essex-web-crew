#!/usr/bin/env python3
"""seedance-chain.py <storyboard.json> <outdir> — kie-chain.py contract, Seedance edition.

Same chain law as scroll-film-studio/scripts/kie-chain.py (keyframes are a chain;
clips pinned both ends; clip N+1 starts on clip N's literal extracted last frame),
with the generate call swapped from Veo to bytedance/seedance-2-fast via Kie's
jobs/createTask, plus the playbook §2a preflight: measure the first junction
(pin vs the frame the engine actually opened on) and hard-stop if the pin was
re-imagined. STOP_AFTER=2 env → exit cleanly after clip 2 for human review.

Resumable: anything on disk is not regenerated.
"""
import base64
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

KEY = (os.environ.get("KIE_API_KEY")
       or (open(os.path.expanduser("~/.config/kie/key")).read().strip()
           if os.path.exists(os.path.expanduser("~/.config/kie/key")) else None))
if not KEY:
    sys.exit("ERROR: no Kie key (KIE_API_KEY or ~/.config/kie/key)")

UPLOAD_PATH = os.environ.get("KIE_UPLOAD_PATH", "harry-films")
RESOLUTION = os.environ.get("SEEDANCE_RES", "480p")
MODEL = os.environ.get("SEEDANCE_MODEL", "bytedance/seedance-2-fast")
STOP_AFTER = int(os.environ.get("STOP_AFTER", "0") or 0)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
HDRS = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
        "User-Agent": UA}
JOBS_CREATE = "https://api.kie.ai/api/v1/jobs/createTask"
JOBS_INFO = "https://api.kie.ai/api/v1/jobs/recordInfo"
UPLOAD = "https://kieai.redpandaai.co/api/file-base64-upload"


def req(url, body=None, method=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, headers=HDRS,
                               method=method or ("POST" if data else "GET"))
    with urllib.request.urlopen(r, timeout=timeout) as f:
        return json.loads(f.read())


def fetch(url, out, timeout=600):
    r = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(r, timeout=timeout) as src, open(out, "wb") as f:
        f.write(src.read())


def log(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def write_text(path, value):
    with open(path, "w") as f:
        f.write(value)


def safe_id(value, label):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value):
        raise ValueError(f"{label} bad chars")
    if ".." in value:
        raise ValueError(f"{label} cannot contain '..'")
    return value


def credits():
    try:
        return req("https://api.kie.ai/api/v1/chat/credit")["data"]
    except Exception:
        return -1


def poll_job(tid, label, tries=180, sleep_s=8):
    for i in range(tries):
        time.sleep(sleep_s)
        s = req(f"{JOBS_INFO}?taskId={tid}")["data"]
        state = s.get("state")
        if state == "success":
            return json.loads(s["resultJson"])["resultUrls"][0]
        if state == "fail":
            raise RuntimeError(f"{label} failed: {s.get('failMsg')}")
        if i % 8 == 7:
            log(f"    ...{(i + 1) * sleep_s}s")
    raise TimeoutError(f"{label} timed out")


# ---------------------------------------------------------------- keyframes
def gen_still(prompt, ref_url, aspect, out):
    inp = {"prompt": prompt, "aspect_ratio": aspect,
           "resolution": "2K", "output_format": "png"}
    if ref_url:
        inp["image_urls"] = [ref_url]
    d = req(JOBS_CREATE, {"model": "nano-banana-2", "input": inp})
    if d.get("code") != 200:
        raise RuntimeError(f"createTask still: {d.get('msg')}")
    tid = d["data"]["taskId"]
    write_text(f"{out}.task-id", tid)
    url = poll_job(tid, "still", tries=120, sleep_s=4)
    fetch(url, out)
    return url


def upload(path, folder):
    b64 = base64.b64encode(open(path, "rb").read()).decode()
    ext = os.path.splitext(path)[1].lstrip(".") or "png"
    d = req(UPLOAD, {"base64Data": f"data:image/{ext};base64,{b64}",
                     "uploadPath": f"{UPLOAD_PATH.rstrip('/')}/{folder}",
                     "fileName": os.path.basename(path)}, timeout=300)
    if not d.get("success"):
        raise RuntimeError(f"upload: {d}")
    return d["data"]["downloadUrl"]


# --------------------------------------------------------------------- clips
def gen_clip(prompt, first_url, last_url, dur, aspect, out):
    inp = {"prompt": prompt, "first_frame_url": first_url,
           "last_frame_url": last_url, "resolution": RESOLUTION,
           "duration": dur, "aspect_ratio": aspect}
    d = req(JOBS_CREATE, {"model": MODEL, "input": inp})
    if d.get("code") != 200:
        raise RuntimeError(f"createTask clip: {d.get('msg')}")
    tid = d["data"]["taskId"]
    write_text(f"{out}.task-id", tid)
    log(f"    task {tid}")
    url = poll_job(tid, "clip", tries=225, sleep_s=8)
    fetch(url, out)


def ssim(a, b):
    r = subprocess.run(
        ["ffmpeg", "-i", a, "-i", b, "-lavfi",
         "scale2ref[s][r];[s][r]ssim", "-f", "null", "-"],
        capture_output=True, text=True)
    m = re.search(r"All:\s*([0-9.]+)", r.stderr)
    return float(m.group(1)) if m else -1.0


def extract_first(video, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video,
                    "-frames:v", "1", "-q:v", "2", out], check=True)


def extract_last(video, out, width=1080):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.05",
                    "-i", video, "-vf", f"scale={width}:-2",
                    "-frames:v", "1", "-q:v", "2", out], check=True)


# ---------------------------------------------------------------------- main
def main():
    if len(sys.argv) != 3:
        sys.exit("usage: seedance-chain.py <storyboard.json> <outdir>")
    sb = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    kfd, cld = os.path.join(out, "keyframes"), os.path.join(out, "clips")
    os.makedirs(kfd, exist_ok=True)
    os.makedirs(cld, exist_ok=True)
    aspect = sb.get("aspect", "16:9")
    style = sb.get("style", "")
    kfs, clips = sb["keyframes"], sb["clips"]
    if len(clips) != len(kfs) - 1:
        raise ValueError(f"{len(kfs)} keyframes need {len(kfs)-1} clips, got {len(clips)}")
    name = safe_id(sb["name"], "storyboard name")
    for k in kfs:
        safe_id(k["id"], "keyframe id")
    for c in clips:
        safe_id(c["id"], "clip id")

    log(f"{name}: {len(kfs)} keyframes -> {len(clips)} clips "
        f"[{MODEL} {RESOLUTION}]. credits {credits()}")

    urls, prev = [], None
    for i, k in enumerate(kfs):
        p = os.path.join(kfd, f"{k['id']}.png")
        um = os.path.join(kfd, f"{k['id']}.url")
        if os.path.exists(um):
            u = open(um).read().strip()
            log(f"  {k['id']} cached")
        else:
            log(f"  {k['id']} generating"
                f"{' (chained from ' + kfs[i-1]['id'] + ')' if prev else ''}")
            u = gen_still(f"{k['prompt']} {style}".strip(), prev, aspect, p)
            write_text(um, u)
        urls.append(u)
        prev = u

    first_url = urls[0]
    for i, c in enumerate(clips):
        p = os.path.join(cld, f"{i:02d}-{c['id']}.mp4")
        if os.path.exists(p) and os.path.getsize(p) > 100000:
            log(f"  {c['id']} cached")
        else:
            log(f"  {c['id']} {kfs[i]['id']}->{kfs[i+1]['id']} ({c.get('duration', 5)}s)")
            gen_clip(c["prompt"], first_url, urls[i + 1],
                     c.get("duration", 5), aspect, p)
            log(f"    done {os.path.getsize(p)//1024}KB  credits {credits()}")

        # PREFLIGHT / junction measurement: does the engine open on the pin?
        if i > 0:
            pin = os.path.join(cld, f"{i-1:02d}-{clips[i-1]['id']}-last.jpg")
            actual = os.path.join(cld, f"{i:02d}-{c['id']}-first.jpg")
            if not os.path.exists(actual):
                extract_first(p, actual)
            score = ssim(pin, actual)
            log(f"    JUNCTION {clips[i-1]['id']} -> {c['id']}: SSIM(pin, actual first) = {score:.4f}")
            if i == 1 and score < 0.80:
                log("    PREFLIGHT FAIL — engine re-imagined the start pin. "
                    "STOP. Path B (single take) per playbook §2a.")
                sys.exit(2)

        if i < len(clips) - 1:
            last = os.path.join(cld, f"{i:02d}-{c['id']}-last.jpg")
            last_url_file = f"{last}.url"
            if os.path.exists(last_url_file):
                first_url = open(last_url_file).read().strip()
                log(f"    last frame cached")
            else:
                extract_last(p, last)
                first_url = upload(last, name)
                write_text(last_url_file, first_url)
                log(f"    last frame uploaded")

        if STOP_AFTER and i + 1 >= STOP_AFTER:
            log(f"STOP_AFTER={STOP_AFTER} — pausing for human review. Re-run to resume.")
            return

    log(f"all clips done. credits {credits()}")
    log("NEXT: assemble + continuity gate before building.")


if __name__ == "__main__":
    main()
