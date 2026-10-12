import os
import subprocess
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = f"file://{os.path.join(current_dir, 'index.html')}"
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

screenshots = [
    {
        "filename": "screenshot_1_hero_overview.png",
        "width": 1280,
        "height": 900,
    },
    {
        "filename": "screenshot_2_mobile_view.png",
        "width": 390,
        "height": 844,
    },
    {
        "filename": "screenshot_3_tablet_view.png",
        "width": 768,
        "height": 1024,
    }
]

for s in screenshots:
    out_path = os.path.join(current_dir, s["filename"])
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--window-size={s['width']},{s['height']}",
        f"--screenshot={out_path}",
        html_path
    ]
    print(f"Capturing {s['filename']} ({s['width']}x{s['height']})...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_path):
        print(f"Generated {out_path} ({os.path.getsize(out_path)} bytes)")
    else:
        print(f"Failed to generate {out_path}: {res.stderr}")

print("Screenshot capture complete!")
