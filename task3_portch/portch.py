import yaml

res = {}    
alnames = []
pci = []  
#iterate over every line in the input file                      
with open ('input.txt', 'rt') as myfile: 
    for myline in myfile:
        #create a empty temporary dict.
        temp = {}
        if "interface" in myline:
            #Extract access list name from config
            lis = myline.split()
            print(lis)
            #create a temporary dictionary with given accesslist name.
            #temp['route_maps'][lis[-1]] = temp['route_maps'].pop('<access_list_name>')
            #print("creating dictionary for access list",lis[-1])
            temp['port_channel_interfaces'] = {lis[1]: {
                }
            }
            print(temp)
            
            pci.append(lis[-1])
            print(pci)
            #update temp dictionary to res dictionary
            # if len(alnames)<=1:
                #merge new access list to the existing access list
            if len(pci)<=1:
                #print("adding temp dictionary to res dict..")
                #merge new access list to the existing access list
                res.update(temp)
            else:
                #print("adding temp dictionary to res dict..")
                res['port_channel_interfaces'].update(temp['port_channel_interfaces'])
            # if pci em:
            #     res.update(temp)
            #     pci.append(lis[1])
            #     print(pci)
            # else:
            #     res['port_channel_interfaces'].update(temp['port_channel_interfaces'])
            # else:
            #     res['route_maps'][lis[1]]['sequence_numbers'].update(temp['route_maps'][lis[1]]['sequence_numbers'])
            # else:
            #     res['route_maps'].update(temp['route_maps'])
        elif "description" in myline:
            #add values to the dictionary for different sequence numbers
            line = myline.split()
            print(line)
            line.pop(0)
            var = " ".join(line)
            res['port_channel_interfaces'][pci[-1]]['Description'] = var
            print(res)
        elif "switchport" in myline:
            if 'access' in myline:
                line = myline.split()
                res['port_channel_interfaces'][pci[-1]]['Mode'] = 'access'
                res['port_channel_interfaces'][pci[-1]]['vlan_id'] = line[-1]
                res['port_channel_interfaces'][pci[-1]]['Type'] = 'switched'
                print(res)
            elif 'mode trunk' in myline:
                res['port_channel_interfaces'][pci[-1]]['Mode'] = 'trunk'
                res['port_channel_interfaces'][pci[-1]]['Type'] = 'switched'
                print(res)
            elif 'group' in myline:
                line = myline.split()
                res['port_channel_interfaces'][pci[-1]]['Trunk_groups'] = line[-1]
            elif "no switchport" in myline:
                res['port_channel_interfaces'][pci[-1]]['Type'] = 'routed'
        elif "no switchport" in myline:
            res['port_channel_interfaces'][pci[-1]]['Type'] = 'routed'
        elif "mlag" in myline:
            line = myline.split()
            print(line)
            res['port_channel_interfaces'][pci[-1]]['Mlag'] = line[1]
        elif "mtu" in myline:
            line = myline.split()
            print(line)
            res['port_channel_interfaces'][pci[-1]]['Mtu'] = line[1]
        elif "ip address" in myline:
            line = myline.split()
            res['port_channel_interfaces'][pci[-1]]['ip_address'] = line[-1]

with open('output.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()