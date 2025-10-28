import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print("Check in order")
    start_time = time.time()
    prime_list = []
    for num in NUMBERS:
        if is_prime(num):
            prime_list.append(num)
    time_result = time.time() - start_time
    print(f"Primes found: {len(prime_list)} in {time_result:.4f} sec.")


    print("Check in thread")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results_thread = list(executor.map(is_prime, NUMBERS))
    primes_thread = [NUMBERS[i] for i in range(len(NUMBERS)) if results_thread[i]]
    time_thread = time.time() - start_time
    print(f"With threads: {len(primes_thread)} primes in {time_thread:.4f} sec.")


    print("Check in proc")
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results_proc = list(executor.map(is_prime, NUMBERS))
    primes_proc = [NUMBERS[i] for i in range(len(NUMBERS)) if results_proc[i]]
    time_proc = time.time() - start_time
    print(f"With proc: {len(primes_proc)} primes in {time_proc:.4f} sec.")

    print("\nAre the results the same?", prime_list == primes_thread == primes_proc)
    print("Prime numbers:", prime_list)
    print("Time: in order -", time_result, "threads -", time_thread, "proc -", time_proc)
    if time_proc < time_thread:
        print("Proc are faster.")
    else:
        print("Threads are faster.")