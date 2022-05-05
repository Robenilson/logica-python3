A = float(input())
se = 0
ci = 0
vi = 0
de = 0
c = 0
do =0
um  = 0

moeda1=0
moeda2=0
moeda3=0
moeda4=0
moeda5=0
moeda6=0
while(True):
	if (float("{:.2f}".format( A - 100.00 )) >= 0.00):
		A = A-100.00
		se =se +1

	elif (float("{:.2f}".format( A - 50.00)) >= 0.00 ):
		A = A- 50.00
		ci = ci + 1

	elif (float("{:.2f}".format( A - 20.00)) >= 0.00):
		A= A - 20.00
		vi= vi +1

	elif (float("{:.2f}".format( A - 10.00))  >= 0.00):
		A = A - 10.00
		de = de -1

	elif (float("{:.2f}".format(A - 5.00)) >= 0.00):
		A = A- 5.00
		c = c +1

	elif(float("{:.2f}".format( A - 2.00))   >= 0.00 ):
		A = A - 2.00
		do = do + 1

	elif (float("{:.2f}".format(  A -1.00 ))  >= 0.00):
		A = A-1.00
		moeda1 =moeda1 +1

	elif (float("{:.2f}".format(  A - 0.50))   >= 0.00 ):
		A = A- 0.50
		moeda2 = moeda2 + 1

	elif (float("{:.2f}".format( A - 0.25))    >= 0.00):
		A= A - 0.25
		moeda3= moeda3 +1

	elif (float("{:.2f}".format( A - 0.10 ))   >= 0.00):
		A = A - 0.10
		moeda4 = moeda4 +1

	elif (float("{:.2f}".format( A - 0.05 )) >= 0.00):
		A = A- 0.05
		moeda5 = moeda5 + 1

	elif(float("{:.2f}".format(A)) == 0.00 ):
		break

	elif(float("{:.2f}".format( A - 0.01 )) >= 0.00 ):
		A = A - 0.01
		moeda6 = moeda6 + 1



print ('NOTAS:')
print ('{} nota(s) de R$ 100.00'.format(se))
print ('{} nota(s) de R$ 50.00'.format(ci))
print ('{} nota(s) de R$ 20.00'.format(vi))
print ('{} nota(s) de R$ 10.00'.format(de))
print ('{} nota(s) de R$ 5.00'.format(c))
print ('{} nota(s) de R$ 2.00'.format(do))
print ('MOEDAS:')
print ('{} moeda(s) de R$ 1.00'.format(moeda1))
print ('{} moeda(s) de R$ 0.50'.format(moeda2))
print ('{} moeda(s) de R$ 0.25'.format(moeda3))
print ('{} moeda(s) de R$ 0.10'.format(moeda4))
print ('{} moeda(s) de R$ 0.05'.format(moeda5))
print ('{} moeda(s) de R$ 0.01'.format(moeda6))
