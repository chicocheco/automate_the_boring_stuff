#! python3
# subprocess_countdown.py - A simple countdown script.

import subprocess
import time

time_left = 60
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)  # The keyword argument shell=True needed only on Windows.
