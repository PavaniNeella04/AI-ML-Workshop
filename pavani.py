# -*- coding: utf-8 -*-
"""pavani.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lC0ROr3vSJ7BuA8GOSAcg-X7og5vtzf0
"""

import numpy as np
arr=[1,2,3,4,5,6,7,8,9,10]
arra=np.array(arr)
arra

arr=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(arr)):
  print(arr[i])

l=arr[::]
tuple(l)

l=arr[::]
set(l)