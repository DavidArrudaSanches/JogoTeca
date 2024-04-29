def jogoppt () :
    import random
    jogador= input("escolha a sua jogada: pedra,papel,tesoura: ").lower()

    maquina=random.randint(1,3)
    if maquina==1:
        maquina="pedra"
    elif maquina==2:
        maquina="papel"
    elif maquina==3:
        maquina="tesoura"

    print(f"{jogador} vs {maquina}")

    if jogador==maquina:
        print("Empate ambos dos jogadores usaram a mesma jogada.")
    if jogador=="pedra":
        if jogador=="pedra" and maquina=="tesoura":
            print("o jogador ganhou")
        else:
            print("vitoria da maquina")
    if jogador=="tesoura":
        if jogador=="tesoura" and maquina=="papel":
            print("o jogador ganhou")
        else:
            print("vitoria da maquina")
    if jogador=="papel":
        if jogador=="papel" and maquina=="pedra":
            print("o jogador ganhou")
        else:
            print("vitoria da maquina")