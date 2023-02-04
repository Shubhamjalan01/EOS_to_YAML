import yaml

data = {
    'access_lists': {
        'test1': {
            'counters_per_entry': '<true | false>',
            'sequence_numbers': {
                '<sequence_id>': {
                    'action': "<action_string>"
                }
            }
        }
    }
}
mylines = []                             
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:                
        mylines.append(myline)           
print(mylines)
mylines.pop(0)
print(mylines)
seq = [i.split()[0] for i in mylines]
print(seq)
f = open('output.txt', mode='w')
for x in seq:
    data['access_lists']['test1']['sequence_numbers'] = {
                x: {
                    'action': "permit ip 10.10.10.0/24 host 10.20.10.1"
                }
            }
    yaml.dump(data, f, indent=2)
f.close()
