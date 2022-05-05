A = int(input())

ano = int( A / 365) 
mes = int(A % 365 / 30) 
dia = int( A % 365 % 30) 

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
