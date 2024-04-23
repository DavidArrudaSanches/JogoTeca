from funcoes_forca import *
def jogo_da_forca():    
    vidas=6
    escolhe_tema=input("escolha um tema 1-animais 2-frutas 3-objetos: ")
    if escolhe_tema=="1":
        palavrasecreta=escolhe_palavra("animais")

    elif escolhe_tema=="2":
        palavrasecreta=escolhe_palavra("fruta")

    elif escolhe_tema=="3":
        palavrasecreta=escolhe_palavra("objetos")




    mascara=cria_mascara(palavrasecreta)

    print (*mascara)
    while True:
    
        letra=input("escolha uma letra: ").lower() 
        mascara=preenche_mascara(palavrasecreta,letra,mascara)
        print(*mascara)
        
        if vidas<=0:
            print("voçê perdeu")
            print(f"a palavra era {palavrasecreta}")
            break

        elif letra not in palavrasecreta:
            vidas-=1
            print(f"voçê tem {vidas}")

        elif "_" not in mascara:
            break
      