"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

import random

while True:
    num = random.randrange(2, 12)
    if num == 7 or num == 11:
        print(f"O número sorteado foi {num}\nNatural! Parabéns você ganhou!") 
        break
    elif num == 2 or num == 3 or num == 12:
        print(f"O número sorteado foi {num}\ncraps! Você perdeu!")
        break
    else:
        ponto = num
        while True:
            num = random.randrange(2, 12)
            if num == 7:
                print(f"O número sorteado foi {num}. Você perdeu!")
                break
            elif num == ponto:
                print(f"O número sorteado foi {num}. Parabéns você ganhou! ")
                break
        