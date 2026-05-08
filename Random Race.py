import multiprocessing
import time
import random
from datetime import datetime

def phase(name):
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    print(f"[{name}] Finished waiting for {wait_time:.2f} seconds.")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    phases = [
        'Ferrari',
        'Lamborghini',
        'Porsche'
    ]
    with multiprocessing.Pool() as pool:
        results = pool.map(phase, phases)

if __name__ == '__main__':
    main()
