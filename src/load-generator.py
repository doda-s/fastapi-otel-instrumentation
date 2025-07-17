import random
import requests
import time

HOST = "localhost"

VEHICLES = [
    'bike',
    'scooter',
    'car',
]

if __name__ == "__main__":
    print(f"starting load generator")
    time.sleep(3)
    while True:
        vehicle = VEHICLES[random.randint(0, len(VEHICLES) - 1)]
        print(f"requesting {vehicle} from {HOST}")
        try:
            resp = requests.get(f'http://{HOST}:5000/order/{vehicle}')
            resp.raise_for_status()
            print(f"received {resp}")
        except BaseException as e:
            print (f"http error {e}")

        time.sleep(random.uniform(0.1, 0.2))