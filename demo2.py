import yaml

data = {}
mylines = []                             
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:                
        mylines.append(myline)           
print(mylines)
type = mylines.pop(0)
print(type)
print(mylines)
seq = [i.split()[0] for i in mylines]
print(seq)
act = [i.partition(' ')[2] for i in mylines]
act1 = [i.split(' ',1)[1] for i in act]
act3 = []
for s in act1:
    act3.append(s.replace("\n", " "))
print(act3)

al_name = type.split()
print(al_name)

if "Access List" in type:  
    data['access_lists'] = { al_name[-1]: {
            'counters_per_entry': 'true',
            'sequence_numbers': {
                seq[0]: {
                    'action': 'action_description'
                }
            }
        }
    }

if "Access List" in type:
    for (x,y) in zip(seq,act3):
        data['access_lists'][al_name[-1]]['sequence_numbers'][x] =  {
                    'action': y
        }

f = open('output.txt', mode='w')
yaml.dump(data, f, indent=2)
f.close()
