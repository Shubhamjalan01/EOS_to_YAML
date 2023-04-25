import yaml

res1 = {}    
alnames = []
res2 = {}    
rmaps = []
sd = []  
res3 = {}    
srnames = []
res4 = {}  
pci = []
res5 = {}    
vlans = []
res6 = {}    
pgnames = []
rb = []  
vrfs = []
nbr = []
vrfnbr = []
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
            
            #update temp dictionary to res1 dictionary
            if len(alnames)<=1:
                #print("adding temp dictionary to res1 dict..")
                #merge new access list to the existing access list
                res1.update(temp)
            else:
                #print("adding temp dictionary to res1 dict..")
                res1['access_lists'].update(temp['access_lists'])

        elif "permit ip" in myline or "deny ip" in myline:
            #add values to the dictionary for different sequence numbers
            #print("adding values for",alnames[-1],"in res1 dict..")
            line = myline.split()
            print(line)
            var = " ".join(line)
            print(var)
            res1['access_lists'][alnames[-1]]['sequence_numbers'][var[:2]] =  {
                    'action': var[3:]
                }
        elif "route-map" in myline:
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
            
            sd.append(lis[-1])
            #update temp dictionary to res2 dictionary
            # if len(rmaps)<=1:
                #merge new access list to the existing access list
            if lis[1] not in rmaps:
                if len(rmaps)==0:
                    res2.update(temp)
                    rmaps.append(lis[1])
                else:
                    res2['route_maps'].update(temp['route_maps'])  
                    rmaps.append(lis[1])
            else:
                res2['route_maps'][lis[1]]['sequence_numbers'].update(temp['route_maps'][lis[1]]['sequence_numbers'])
            # else:
            #     res2['route_maps'].update(temp['route_maps'])
        elif "match" in myline:
            #add values to the dictionary for different sequence numbers
            line = myline.split()
            print(line)
            var = " ".join(line)
            res2['route_maps'][rmaps[-1]]['sequence_numbers'][sd[-1]]['match'].append(var)
            print(res2)
        elif "set" in myline:
            line = myline.split()
            print(line)
            var = " ".join(line)
            res2['route_maps'][rmaps[-1]]['sequence_numbers'][sd[-1]]['set'].append(var)
            print(res2)
        elif "ip route" in myline:
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
                res3.update(temp)
            elif len(lis)<6:
                res3['static_routes'].append({
                    'destination_address_prefix': lis[2],
                    'gateway': lis[3]})
            else:
                #print("adding temp dictionary to res dict..")
                    # res['static_routes'].update(temp['static_routes'])
                    # res['static_routes'].append(temp['static_routes'])
                res3['static_routes'].append({'VRF':lis[3],
                    'destination_address_prefix': lis[4],
                    'gateway': lis[5]})

        elif "interface" in myline:
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
            #update temp dictionary to res4 dictionary
            # if len(alnames)<=1:
                #merge new access list to the existing access list
            if len(pci)<=1:
                #print("adding temp dictionary to res4 dict..")
                #merge new access list to the existing access list
                res4.update(temp)
            else:
                #print("adding temp dictionary to res4 dict..")
                res4['port_channel_interfaces'].update(temp['port_channel_interfaces'])
            # if pci em:
            #     res4.update(temp)
            #     pci.append(lis[1])
            #     print(pci)
            # else:
            #     res4['port_channel_interfaces'].update(temp['port_channel_interfaces'])
            # else:
            #     res4['route_maps'][lis[1]]['sequence_numbers'].update(temp['route_maps'][lis[1]]['sequence_numbers'])
            # else:
            #     res4['route_maps'].update(temp['route_maps'])
        elif "description" in myline:
            #add values to the dictionary for different sequence numbers
            line = myline.split()
            print(line)
            line.pop(0)
            var = " ".join(line)
            res4['port_channel_interfaces'][pci[-1]]['Description'] = var
            print(res4)
        elif "switchport" in myline:
            if 'access' in myline:
                line = myline.split()
                res4['port_channel_interfaces'][pci[-1]]['mode'] = 'access'
                res4['port_channel_interfaces'][pci[-1]]['vlan_id'] = line[-1]
                res4['port_channel_interfaces'][pci[-1]]['type'] = 'switched'
                print(res4)
            elif 'mode' in myline:
                line = myline.split()
                res4['port_channel_interfaces'][pci[-1]]['mode'] = line[2]
                res4['port_channel_interfaces'][pci[-1]]['type'] = 'switched'
                print(res4)
            elif 'group' in myline:
                line = myline.split()
                res4['port_channel_interfaces'][pci[-1]]['trunk_groups'] = line[-1]
            elif "no switchport" in myline:
                res4['port_channel_interfaces'][pci[-1]]['type'] = 'routed'
        elif "no switchport" in myline:
            res4['port_channel_interfaces'][pci[-1]]['type'] = 'routed'
        elif "mlag" in myline:
            line = myline.split()
            print(line)
            res4['port_channel_interfaces'][pci[-1]]['mlag'] = line[1]
        elif "mtu" in myline:
            line = myline.split()
            print(line)
            res4['port_channel_interfaces'][pci[-1]]['mtu'] = line[1]
        elif "ip address" in myline:
            line = myline.split()
            res4['port_channel_interfaces'][pci[-1]]['ip_address'] = line[-1]
        elif "Vlan" in myline:
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
        elif "router bgp" in myline:
            #Extract access list name from config
            lis = myline.split()
            print(lis)
            #create a temporary dictionary with given accesslist name.
            #temp['route_maps'][lis[-1]] = temp['route_maps'].pop('<access_list_name>')
            #print("creating dictionary for access list",lis[-1])
            temp['router_bgp'] = {'as':lis[2],
                'update':{}
            }
            print(temp)
            
            rb.append(lis[-1])
            print(rb)
            #update temp dictionary to res6 dictionary
            # if len(alnames)<=1:
                #merge new access list to the existing access list
            if len(rb)<=1:
                #print("adding temp dictionary to res6 dict..")
                #merge new access list to the existing access list
                res6.update(temp)
            else:
                #print("adding temp dictionary to res6 dict..")
                res6['router_bgp'].update(temp['router_bgp'])
                
        elif "router-id" in myline:
            line = myline.split()
            print(line)
            res6['router_bgp']['router_id'] = line[1]
            print(res6)
        # elif "wait-for-convergence" in myline:
        #     line = myline.split()
        #     print(line)
        #     res6['router_bgp']['update'] = {'wait_for_convergence': 'true'}
        #     print(res6)
        # elif "wait-install" in myline:
        #     line = myline.split()
        #     print(line)
        #     res6['router_bgp']['update'].update({'wait_install': 'true'})
        #     print(res6)
        elif "update" in myline:
            # temp['router_bgp']={
            #     'update':{}
            # }
            if 'wait-for-convergence' in myline:
                line = myline.split()
                res6['router_bgp']['update']['wait_for_convergence'] = 'true'
                # temp['router_bgp']['update']['wait_for_convergence'] = 'true'
                # res6['router_bgp']['update']=temp['router_bgp']['update']
                print(res6)
            elif 'wait-install' in myline:
                line = myline.split()
                res6['router_bgp']['update']['wait_install'] = 'true'
                # temp['router_bgp']['update']['wait_install'] = 'true'
                # res6['router_bgp']['update'].update(temp['router_bgp']['update'])
                # res6['router_bgp']['update']['wait_install'] = 'true'
                print(res6)
        elif "distance" in myline:
            line = myline.split()
            res6['router_bgp']['distance']={
                'extrenal_routes': line[2],
                'internal_routes': line[3],
                'local_routes': line[4]
            }
            print(res6)
        elif "maximum-paths" in myline:
            line = myline.split()
            res6['router_bgp']['maximum_paths']={
                'paths': line[1],
                'ecmp': line[3],
            }
            print(res6)
        elif "timers bgp" in myline:
            line = myline.split()
            res6['router_bgp']['timers']= line[2]+" "+line[3]
            print(res6)
        elif "neighbor" in myline:
            line = myline.split()
            if len(line)<=4:
                if len(vrfs)==0:
                    if 'peer group' in myline:
                        pgnames.append(line[1])
                        if len(pgnames)<=1:
                            res6['router_bgp']['peer_groups']= {
                                pgnames[-1]:{}
                            }
                        else:
                            res6['router_bgp']['peer_groups'].update({pgnames[-1]:{}}) 
                    elif 'description' in myline:
                        res6['router_bgp']['peer_groups'][pgnames[-1]]['description']= line[3] 
                    elif 'update-source' in myline:
                        res6['router_bgp']['peer_groups'][pgnames[-1]]['update_source']= line[3]
                    elif 'default-originate' in myline:
                        if 'always' in myline:
                            res6['router_bgp']['peer_groups'][pgnames[-1]]['default-originate']= {line[3]: 'true'}
                    elif 'send-community' in myline:
                        res6['router_bgp']['peer_groups'][pgnames[-1]]['send_community']= 'standard'
                    elif 'maximum-routes' in myline:
                        res6['router_bgp']['peer_groups'][pgnames[-1]]['maximum_routes']= line[3]
                    elif 'remote-as' in myline:
                        res6['router_bgp']['peer_groups'][pgnames[-1]]['remote_as']= line[3]
                else:
                    if 'remote-as' in myline: 
                        vrfnbr.append(line[1]) 
                        if len(vrfnbr)<=1:
                            res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors']={
                                vrfnbr[-1]:{
                                    'remote_as':line[3]
                                }
                            }   
                        else:
                            res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'].update({vrfnbr[-1]: {'remote_as':line[3]} }) 
                    elif 'description' in myline:
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['description']=line[3]
                    elif 'update-source' in myline:
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['update_source']=line[3]
                    elif 'maximum-routes' in myline:
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['maximum_routes']=line[3]
                    elif 'send-community' in myline:
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['send_community']='standard'
                    elif 'next-hop-self' in myline:
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['next_hop_self']='true'

            elif "neighbor" and len(line)>4:
                if len(vrfs)==0:
                    if 'peer group' in myline:
                        if len(nbr)==0:
                            res6['router_bgp']['neighbors']= {line[1]:{
                                'peer_group': line[4]
                                }
                            }
                            nbr.append(line[1])
                        else:
                            res6['router_bgp']['neighbors'].update({line[1]:{'peer_group': line[4] }})
                    elif 'local-as' in myline:
                        res6['router_bgp']['peer_groups'][pgnames[-1]]['local_as']= line[3]
                else:
                    if 'local-as' in myline:
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['local_as']=line[3]
                    elif 'timers' in myline:
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['timers']=line[3]+" "+line[4]
                    elif 'route-map' in myline:
                        if 'in' in myline:
                            res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['route_map_in']=line[3]
                        elif 'out' in myline:
                            res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['route_map_out']=line[3]
                    elif 'peer group' in myline: 
                        vrfnbr.append(line[1]) 
                        res6['router_bgp']['vrfs'][vrfs[-1]]['neighbors'].update({vrfnbr[-1]: {'peer_group':line[4]} })

        elif 'vrf' in myline:
            line = myline.split()
            vrfs.append(line[-1])
            if len(vrfs)<=1:
                res6['router_bgp']['vrfs'] = {
                    line[1]:{
                        'neighbors':{}
                    }
                }  
            else:
                res6['router_bgp']['vrfs'].update({line[1]:{'neighbors':{}}})
        elif 'redistribute' in myline:
            line = myline.split()
            if len(vrfs)==0:
                res6['router_bgp']['redistribute_routes']={
                    line[1]:{
                        'route_map':line[-1]
                    }
                }
            else:
                if 'connected' in myline:
                    res6['router_bgp']['vrfs'][vrfs[-1]]['redistribute_routes']=['connected']
                elif 'static' in myline:
                    res6['router_bgp']['vrfs'][vrfs[-1]]['redistribute_routes'].append('static')
                    
        elif 'bgp listen' in myline:
            line = myline.split()
            res6['router_bgp']['vrfs'][vrfs[-1]].update({'listen_ranges':{
                'prefix': line[3],
                'peer_group':line[5],
                'peer_filter':line[7]
                }
            })

    if len(res2['route_maps'][rmaps[-1]]['sequence_numbers'][sd[-1]]['set'])==0:
        res2['route_maps'][rmaps[-1]]['sequence_numbers'][sd[-1]].pop('set')
    
        
# write dictionary to file converting into yaml format
with open('output1.txt', mode='w') as f1:
    yaml.dump(res1, f1, indent=2)

with open('output2.txt', mode='w') as f2:
    yaml.dump(res2, f2, indent=2)

with open('output3.txt', mode='w') as f3:
    yaml.dump(res3, f3, indent=2)

with open('output4.txt', mode='w') as f4:
    yaml.dump(res4, f4, indent=2)

with open('output5.txt', mode='w') as f5:
    yaml.dump(res5, f5, indent=2)

with open('output6.txt', mode='w') as f6:
    yaml.dump(res6, f6, indent=2)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()