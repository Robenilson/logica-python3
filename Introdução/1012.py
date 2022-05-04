A = input()

Arr= list(map(float,A.split(' ')))

aria_triangulo =  (Arr[0]*Arr[2])/2
aria_circulo   =  3.14159 * (Arr[2]**2)
aria_trapezio  =  ((Arr[0] + Arr[1])*Arr[2])/2
aria_quadrado  =  Arr[1]**2
aria_retangulo =  Arr[0] *Arr[1]

print('TRIANGULO: {:.3f}'.format(aria_triangulo))
print('CIRCULO: {:.3f}'.format(aria_circulo))
print('TRAPEZIO: {:.3f}'.format(aria_trapezio))
print('QUADRADO: {:.3f}'.format(aria_quadrado))
print('RETANGULO: {:.3f}'.format(aria_retangulo)) 

