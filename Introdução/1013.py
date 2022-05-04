
import math

A = input()

Arr= list(map(int,A.split(' ')))

A  =  ( Arr[0] + Arr[1] + abs(Arr[0] - Arr[1])) /2
D  =  ( A + Arr[2] + abs(A -Arr[2]))/2

print('{:.0f} eh o maior'.format(D))
