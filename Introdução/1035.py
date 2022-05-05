
A = input()

Arr= list(map(int,A.split(' ')))




part1 =  (Arr[1] > Arr[2]) & (Arr[3] > Arr[0])
soma  = (Arr[2] + Arr[3]) > (Arr[0] + Arr[1])
pos   =  Arr[3]  >= 0  & Arr[2] >=0
par = (Arr[0]%2) == 0

if ( part1 & soma & pos & par):
    print ('Valores aceitos')
else:
    print('Valores nao aceitos')
