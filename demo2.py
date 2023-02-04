import yaml

data = {}
data['access_lists'] = {'test1': {'counters_per_entry': 'true','sequence_numbers': {10: {'action': "permit ip 10.10.10.0/24 any"}}}}
data['access_lists']['test2'] = {
            'counters_per_entry': 'true',
            'sequence_numbers': {
                10: {
                    'action': "permit ip 10.10.10.0/24 host 10.20.10.1"
                },
                20: {
                    'action': "ip"
                }
            }
        }
with open('output.txt', mode='w') as f:
    yaml.dump(data, f, indent=2)