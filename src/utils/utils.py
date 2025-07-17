import random
import pyroscope
import time
from datetime import datetime

ORDER_AVAILABILITY_MULTIPLIER = 0.5

def dice_random_number():
    result = random.randrange(1, 6)
    return result

def process_order(n, veicle):
    with pyroscope.tag_wrapper({
        "veicle": veicle
    }):
        i = 0
        start_time = time.time()
        while time.time() - start_time < n:
            i += 1
        
        if veicle == "car":
            check_order_availability(n)
        
def check_order_availability(n):
    i = 0
    start_time = time.time()
    while time.time() - start_time < n * ORDER_AVAILABILITY_MULTIPLIER:
        i += 1
    
    # Every 4 minutes this will artificially create make requests in eu-north region slow
    # this is just for demonstration purposes to show how performance impacts show up in the
    # flamegraph
    
    force_mutex_lock = datetime.today().minute * 4 % 8 == 0
    if force_mutex_lock:
        mutex_lock(n)
        
def mutex_lock(n):
    i = 0
    start_time = time.time()
    while time.time() - start_time < n * MUTEX_LOCK_MULTIPLIER:
        i += 1