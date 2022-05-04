A = int(input())
se = 0
ci = 0
vi = 0
de = 0
c = 0
do =0
um  = 0
print ('{}'.format(A))
while(True):
	if (A -100 >= 0):
		A = A-100
		se =se +1

	elif (A - 50 >= 0 ):
		A = A- 50
		ci = ci + 1

	elif (A - 20 >= 0):
		A= A - 20
		vi= vi +1

	elif (A - 10 >= 0):
		A = A - 10
		de = de -1

	elif (A - 5 >= 0):
		A = A- 5
		c = c +1

	elif(A - 2 >= 0 ):
		A = A - 2
		do = do + 1

	elif(A - 1 >= 0):
		A = A - 1
		um= um + 1
	elif( A == 0):
		break






print ('{} nota(s) de R$ 100,00'.format(se))
print ('{} nota(s) de R$ 50,00'.format(ci))
print ('{} nota(s) de R$ 20,00'.format(vi))
print ('{} nota(s) de R$ 10,00'.format(de))
print ('{} nota(s) de R$ 5,00'.format(c))
print ('{} nota(s) de R$ 2,00'.format(do))
print ('{} nota(s) de R$ 1,00'.format(um))



