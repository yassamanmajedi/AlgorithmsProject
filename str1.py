import random
import string
str1 = []
file_object = open("str1.txt", "w")
for i in range(1000):
    N = random.randint(1, 80)
    string1 = ''.join(random.choices(string.ascii_letters, k=N))
    file_object.write(string1)
    str1.append(string1)
file_object.close()

