#####JOGO TECA#####
#CRIADO POR DAVID#

import os
from adivinhacao.jogo_adivinhacao import*
from jogo_velha.jogo_da_velha import*
from jogo_forca import*
from funcoes_forca import*
from pedra_papel_tesoura.jogo_jokenpo import*
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
while True:    
    print("""
            1- Jogo Da VEIA
            2- Jogo Do Enforcamento
            3- Talbada 
            4- Adivinha ou MORRA!
            5- Pedra papel ou MORRA!!!!!""")
    jogo_escolhido=int(input("escolha um dos jogos digitando o numero: "))
    if jogo_escolhido=="sair":
        exit()

    if jogo_escolhido==1:
        jogo_da_velha()
    if jogo_escolhido==2:
        jogo_da_forca()
    if jogo_escolhido ==4:
        jogo_adivinhacao()
    if jogo_escolhido ==5:
        jogoppt()
    input("Digite enter para recomeçar. ")
    


                                                       