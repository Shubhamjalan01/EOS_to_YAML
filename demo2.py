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
for x in seq:
    data['access_lists'] = {'test1': {
            'counters_per_entry': 'true',
            'sequence_numbers': {
                x: {
                    'action': "permit ip 10.10.10.0/24 host 10.20.10.1"
                }
            }
        }
    }
with open('output.txt', mode='w') as f:
    yaml.dump(data, f, indent=2)
