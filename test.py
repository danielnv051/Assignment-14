import time

a = time.time()
s = time.sleep(3)

b = time.time()

print(int(b) - int(a))