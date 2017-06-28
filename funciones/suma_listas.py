def suma_lista():

  lista = raw_input("ingresa una serie de numeros separados por espacios: ")
  lista = lista.split(' ')
  suma = 0
  for x in lista:
    suma += int(x)
  print suma

suma_lista()