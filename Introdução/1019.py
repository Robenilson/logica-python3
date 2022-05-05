A = int(input())

ho=int(A/3600)
mi= int((A % 3600)/60)
se= int((A % 3600)%60)




print ('{}:{}:{}'.format(ho,mi,se))
