import yaml

res = {}    
alnames = []  
#iterate over the input file                      
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:
        #create a empty temporary dict.
        temp = {}
        if "Access List" in myline:
            #Extract access list name from config
            lis = myline.split()
            alnames.append(lis[-1])
            print(lis[-1])
            #create a temporary dictionary with given accesslist name.
            #temp['access_lists'][lis[-1]] = temp['access_lists'].pop('<access_list_name>')
            temp['access_lists'] = {lis[-1]: {
            'counters_per_entry': 'true',
            'sequence_numbers': {
                }
            }}
            
            print(temp)
            #update temp dictionary to res dictionary
            if len(alnames)>1:
                #res.update(temp['access_lists'])
                #merge new access list to the existing access list
                res['access_lists'].update(temp['access_lists'])
            else:
                res.update(temp)
            print(res)
            print(alnames)
        else:
            #add values to the dictionary for different sequence numbers
            #for x in alnames:
            var = myline.strip('\n')
            res['access_lists'][alnames[-1]]['sequence_numbers'][myline[1:3]] =  {
                    'action': var[4:]
                }
            print(res)
print(res)   
# write dictionary to file converting into yaml format  
with open('output.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()
