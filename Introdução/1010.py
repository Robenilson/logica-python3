n1 = input()
l1= list(map(float,n1.split(' ')))

n2=input()
l2=list(map(float,n2.split(' ')))


r1=(l1[1]*l1[2])+(l2[1]*l2[2]) 



print('VALOR A PAGAR: R$ {:.2f}'.format(r1))
