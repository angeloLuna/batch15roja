frase='agua pasa por mi casa'
frase=frase.split(' ')
frase_lista=[]
for palabra in frase:
   buf=palabra[0].upper()+palabra[1:]
   frase_lista.append(buf)
frase=' '.join(frase_lista)
print frase

x = "1 2 3 4 5"
