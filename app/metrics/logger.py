import time

class Metrics:

    def __init__(self):
        self.start = time.time()

    def report(self):

        end = time.time()

        print("\n===== METRICS =====")
        print(f"Execution Time: {round(end-self.start,2)} seconds")