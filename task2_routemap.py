import yaml

res = {}    
alnames = []
sd = []  
#iterate over every line in the input file                      
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:
        #create a empty temporary dict.
        temp = {}
        if "route-map" in myline:
            #Extract access list name from config
            lis = myline.split()
            print(lis)
            #create a temporary dictionary with given accesslist name.
            #temp['route_maps'][lis[-1]] = temp['route_maps'].pop('<access_list_name>')
            #print("creating dictionary for access list",lis[-1])
            temp['route_maps'] = {lis[1]: {
            'sequence_numbers': {
                lis[-1]: {
                    'Type': lis[2],
                    'match':[],
                    'set':[]
                }
                }
            }}
            print(temp)
            alnames.append(lis[1])
            sd.append(lis[-1])
            #update temp dictionary to res dictionary
            if len(alnames)<=1:
                #merge new access list to the existing access list
                res.update(temp)
                print(res)
            else:
                res['route_maps'].update(temp['route_maps'])
        elif "match" in myline:
            #add values to the dictionary for different sequence numbers
            var = myline.strip('\n')
            print(var)
            res['route_maps'][alnames[-1]]['sequence_numbers'][sd[-1]]['match'].append(var)
            print(res)
        elif "set" in myline:
            var = myline.strip('\n')
            print(var)
            res['route_maps'][alnames[-1]]['sequence_numbers'][sd[-1]]['set'].append(var)
            print(res)

# write dictionary to file converting into yaml format
with open('output.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()