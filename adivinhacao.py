import random

def jogar():

    cabecalho_jogo()

    numero_secreto = gera_num_secreto()
    pontuacao = 500


    escolher_dificuldade()
    

    nivel = 10
    while nivel > 3:
        nivel = int(input("Defina seu nível: "))

    if nivel == 1:
        tentativas = 20
        print("Nível escolhido: #Fácil#")
    elif nivel == 2:
        tentativas = 10
        print("Nível escolhido: #Médio#")
    else:
        tentativas = 5
        print("Nível escolhido: #Difícil#")

    pontos_reducao = pontuacao / tentativas

    for rodada in range(1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}')

        chute = int(input("Digite um numero entre 1 e 100: "))

        print(f'Número de chute {chute}')

        if chute < 1 or chute > 100:
            print("Atenção! Você deve digitar um número entre 1 e 100!")
            pontuacao -= pontos_reducao
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Acertou!!! Parabéns, sua pontuação final é de {pontuacao}")
            break
        else:
            if maior:
                print("Errou! Seu chute é maior que o número secreto.")
            elif menor:
                print("Errou! Seu chute é menor que o número secreto")

            pontuacao -= pontos_reducao

            if(rodada == tentativas):
                print(f'O número correto é: {numero_secreto} e sua pontuação final é de 0')

    print("Fim do jogo!")

def cabecalho_jogo():
    print("*************************")
    print("***Jogo de Adivinhação***")
    print("*************************")
def gera_num_secreto():
   return random.randrange(1,101)
def escolher_dificuldade():
    print("Escolha abaixo o nível de dificuldade:")
    print("(1) - Fácil | (2) - Médio | (3) - Difícil")
    

if(__name__ == "__main__"):
    jogar()
