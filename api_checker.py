import json
import requests

file_path = 'projects.json'
with open(file_path, 'r') as file:
    config = json.load(file)



def staked_amount(asked_addies):
    staked_dict = {}
    for project, addresses in zip(config['projects'], asked_addies):
        staked_dict[project] = 0
        denom = int(config['projects'][project]['denom'])
        for address in addresses: 
            for api in config['projects'][project]['api']:
                    total = 0
                    url = f"{api}/cosmos/staking/v1beta1/delegations/{address}"
                    try:
                        response = requests.get(url)
                        data = response.json()
                        for i in range(0,len(data['delegation_responses'])):
                            balance = data['delegation_responses'][i]['balance']['amount']
                            total += (float(balance)/ denom)
                        staked_dict[project] += total
                        break
                    except Exception as e:
                        if not isinstance(e, requests.exceptions.RequestException):
                            print(f"Error: {e}")

    return staked_dict


