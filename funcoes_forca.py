import random
def escolhe_palavra(escolhadetema:str):
    palavras=open(f"{escolhadetema}.txt", "r", encoding='utf-8')
    linhas=palavras.read()
    correção_linhas=linhas.split("\n")
    palavras_aleatorias=random.choice(correção_linhas)
    return palavras_aleatorias.lower()

        

def cria_mascara(palavra:str) -> list:
    lista_mascara = []
    for letra in palavra:
        lista_mascara.append("_")
    return lista_mascara



def preenche_mascara(palavra:str,letra:str,mascara:list) -> list:
    indice=0
    for letra2 in palavra:
        if letra2==letra:
            mascara[indice]=letra
        indice+=1
        
    return mascara
