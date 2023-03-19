import json
import os

processed = 0
input_files = [f for f in os.listdir('./data')]
total = len(input_files)

with open ('./generated/full.json', 'wt') as fout:
    fout.write('[')
    for filename in input_files:
        with open('./data/' + filename, 'r') as fin:
            content = fin.read()
            if filename is not input_files[0]:
                fout.write(',')
            fout.write(json.dumps(json.loads(content)))
    fout.write(']')