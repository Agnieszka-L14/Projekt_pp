import platform
import random
import math

print("Procesor:", platform.processor())
print("Losowanie:", random.sample(range(1,11),3))
print("sinus 90 stopni:", math.sin(math.radians(90)))