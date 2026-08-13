#!/usr/bin/env python3
"""single-take.py — one 25s Seedance 2.5 generation (Path: single continuous take).

Persists taskId to disk the moment it is issued; downloads with a browser UA;
logs credit balance before and after. Resumable: if task-id file exists, polls
that task instead of creating a new one.
"""
import json
import os
import sys
import time
import urllib.request

OUT = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(OUT, "build")
os.makedirs(BUILD, exist_ok=True)

KEY = (os.environ.get("KIE_API_KEY")
       or open(os.path.expanduser("~/.config/kie/key")).read().strip())
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
HDRS = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
        "User-Agent": UA}
CREATE = "https://api.kie.ai/api/v1/jobs/createTask"
INFO = "https://api.kie.ai/api/v1/jobs/recordInfo"

PROMPT = (
    "One single unbroken 25-second shot, no cuts, no edits, continuous slow "
    "forward camera move throughout at constant speed. Cinematic night footage "
    "of a completely empty american football stadium. The camera glides at knee "
    "height along a freshly painted chalk-white yard line, pushing steadily "
    "forward along the line toward midfield the entire time. It begins in "
    "near-darkness: floodlights off, dark green turf almost black, silhouetted "
    "empty stands, faint cold city glow above the stadium rim. As the camera "
    "advances, a floodlight bank on the right stand slams on with a hard flare, "
    "raking light and long shadows cutting across the turf, thin mist drifting "
    "over the grass. The push continues and a second floodlight bank ignites, "
    "half the bowl now glowing cold white, chalk dust drifting through the "
    "beams, and far ahead the near edge of an enormous chalk-white painted "
    "abstract emblem on the turf enters the top of the frame. The remaining "
    "banks slam on flare after flare until the whole stadium reaches full "
    "broadcast brightness, the turf saturating to vivid gameday green, the "
    "painted emblem growing larger directly ahead. The camera sinks lower while "
    "still advancing, gliding into the near edge of the emblem, thick white "
    "paint texture on individual grass blades filling the lower half of the "
    "frame, floodlight glare blooming. The shot ends pressing close into the "
    "paint, chalk-white texture on dark green turf filling the entire frame, "
    "soft floodlight bloom washing the top of the frame, motion easing to near "
    "stillness. Photorealistic, anamorphic 35mm, subtle film grain, deep "
    "green-black palette, completely empty stadium, no people, no crowds, no "
    "text, no lettering, no logos."
)


def req(url, body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, headers=HDRS,
                               method="POST" if data else "GET")
    with urllib.request.urlopen(r, timeout=timeout) as f:
        return json.loads(f.read())


def log(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def credits():
    try:
        return req("https://api.kie.ai/api/v1/chat/credit")["data"]
    except Exception:
        return -1


def main():
    tid_file = os.path.join(BUILD, "single-take.task-id")
    out_mp4 = os.path.join(BUILD, "master-raw.mp4")
    if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 1000000:
        log("master-raw.mp4 already on disk — nothing to do")
        return

    log(f"credits before: {credits()}")
    if os.path.exists(tid_file):
        tid = open(tid_file).read().strip()
        log(f"resuming task {tid}")
    else:
        d = req(CREATE, {"model": "bytedance/seedance-2-5", "input": {
            "prompt": PROMPT,
            "aspect_ratio": "16:9",
            "resolution": "480p",
            "duration": 25,
            "generate_audio": False,
            "output_format": "mp4",
        }})
        if d.get("code") != 200:
            log(f"CREATE FAILED: {json.dumps(d)}")
            sys.exit(1)
        tid = d["data"]["taskId"]
        with open(tid_file, "w") as f:
            f.write(tid)
        log(f"task {tid} created (id persisted)")

    for i in range(360):  # up to 60 min
        time.sleep(10)
        s = req(f"{INFO}?taskId={tid}")["data"]
        state = s.get("state")
        if state == "success":
            url = json.loads(s["resultJson"])["resultUrls"][0]
            log(f"success: {url}")
            r = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(r, timeout=900) as src, \
                    open(out_mp4, "wb") as f:
                f.write(src.read())
            log(f"downloaded {os.path.getsize(out_mp4)//1024//1024}MB")
            log(f"credits after: {credits()}")
            return
        if state == "fail":
            log(f"FAILED: {s.get('failMsg')}  (credits: {credits()})")
            sys.exit(1)
        if i % 6 == 5:
            log(f"  ...{(i + 1) * 10}s  state={state}")
    log("TIMEOUT — task id persisted, re-run to resume polling")
    sys.exit(1)


if __name__ == "__main__":
    main()
