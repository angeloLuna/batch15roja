
def cuadrado(numero):
  print numero * numero  

def jadenCase():
  frase = raw_input('Ingresa un twitt')
  frase=frase.split(' ')
  frase_lista=[]
  for palabra in frase:
     buf=palabra[0].upper()+palabra[1:]
     frase_lista.append(buf)
  frase=' '.join(frase_lista)
  print frase


opcion = input("ingresa un 1 o un 2")

if opcion == 1:
  jadenCase()
else:
  cuadrado(opcion)

Una funcion que reciba como paramtro una lista de números y sume todos los numeros, la lista tiene que ser dínamica.



a = 10
c = 30

c += a

c = a + c








