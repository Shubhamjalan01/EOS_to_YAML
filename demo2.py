import yaml

data = {}
mylines = []                             
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:                
        mylines.append(myline)           
print(mylines)
mylines.pop(0)
print(mylines)
seq = [i.split()[0] for i in mylines]
print(seq)
data['access_lists'] = {'test1': {'counters_per_entry': 'true','sequence_numbers': {10: {'action': "permit ip 10.10.10.0/24 any"}}}}
data['access_lists']['test2'] = {
            'counters_per_entry': 'true',
            'sequence_numbers': {
                seq[0]: {
                    'action': "permit ip 10.10.10.0/24 host 10.20.10.1"
                },
                seq[1]: {
                    'action': "ip"
                }
            }
        }
with open('output.txt', mode='w') as f:
    yaml.dump(data, f, indent=2)