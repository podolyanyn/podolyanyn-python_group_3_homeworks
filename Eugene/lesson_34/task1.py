import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(Counter.rounds):
            Counter.counter += 1

c_1 = Counter()
c_2 = Counter()

c_1.start()
c_2.start()

c_1.join()
c_2.join()

print(f"Final value counter: {Counter.counter}")