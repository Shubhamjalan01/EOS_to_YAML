import yaml

res5 = {}    
vlans = []  
#iterate over every line in the input file                      
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:
        #create a empty temporary dict.
        temp = {}
        if "Vlan" in myline:
            #Extract access list name from config
            lis = myline.split()
            print(lis)
            vlans.append(lis[-1])
            #create a temporary dictionary with given accesslist name.
            #temp['access_lists'][lis[-1]] = temp['access_lists'].pop('<access_list_name>')
            #print("creating dictionary for access list",lis[-1])
            temp['vlans'] = {lis[-1]: {
            }}
            
            #update temp dictionary to res5 dictionary
            if len(vlans)<=1:
                #print("adding temp dictionary to res5 dict..")
                #merge new access list to the existing access list
                res5.update(temp)
            else:
                #print("adding temp dictionary to res5 dict..")
                res5['vlans'].update(temp['vlans'])
        elif 'name' in myline:
            #add values to the dictionary for different sequence numbers
            #print("adding values for",alnames[-1],"in res5 dict..")
            var = myline.split()
            print(var)
            res5['vlans'][vlans[-1]] =  {
                    'name': var[1]
                }
   
# write dictionary to file converting into yaml format
with open('output.txt', mode='w') as f:
    yaml.dump(res5, f, indent=2)
f.close()