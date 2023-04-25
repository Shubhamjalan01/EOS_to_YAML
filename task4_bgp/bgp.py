import yaml

res = {}    
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
        if "router bgp" in myline:
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
            #update temp dictionary to res dictionary
            # if len(alnames)<=1:
                #merge new access list to the existing access list
            if len(rb)<=1:
                #print("adding temp dictionary to res dict..")
                #merge new access list to the existing access list
                res.update(temp)
            else:
                #print("adding temp dictionary to res dict..")
                res['router_bgp'].update(temp['router_bgp'])
                
        elif "router-id" in myline:
            line = myline.split()
            print(line)
            res['router_bgp']['router_id'] = line[1]
            print(res)
        # elif "wait-for-convergence" in myline:
        #     line = myline.split()
        #     print(line)
        #     res['router_bgp']['update'] = {'wait_for_convergence': 'true'}
        #     print(res)
        # elif "wait-install" in myline:
        #     line = myline.split()
        #     print(line)
        #     res['router_bgp']['update'].update({'wait_install': 'true'})
        #     print(res)
        elif "update" in myline:
            # temp['router_bgp']={
            #     'update':{}
            # }
            if 'wait-for-convergence' in myline:
                line = myline.split()
                res['router_bgp']['update']['wait_for_convergence'] = 'true'
                # temp['router_bgp']['update']['wait_for_convergence'] = 'true'
                # res['router_bgp']['update']=temp['router_bgp']['update']
                print(res)
            elif 'wait-install' in myline:
                line = myline.split()
                res['router_bgp']['update']['wait_install'] = 'true'
                # temp['router_bgp']['update']['wait_install'] = 'true'
                # res['router_bgp']['update'].update(temp['router_bgp']['update'])
                # res['router_bgp']['update']['wait_install'] = 'true'
                print(res)
        elif "distance" in myline:
            line = myline.split()
            res['router_bgp']['distance']={
                'extrenal_routes': line[2],
                'internal_routes': line[3],
                'local_routes': line[4]
            }
            print(res)
        elif "maximum-paths" in myline:
            line = myline.split()
            res['router_bgp']['maximum_paths']={
                'paths': line[1],
                'ecmp': line[3],
            }
            print(res)
        elif "timers bgp" in myline:
            line = myline.split()
            res['router_bgp']['timers']= line[2]+" "+line[3]
            print(res)
        elif "neighbor" in myline:
            line = myline.split()
            if len(line)<=4:
                if len(vrfs)==0:
                    if 'peer group' in myline:
                        pgnames.append(line[1])
                        if len(pgnames)<=1:
                            res['router_bgp']['peer_groups']= {
                                pgnames[-1]:{}
                            }
                        else:
                            res['router_bgp']['peer_groups'].update({pgnames[-1]:{}}) 
                    elif 'description' in myline:
                        res['router_bgp']['peer_groups'][pgnames[-1]]['description']= line[3] 
                    elif 'update-source' in myline:
                        res['router_bgp']['peer_groups'][pgnames[-1]]['update_source']= line[3]
                    elif 'default-originate' in myline:
                        if 'always' in myline:
                            res['router_bgp']['peer_groups'][pgnames[-1]]['default-originate']= {line[3]: 'true'}
                    elif 'send-community' in myline:
                        res['router_bgp']['peer_groups'][pgnames[-1]]['send_community']= 'standard'
                    elif 'maximum-routes' in myline:
                        res['router_bgp']['peer_groups'][pgnames[-1]]['maximum_routes']= line[3]
                    elif 'remote-as' in myline:
                        res['router_bgp']['peer_groups'][pgnames[-1]]['remote_as']= line[3]
                else:
                    if 'remote-as' in myline: 
                        vrfnbr.append(line[1]) 
                        if len(vrfnbr)<=1:
                            res['router_bgp']['vrfs'][vrfs[-1]]['neighbors']={
                                vrfnbr[-1]:{
                                    'remote_as':line[3]
                                }
                            }   
                        else:
                            res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'].update({vrfnbr[-1]: {'remote_as':line[3]} }) 
                    elif 'description' in myline:
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['description']=line[3]
                    elif 'update-source' in myline:
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['update_source']=line[3]
                    elif 'maximum-routes' in myline:
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['maximum_routes']=line[3]
                    elif 'send-community' in myline:
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['send_community']='standard'
                    elif 'next-hop-self' in myline:
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['next_hop_self']='true'

            elif "neighbor" and len(line)>4:
                if len(vrfs)==0:
                    if 'peer group' in myline:
                        if len(nbr)==0:
                            res['router_bgp']['neighbors']= {line[1]:{
                                'peer_group': line[4]
                                }
                            }
                            nbr.append(line[1])
                        else:
                            res['router_bgp']['neighbors'].update({line[1]:{'peer_group': line[4] }})
                    elif 'local-as' in myline:
                        res['router_bgp']['peer_groups'][pgnames[-1]]['local_as']= line[3]
                else:
                    if 'local-as' in myline:
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['local_as']=line[3]
                    elif 'timers' in myline:
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['timers']=line[3]+" "+line[4]
                    elif 'route-map' in myline:
                        if 'in' in myline:
                            res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['route_map_in']=line[3]
                        elif 'out' in myline:
                            res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'][vrfnbr[-1]]['route_map_out']=line[3]
                    elif 'peer group' in myline: 
                        vrfnbr.append(line[1]) 
                        res['router_bgp']['vrfs'][vrfs[-1]]['neighbors'].update({vrfnbr[-1]: {'peer_group':line[4]} })

        elif 'vrf' in myline:
            line = myline.split()
            vrfs.append(line[-1])
            if len(vrfs)<=1:
                res['router_bgp']['vrfs'] = {
                    line[1]:{
                        'neighbors':{}
                    }
                }  
            else:
                res['router_bgp']['vrfs'].update({line[1]:{'neighbors':{}}})
        elif 'redistribute' in myline:
            line = myline.split()
            if len(vrfs)==0:
                res['router_bgp']['redistribute_routes']={
                    line[1]:{
                        'route_map':line[-1]
                    }
                }
            else:
                if 'connected' in myline:
                    res['router_bgp']['vrfs'][vrfs[-1]]['redistribute_routes']=['connected']
                elif 'static' in myline:
                    res['router_bgp']['vrfs'][vrfs[-1]]['redistribute_routes'].append('static')
                    
        elif 'bgp listen' in myline:
            line = myline.split()
            res['router_bgp']['vrfs'][vrfs[-1]].update({'listen_ranges':{
                'prefix': line[3],
                'peer_group':line[5],
                'peer_filter':line[7]
                }
            })
        print(res)

with open('output.txt', mode='w') as f:
    yaml.dump(res, f, indent=2)
f.close()