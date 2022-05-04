import math


x = input()
y = input()

Arrx = list(map(float,x.split(' ')))
Arry = list(map(float,y.split(' ')))

D= ((Arrx[0]- Arry[0])** 2) + ((Arrx[1] - Arry[1])**2)

R = math.sqrt(D)

print('{:.4f}'.format(R))
