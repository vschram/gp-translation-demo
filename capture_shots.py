"""Capture the slide frames of the GP demo as PNGs with headless Edge.

Serve this folder first (python -m http.server 8322), then run:
    python capture_shots.py
"""
import os
import subprocess
import tempfile
import time

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
URL = "http://localhost:8322/?shot={name}&w={w}&h={h}"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
W, H = 1067, 740        # SVG viewBox: text is sized relative to this
SCALE = 1.5             # window = viewBox x SCALE, for a crisp PNG
PRESETS = ["decision", "prior", "kernel", "rule", "reveal", "band", "quiz1", "quiz2"]

def capture(url, target, width, height, scale=1):
    if os.path.exists(target):
        os.remove(target)
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([
            EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            f"--force-device-scale-factor={scale}", f"--user-data-dir={profile}",
            f"--window-size={width},{height}", f"--screenshot={target}", url,
        ], check=False)
        for _ in range(60):
            if os.path.exists(target) and os.path.getsize(target) > 0:
                break
            time.sleep(0.5)
        time.sleep(1)  # let Edge release the profile before cleanup
    return "ok" if os.path.exists(target) else "MISSING"


os.makedirs(OUT, exist_ok=True)
for name in PRESETS:
    target = os.path.abspath(os.path.join(OUT, f"gp_{name}.png"))
    status = capture(URL.format(name=name, w=W, h=H), target, round(W * SCALE), round(H * SCALE))
    print(f"{name}: {status}")

# The demo page itself, tabs visible, for the "explore the demo" slide.
target = os.path.abspath(os.path.join(OUT, "gp_demo_tabs.png"))
print("demo_tabs:", capture("http://localhost:8322/?tab=experiment&theme=light", target, 1000, 620, scale=1.5))
