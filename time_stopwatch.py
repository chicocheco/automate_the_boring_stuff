#! python3
# time_stopwatch.py - A simple stopwatch program.

import time
import pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # Press Enter to begin.
print('Started.')

start_time = time.time()  # Get the first lap's start time.
last_time = start_time

lap_num = 1
records = []
# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        record = f'Lap # {str(lap_num).rjust(2)}: {str(total_time).rjust(6)} ({str(lap_time).rjust(6)})'
        records.append(record)
        print(record, end='')
        lap_num += 1
        last_time = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    records_nl = '\r\n'.join(records)  # Formating for the clipboard.
    pyperclip.copy(records_nl)
    print('\n\nCopied to the clipboard. \nClosing in 10 seconds...')
    time.sleep(10)
