from translator import convert_address
import json

PREFIXES = []
file_path = 'projects.json'
with open(file_path, 'r') as file:
    config = json.load(file)
    for project in config['projects']: 
        PREFIXES.append (config['projects'][project]['prefix'])

def user_interface(user_input):
    addresses_list = []
    if " " in user_input: 
        inputs = user_input.split()
    else: 
        inputs = [user_input]

    for input_ in inputs:
        for prefix in PREFIXES:
            if input_.startswith(prefix): 
                try:
                    new_addresses = convert_address(input_, PREFIXES)
                    addresses_list.append(new_addresses)
                    break 
                except Exception as e:
                    print (f"Error: {e}")
    addies = []
    for address in addresses_list:
        addies = addies + address
    categorized_lists = {project: [] for project in config['projects']}

    for item in addies:
        for project, details in config['projects'].items():
                prefix = details['prefix']
                if item.startswith(prefix):
                    categorized_lists[project].append(item)
                    break  # Stop checking once the item is categorized

    # Convert the categorized lists to a list of lists
    result = list(categorized_lists.values())
    return result

