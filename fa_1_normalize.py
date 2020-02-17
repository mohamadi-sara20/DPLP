import re
import os
import json
import sys

def normalize(filepath):
    with open('fa_character_mapping.json') as f:
        mappings = json.load(fp=f)
    with open(filepath) as f:
        text = f.read()
    for c in mappings:
        text = re.sub(chr(int(c)), mappings[c], text)
    with open(filepath , 'w') as f:
        f.write(text)


if __name__ == '__main__':
    print('====================== normalize =================')
    path = sys.argv[1]
    all_files = os.listdir(path)
    for f in all_files:
        if not f.endswith('.rs3'):
            continue
        normalize(path + '/' + f)