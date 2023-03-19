import json
data = None
expected_keys = {
    'id', 
    'instruction', 
    'input', 
    'output', 
    'license',
    'generation-type', 
    'generation-reference', 
    'modified', 
    'verified', 
    'tags'
}

with open('./instructions.json', 'r') as fin:
    data = json.loads(fin.read())
    for row in data:
        keys = set(row.keys())
        if keys != expected_keys:
            print('Invalid row %s:\n%s' % (row['id'], json.dumps(row, indent=2)))
            print('Expected keys: %s' % expected_keys)
            print('Actual keys: %s' % keys)
            raise Exception("Keys don't match")
            

