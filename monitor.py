import threading
import subprocess
import os
import time

def run_discord_bot():
    subprocess.run(['python3', 'discord_main.py'])

def run_collector():
    while True:
        subprocess.run(['python3', 'collect_main.py'], cwd='stats')

if __name__ == "__main__":
    # Create threads for the Discord bot and the collector
    discord_thread = threading.Thread(target=run_discord_bot)
    collector_thread = threading.Thread(target=run_collector)

    # Start both threads
    discord_thread.start()
    collector_thread.start()

    try:
        # Wait for both threads to complete
        discord_thread.join()
        collector_thread.join()
    except KeyboardInterrupt:
        print("Stopping scripts...")

