import requests
import json
import time
import random
from requests.exceptions import RequestException
import concurrent.futures

def simulate_sensor(location):
    while True:
        try:
            noise_level = random.uniform(30, 90)
            frequency_distribution = [random.uniform(0, 1) for _ in range(10)]
            
            data = {
                "location": location,
                "noise_level": noise_level,
                "frequency_distribution": frequency_distribution,
                "timestamp": time.time()
            }
            
            response = requests.post("http://localhost:3001/soundscape", json=data, timeout=10)
            response.raise_for_status()
            print(f"Data sent for {location}: {response.status_code}")
        except RequestException as e:
            print(f"Error sending data for {location}: {e}")
            print(f"Retrying {location} in 5 seconds...")
        except Exception as e:
            print(f"Unexpected error for {location}: {e}")
            print(f"Stopping simulation for {location}")
            break
        
        time.sleep(5)  # Simulate data every 5 seconds

def run_simulation(locations):
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(locations)) as executor:
        futures = [executor.submit(simulate_sensor, location) for location in locations]
        
        try:
            concurrent.futures.wait(futures)
        except KeyboardInterrupt:
            print("Simulation stopped by user.")
            executor.shutdown(wait=False, cancel_futures=True)

if __name__ == "__main__":
    locations = ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai", "Hyderabad"]
    run_simulation(locations)