import yaml

res = {}    
srnames = [] 
#iterate over every line in the input file                      
with open ('inputsr.txt', 'rt') as myfile: 
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
            # if lis[3] not in srnames:
            if len(lis)>=6:
                temp['static_routes'] = [{'VRF':lis[3],
                'destination_address_prefix': lis[4],
                'gateway': lis[5]}]
            srnames.append(lis[3])
            if len(srnames)<=1:
                #print("adding temp dictionary to res dict..")
                #merge new access list to the existing access list
                res.update(temp)
            elif len(lis)<6:
                res['static_routes'].append({
                    'destination_address_prefix': lis[3],
                    'gateway': lis[4]})
            else:
                #print("adding temp dictionary to res dict..")
                    # res['static_routes'].update(temp['static_routes'])
                    # res['static_routes'].append(temp['static_routes'])
                res['static_routes'].append({'VRF':lis[3],
                    'destination_address_prefix': lis[4],
                    'gateway': lis[5]})
                
            # else:
            #     res['static_routes'].append({'VRF':lis[3],
            #     'destination_address_prefix': lis[4],
            #     'gateway': lis[5]})
                
   
# write dictionary to file converting into yaml format
with open('outputsr.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()