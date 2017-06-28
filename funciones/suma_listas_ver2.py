def suma_lista():

  lista = raw_input("ingresa una serie de numeros separados por espacios: ")
  lista = lista.split(' ')
  suma = 0
  lista2 = []
  for x in lista:
    x = int(x)
    lista2.append(x)

  for i in lista2:
    suma = suma + i

  print suma

suma_lista()