import yaml

res = {}    
alnames = []  
#iterate over every line in the input file                      
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:
        #create a empty temporary dict.
        temp = {}
        if "Access List" in myline:
            #Extract access list name from config
            lis = myline.split()
            alnames.append(lis[-1])
            #create a temporary dictionary with given accesslist name.
            #temp['access_lists'][lis[-1]] = temp['access_lists'].pop('<access_list_name>')
            #print("creating dictionary for access list",lis[-1])
            temp['access_lists'] = {lis[-1]: {
            'counters_per_entry': 'true',
            'sequence_numbers': {
                }
            }}
            
            #update temp dictionary to res dictionary
            if len(alnames)<=1:
                #print("adding temp dictionary to res dict..")
                #merge new access list to the existing access list
                res.update(temp)
            else:
                #print("adding temp dictionary to res dict..")
                res['access_lists'].update(temp['access_lists'])
        else:
            #add values to the dictionary for different sequence numbers
            #print("adding values for",alnames[-1],"in res dict..")
            var = myline.strip('\n')
            res['access_lists'][alnames[-1]]['sequence_numbers'][myline[1:3]] =  {
                    'action': var[4:]
                }
   
# write dictionary to file converting into yaml format
with open('output.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()
