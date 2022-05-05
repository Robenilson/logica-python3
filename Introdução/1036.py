import  math

A = input()
Arr= list(map(float,A.split(' ')))
try:
	raiz=(Arr[1]**2) - 4 * Arr[0] * Arr[2]
	raiz = math.sqrt(raiz)
	r1 =  (- Arr[1]  +  raiz ) / ( 2 * Arr[0])
	r2 =  (-Arr[1]  - raiz  ) / ( 2 * Arr[0])
	print ('R1 = {:.5f}'.format(r1))
	print ('R2 = {:.5f}'.format(r2))


except Exception as e:
	print('Impossivel calcular')
