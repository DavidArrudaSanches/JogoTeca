#####JOGO TECA#####
#CRIADO POR DAVID#
import os
from adivinhacao.jogo_adivinhacao import*
os.system("cls")

print("""        
         _ __ ___   ___ _ __  _   _ 
        | '_ ` _ \ / _ \ '_ \| | | |
        | | | | | |  __/ | | | |_| |
        |_| |_| |_|\___|_| |_|\__,_|  
                                    """)

idade=int(input("         Qual é a sua idade ?: "))
if idade >=18:
    print("         acesso liberado😀😀")
if idade <18:
    print("         Sai daqui seu muleke!!!😡😠😡")
    exit()

print("""
         1- Jogo Da VEIA
         2- Jogo Do Enforcamento
         3- Talbada 
         4- Adivinha ou MORRA!""")
jogo_escolhido=int(input("escolha um dos jogos digitando o numero: "))

if jogo_escolhido ==4:
    jogo_adivinhacao()


                                                       