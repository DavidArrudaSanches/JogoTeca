import random
palavras=open("Lista_de_palavras.txt","r", encoding='utf8')
arquivo=palavras.readline()
lista=arquivo.split("/n")
palavras_aleatorias=random.choice(lista)
print(palavras_aleatorias)
palavras.close()