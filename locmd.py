#!/usr/bin/env python
import requests
## Define the path to your file
file_path = ARGV[1]

# Open the file and read it line by line
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        # Strip newline and whitespace
        clean_line = line.strip()
        outf = f'{clean_line}.xml'
        r = requests.get(f'https://lccn.loc.gov/{clean_line}/marcxml')
        open(outf, 'w')
        outf.write(r.content)
        outf.close()
        sleep(20)
