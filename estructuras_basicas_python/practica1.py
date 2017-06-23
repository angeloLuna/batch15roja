import random

humano = raw_input("piedra, papel o tijera?")
computadora = random.randint(0, 2)

# asigno piedra papel o tijera a la compu
if computadora == 0:
  computadora = "piedra"
elif computadora == 1:
  computadora = "papel"
else: computadora = "tijera"

# Humano elige piedra
if humano == "piedra":
  if computadora == "piedra":
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "empate"
  elif computadora == "papel":
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "perdiste"
  else: 
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "ganaste"

# Humano elige papel
elif humano == "papel":
  if computadora == "piedra":
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "ganaste"
  elif computadora == "papel":
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "empate"
  else: 
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "perdiste"

# Humano elige piedra
else:
  if computadora == "piedra":
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "pierdes"
  elif computadora == "papel":
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "ganas"
  else: 
    print "La computadora eligio: ", computadora
    print "elegiste: ", humano
    print "empate"


