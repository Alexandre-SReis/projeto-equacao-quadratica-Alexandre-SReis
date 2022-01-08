print(f'Considere a equação quadrática ax²+bx+c=0.')

#Digitar os valores dos coeficientes
a = float(input(f'Digite o valor de a: '))
b = float(input(f'Digite o valor de b: '))
c = float(input(f'Digite o valor de c: '))

if (a != 0): 
   #Mostrar a equação
   from math import fabs
   if (a > 0):
   	if (b > 0):
   		if (c > 0):
   			print(f'Sua equação é da forma {a}x²+{b}x+{c}=0.')
   		elif (c == 0):
   			print(f'Sua equação é da forma {a}x²+{b}x=0')
   		else:
   			print(f'Sua equação é da forma {a}x²+{b}x-{fabs(c)}=0.')
   	elif (b == 0):
   		if (c > 0):
   			print(f'Sua equação é da forma {a}x²+{c}=0.')
   		elif (c == 0):
   			print(f'Sua equação é da forma {a}x²=0')
   		else:
   			print(f'Sua equação é da forma {a}x²-{fabs(c)}=0.')
   	else:
   		if (c > 0):
   			print(f'Sua equação é da forma {a}x²-{abs(b)}x+{c}=0.')
   		elif (c == 0):
   			print(f'Sua equação é da forma {a}x²-{abs(b)}x=0')
   		else:
   			print(f'Sua equação é da forma {a}x²-{abs(b)}x-{fabs(c)}=0.')
   elif (a < 0):
   	if (b > 0):
   		if (c > 0):
   			print(f'Sua equação é da forma -{abs(a)}x²+{b}x+{c}=0.')
   		elif (c == 0):
   			print(f'Sua equação é da forma -{abs(a)}x²+{b}x=0')
   		else:
   			print(f'Sua equação é da forma -{abs(a)}x²+{b}x-{fabs(c)}=0.')
   	elif (b == 0):
   		if (c > 0):
   			print(f'Sua equação é da forma -{abs(a)}x²+{c}=0.')
   		elif (c == 0):
   			print(f'Sua equação é da forma -{abs(a)}x²=0')
   		else:
   			print(f'Sua equação é da forma -{abs(a)}x²-{fabs(c)}=0.')
   	else:
   		if (c > 0):
   			print(f'Sua equação é da forma -{abs(a)}x²-{abs(b)}x+{c}=0.')
   		elif (c == 0):
   			print(f'Sua equação é da forma -{abs(a)}x²-{abs(b)}x=0')
   		else:
   			print(f'Sua equação é da forma -{abs(a)}x²-{abs(b)}x-{fabs(c)}=0.')
   
   #Resolver a equação

   from math import sqrt
   delta = b**2 - 4 * a * c
   if (delta > 0):
      x_1 = (-b + sqrt(delta)) / (2 * a)
      x_2 = (-b - sqrt(delta)) / (2 * a)
      print(f'Sua equação possui duas soluções distintas, que são x1={x_1} e x2={x_2}.')
   elif (delta == 0):
      x = (-b) / (2 * a)
      print(f'Sua equação possui uma única solução, que é x={x}.')
   else:
      print(f'Sua equação não possui soluções reais, pois b²-4ac={delta} é um valor negativo.')

else:
  if (b == 0):
    if (c == 0):
      print(f'Equação trivial 0=0.')
    else:
      print(f'Equação inválida matematicamente, pois {c} = 0 não é verdade.')
  else:
    x = (-c / b)
    print(f'Você digitou a={int(a)}, logo a equação é do tipo bx+c=0 e tem solução x={x}.')
