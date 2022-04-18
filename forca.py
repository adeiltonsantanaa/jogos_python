import random
import ascii


def jogar():
    
    inicia_cabecalho()
    palavra_secreta = carrega_palavra()
    posicao_letras = carrega_posicao(palavra_secreta)

    letras_utilizadas = []
    acertou = False
    enforcou = False
    erros = 0

    while(not acertou and not enforcou):
        print(f"Palavra secreta: {' '.join(posicao_letras)}")
        exibe_letras_digitadas(letras_utilizadas)
        chute = input("Chute uma letra que você ache que está na palavra: ").upper().strip()
        if verifica_chute(chute, letras_utilizadas):
            continue

        letras_utilizadas.append(chute)

        if chute in palavra_secreta:
            exibe_letras_ocultas(palavra_secreta, chute, posicao_letras)
        else:
            erros += 1
            desenha_forca(erros)
            print(f"Você errou e já tem {erros} erro(s)")

        enforcou = erros == 7
        acertou = "_" not in posicao_letras

    if acertou:
        imprime_mensagem_venceu()
    else:
        imprime_mensagem_perdeu(palavra_secreta)




def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    return palavras[random.randrange(0, len(palavras))].upper()

def carrega_posicao(palavra):
    return ["_" for l in palavra]

def exibe_letras_digitadas(letras):
    if len(letras):
        print(f"Letras já digitadas: {', '.join(letras)}")

def verifica_chute(chute,letras_utilizadas):
    if chute in letras_utilizadas:
        print("Essa letra já foi utilizada! Tente outra vez.")
        return True
    return False

def exibe_letras_ocultas(palavra_secreta, chute, posicao_letras):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            posicao_letras[index] = letra
        index += 1

def gera_imagem(url):
    output = ascii.loadFromUrl(url)
    return output
def imprime_mensagem_venceu():
    print("Parabéns, você ganhou!")
    print(gera_imagem('https://img.lovepik.com/free-png/20220120/lovepik-trophy-png-image_401523290_wh860.png'))

    '''print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")'''

def imprime_mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print(gera_imagem('http://2.bp.blogspot.com/-gRRxqUEzMf8/UA5jG91WHEI/AAAAAAAAAFc/-2wqVNrdTGA/w1200-h630-p-k-no-nu/caveira.jpg'))
    '''print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")'''

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def inicia_cabecalho():
    print("*************************")
    print("******Jogo da Forca******")
    print("*************************")
    print("Jogo iniciado!")

if(__name__ == "__main__"):
    jogar()
