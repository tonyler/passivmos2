from prices import scrape_prices
from apr import scrape_aprs
import json
from colorama import Fore, Style, init
import schedule
import time


def save_stats():
    aprs = scrape_aprs()
    prices = scrape_prices()
    
    stats_data = {}
    for project in aprs:
        print(f'{Fore.BLUE}{project}{Style.RESET_ALL} has an APR of {Fore.GREEN}{aprs[project]}%{Style.RESET_ALL} and a price of {Fore.YELLOW}{prices[project]}${Style.RESET_ALL}')
        stats_data[project] = {
            "APR": aprs[project],
            "Price": prices[project]
        }
    
    with open('stats.json', 'w') as json_file:
        json.dump(stats_data, json_file, indent=4)  # Save with pretty formatting

save_stats()

# Schedule the save_stats function to run every 5 minutes
schedule.every(2).minutes.do(save_stats)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

