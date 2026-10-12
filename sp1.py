# kód : 23
# datum : 12.10.2026
# kulička se bude pohybovat po obrazovce

import time
import math

print("Zadej počet kuliček")
pocet = int(input())
print("Kulička jede")

for i in range(pocet):
    print(" " * i + "O")
    time.sleep(0.1)

for i in range(pocet):
    print(" " * (pocet - i) + "O")
    time.sleep(0.1)

print("Tabulka")
for i in range(1, pocet + 1):
    print(i, i*i, math.sqrt(i))
    time.sleep(0.1)