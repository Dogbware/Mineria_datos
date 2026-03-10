import pandas as pd
import numpy as np
from numpy import random

#ejercicio1
array10 = random.randint(0,100,10)
print(array10)

#ejercicio2
array5= random.rand(5)
print(array5)

#ejercicio3
array1 = random.randint(0,100,5)
array2 = random.randint(0,100,5)
arrayc=np.concatenate((array1,array2))
print(arrayc)

#ejercicio4
array3 = random.randint(0,100,10)
arrayse1=np.split(array3,2)
print(arrayse1)

#ejercicio5
array4 = random.rand(3,3)
print(array4)

#ejercicio6
array6 = random.randint(0,100,10)
arrayselect=random.choice(array6,3)
print(arrayselect)

#ejercicio7
array7=random.randint(0,100, 10)
media = array7.mean()
print(media)