import random

with open("random.txt", "w") as f:
    for _ in range(10000):
        f.write("{}\n".format(random.uniform(0, 100000)))
