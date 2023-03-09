import yaml

res = {}    
srnames = [] 
i=1 
#iterate over every line in the input file                      
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:
        #create a empty temporary dict.
        temp = {}
        if "route" in myline:
            #Extract access list name from config
            lis = myline.split()
            print(lis)
            #create a temporary dictionary with given accesslist name.
            #temp['access_lists'][lis[-1]] = temp['access_lists'].pop('<access_list_name>')
            #print("creating dictionary for access list",lis[-1])
            if lis[3] not in srnames:
                temp['static_routes'] = [{'VRF':lis[3],
                'destination_address_prefix': lis[4],
                'gateway': lis[5]}]
                srnames.append(lis[3])
                if len(srnames)<=1:
                #print("adding temp dictionary to res dict..")
                #merge new access list to the existing access list
                    res.update(temp)
                else:
                #print("adding temp dictionary to res dict..")
                    res['static_routes'].update(temp['static_routes'])
                
            else:
                res['static_routes'].append({
                'destination_address_prefix': lis[4],
                'gateway': lis[5]})
                
   
# write dictionary to file converting into yaml format
with open('output.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()