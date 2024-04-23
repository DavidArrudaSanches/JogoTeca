import os 


def jogo_da_velha():
    os.system("cls")
    marcacoes= [0,1,2,3,4,5,6,7,8,9]
    jogador="X"
    jogada=0
    while True:
        while True:
                print (f"{marcacoes[1]:^5}|{marcacoes[2]:^5}|{marcacoes[3]:^5}|")
                print("-------------------")
                print (f"{marcacoes[4]:^5}|{marcacoes[5]:^5}|{marcacoes[6]:^5}|")
                print("-------------------")
                print (f"{marcacoes[7]:^5}|{marcacoes[8]:^5}|{marcacoes[9]:^5}|")

                print(f"e a vez do jogador {jogador} ")
                jogada= int(input ("faça sua jogada:"))

                if marcacoes[jogada]=="X" or marcacoes[jogada]== "O":
                    print("jogada invalida jogue de novo ")
                else :
                    break

        marcacoes[jogada]=jogador

        if marcacoes[3]=="X":
            if marcacoes[5]== "X":
                if marcacoes[7]== "X":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[1]=="X":
            if marcacoes[5]== "X":
                if marcacoes[9]== "X":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[1]=="X":
            if marcacoes[2]== "X":
                if marcacoes[3]== "X":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[4]=="X":
            if marcacoes[5]== "X":
                if marcacoes[6]== "X":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[7]=="X":
            if marcacoes[8]== "X":
                if marcacoes[9]== "X":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[3]=="X":
            if marcacoes[6]== "X":
                if marcacoes[9]== "X":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[2]=="X":
            if marcacoes[5]== "X":
                if marcacoes[8]== "X":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[1]=="X":
            if marcacoes[4]== "X":
                if marcacoes[7]== "X":
                    print(f"o {jogador} ganhou")
                    break

        if marcacoes[3]=="O":
            if marcacoes[5]== "O":
                if marcacoes[7]== "O":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[1]=="O":
            if marcacoes[5]== "O":
                if marcacoes[9]== "O":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[1]=="O":
            if marcacoes[2]== "O":
                if marcacoes[3]== "O":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[4]=="O":
            if marcacoes[5]== "O":
                if marcacoes[6]== "O":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[7]=="O":
            if marcacoes[8]== "O":
                if marcacoes[9]== "O":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[3]=="O":
            if marcacoes[6]== "O":
                if marcacoes[9]== "O":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[2]=="O":
            if marcacoes[5]== "O":
                if marcacoes[8]== "O":
                    print(f"o {jogador} ganhou")
                    break
        if marcacoes[1]=="O":
            if marcacoes[4]== "O":
                if marcacoes[7]== "O":
                    print(f"o {jogador} ganhou")
                    break



        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"
        os.system("cls")