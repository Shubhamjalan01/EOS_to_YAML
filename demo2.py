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
act = [i.partition(' ')[2] for i in mylines]
act1 = [i.split(' ',1)[1] for i in act]
act3 = []
for s in act1:
    act3.append(s.replace("\n", " "))
print(act3)
f = open('output.txt', mode='w')
for x in seq:
    data['access_lists'] = {'test1': {
            'counters_per_entry': 'true',
            'sequence_numbers': {
                x: {
                    'action': act3[0]
                }
            }
        }
    }
    yaml.dump(data, f, indent=2)
