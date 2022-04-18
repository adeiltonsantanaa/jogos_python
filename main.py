import forca
import adivinhacao

print("***********************")
print("*****Menu de jogos*****")
print("***********************")

print("Escolha abaixo o jogo que deseja iniciar.")
print("(1) - Forca  |  (2) - Adivinhação")

jogo_escolhido = int(input("Digite sua escolha: "))

if jogo_escolhido == 1:
    print("Forca escolhido")
    forca.jogar()
elif jogo_escolhido == 2:
    print("Adivinhação escolhido")
    adivinhacao.jogar()