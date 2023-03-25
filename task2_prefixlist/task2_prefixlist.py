import yaml

res = {}    
plnames = []  
#iterate over every line in the input file                      
with open ('inputp.txt', 'rt') as myfile: 
    for myline in myfile:
        #create a empty temporary dict.
        temp = {}
        if "prefix-list" in myline:
            #Extract access list name from config
            lis = myline.split()
            print(lis)
            
            #create a temporary dictionary with given accesslist name.
            #temp['access_lists'][lis[-1]] = temp['access_lists'].pop('<access_list_name>')
            #print("creating dictionary for access list",lis[-1])
            if lis[2] not in plnames:
                temp['prefix_lists'] = {lis[2]: {
                'counters_per_entry': 'true',
                'sequence_numbers': {
                    lis[4]: {
                        'action': lis[5]+' '+lis[6]
                            }
                        }
                }   }
                plnames.append(lis[2])
                if len(plnames)<=1:
                #print("adding temp dictionary to res dict..")
                #merge new access list to the existing access list
                    res.update(temp)
                else:
                #print("adding temp dictionary to res dict..")
                    res['prefix_lists'].update(temp['prefix_lists'])
                
            else:
                res['prefix_lists'][lis[2]]['sequence_numbers'][lis[4]] =  {
                    'action': lis[5]+' '+lis[6]
                }
                
   
# write dictionary to file converting into yaml format
with open('outputp.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()