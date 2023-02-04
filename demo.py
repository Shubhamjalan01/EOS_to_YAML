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
#data['<sequence_id>'] = data[10]
data['access_lists']['<access_list_name>']['sequence_numbers']['<sequence_id>']['action'] = 'ip any'
data['access_lists']['<access_list_name>']['counters_per_entry'] = 'true'
with open('test.txt', mode='w') as f:
    yaml.dump(data, f, indent=2)