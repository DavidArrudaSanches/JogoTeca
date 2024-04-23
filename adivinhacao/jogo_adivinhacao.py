import random

def jogo_adivinhacao():
    v1 = random.randint(1,5)
    v2 = random.randint(1,20)
    v3 = random.randint(1,50)
    v4 = random.randint(1,100)

    facil = 1000
    medio = 2000
    dificil = 3000
    hard = 4000

    chanses = 4

    dificuldade = int(input("digite a dificuldade, 1000, 2000, 3000, 4000: "))

    if dificuldade == 1000:
        for x in range(5):

            print("adivinhe o numero que estou penssando de 1 a 5")
            resp = int(input("digite um numero: "))

            if resp == v1:
                print("VC ACERTOU")

            if resp != v1:
                print(f"vc tem mais {chanses} chanses")
                chanses -= 1

        if chanses <= 0:
            print("vc morreu de vez")

    if dificuldade == 2000:
        for x in range(5):

            print("adivinhe o numero que estou penssando de 1 a 20")
            resp = int(input("digite um numero: "))

            if resp == v1:
                print("VC ACERTOU")

            if resp != v1:
                print(f"vc tem mais {chanses} chanses")
                chanses -= 1

        if chanses <= 0:
            print("vc morreu de vez")

    if dificuldade == 3000:
        for x in range(5):

            print("adivinhe o numero que estou penssando de 1 a 50")
            resp = int(input("digite um numero: "))

            if resp == v1:
                print("VC ACERTOU")

            if resp != v1:
                print(f"vc tem mais {chanses} chanses")
                chanses -= 1

        if chanses <= 0:
            print("vc morreu de vez")

    if dificuldade == 4000:
        for x in range(5):

            print("adivinhe o numero que estou penssando de 1 a 100")
            resp = int(input("digite um numero: "))

            if resp == v1:
                print("VC ACERTOU")

            if resp != v1:
                print(f"vc tem mais {chanses} chanses")
                chanses -= 1

        if chanses <= 0:
            print("vc morreu de vez")
if "__main__"== __name__:
    jogo_adivinhacao()
