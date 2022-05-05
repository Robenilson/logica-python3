A = float(input())


part0_25  =  (A >=  0.00) &  (A <= 25.00)
part25_50 =  (A >= 25.01)  &  (A <= 50.00)
part50_75  = (A >= 50.01)  &  (A <=  75.00)
part75_100 = (A >= 75.01)  &  (A <=  100.00)


if(part0_25):
    print( 'Intervalo [0,25]'.format( part0_25  ))
elif(part25_50):
    print('Intervalo (25,50]'.format(part25_50))
elif(part50_75):
    print('Intervalo (50,75]'.format(part50_75))
elif(part75_100):
    print('Intervalo (75,100]'.format(part75_100))
else:
    print('Fora de intervalo')
