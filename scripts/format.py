import json
data = None
with open('./instructions.json', 'r') as fin:
    data = json.loads(fin.read())
data = sorted(data, key=lambda x: x['id'])
with open('./instructions.json', 'w') as fout:
    fout.write(json.dumps(data, indent=2))