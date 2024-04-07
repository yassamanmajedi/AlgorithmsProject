import random
data = []
for i in range(1000):
    random_value = random.randint(-2 ** (32), +2 ** (32))
    data.append(random_value)