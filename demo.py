import yaml

data = {
    'access_lists': {
        '<access_list_name>': {
            'counters_per_entry': '<true | false>',
            'sequence_numbers': {
                '<sequence_id>': {
                    'action': "<action_string>"
                }
            }
        }
    }
}
data['access_lists']['<access_list_name>']['sequence_numbers']['<sequence_id>']['action'] = 'permit ip 10.10.10.0/24 any'
data['access_lists']['<access_list_name>']['counters_per_entry'] = True
data['access_lists']['<access_list_name>']['sequence_numbers'][10]=data['access_lists']['<access_list_name>']['sequence_numbers'].pop('<sequence_id>')
data['access_lists']['test1'] = data['access_lists'].pop('<access_list_name>')
with open('test.txt', mode='w') as f:
    yaml.dump(data, f, indent=2)