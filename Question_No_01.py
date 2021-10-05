# qus 1(a)--->

def Fibrecursive(n):
  if n ==1:
    return 1
  if n ==2:
    return 1
  else:
    value = Fibrecursive(n-1) + Fibrecursive(n-2)
    return value


# qus 1(b)--->

dictionary = {}

def Fibdynamic(n):
      global dictionary
      dictionary[1] =1
      dictionary[2] =1
      if n in dictionary.keys():
        return dictionary[n]
      else:
        value = Fibdynamic(n-1) + Fibdynamic(n-2)
        dictionary[n] = value 
        return value


# qus 1(c)--->

import time

T1 = time.time()
for i in range(40):
  Fibrecursive(i+1)
T2 = time.time()
rec_Time = T2-T1
print("recursion function time is : ",rec_Time)

T1 = time.time()
for j in range(40):
  Fibdynamic(j+1)
T2 = time.time()
dp_Time = T2-T1
print("dyanmic function time is : " ,dp_Time)

print("time diffrence is : ",rec_Time - dp_Time)