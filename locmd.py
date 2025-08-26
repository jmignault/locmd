#!/usr/bin/env python
import sys
import time
import requests
## Define the path to your file
file_path = sys.argv[1]

# Open the file and read it line by line
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        # Strip newline and whitespace
        clean_line = line.strip()
        out_path = f'{clean_line}.xml'
        r = requests.get(f'https://lccn.loc.gov/{clean_line}/marcxml')
        outf = open(out_path, 'w')
        outf.write(r.text)
        outf.close()
        print(f'Saving {out_path}')
        time.sleep(15)
