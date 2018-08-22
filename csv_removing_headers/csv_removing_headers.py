#! python3
# csv_removing_headers.py - Removes the header from all CSV files in the current working directory.

import csv
import os

os.makedirs('headers_removed', exist_ok=True)

# Loop through every file in the current working directory.
for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue    # Skip non-csv file.

    print(f'Removing header from {csv_filename}...')

    # Read the CSV file in (skipping first row).
    csv_file_obj = open(csv_filename)
    reader_obj = csv.reader(csv_file_obj)

    csv_rows = []
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue  # Skip first row.
        csv_rows.append(row)
    csv_file_obj.close()

    # Write out the CSV file.
    csv_file_obj = open(os.path.join('headers_removed', csv_filename), 'w', newline='')
    csv_writer = csv.writer(csv_file_obj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_obj.close()
