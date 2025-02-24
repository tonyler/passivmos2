from translator import convert_address
import json

PREFIXES = []
TYPES =[]
file_path = 'projects.json'
with open(file_path, 'r') as file:
    config = json.load(file)
    for project in config['projects']: 
        PREFIXES.append (config['projects'][project]['prefix']['value'])
        TYPES.append (config['projects'][project]['prefix']['type'])

def user_interface(user_input):
    addresses_list = []
    if " " in user_input: 
        inputs = user_input.split()
    else: 
        inputs = [user_input]

    for input_ in inputs:
        for prefix, type_ in zip(PREFIXES,TYPES):
            if input_.startswith(prefix) and type_ == "cosmos":
                try:
                    new_addresses = convert_address(input_, PREFIXES)
                    addresses_list.append(new_addresses)
                    break 
                except Exception as e:
                    print (f"Error: {e}")
            elif input_.startswith(prefix) and type_ == "evm":
                addresses_list.append([input_])
                break



    addies = set()
    for address in addresses_list:
            addies.update(address)
    addies = list(addies)
    
    print (addies)

    categorized_lists = {project: [] for project in config['projects']}

    for item in addies:
        for project in config['projects']:
                prefix = config['projects'][project]['prefix']['value']
                if item.startswith(prefix):
                    categorized_lists[project].append(item)
                    break  # Stop checking once the item is categorized

    # Convert the categorized lists to a list of lists
    result = list(categorized_lists.values())
    return result

