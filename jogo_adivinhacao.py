#Jogo de Adivinhacao
#Gilson Rodrigues 7.10.23


import random
import os
 


acertos=0
erros=0
auxiliar=False
letra_escolhida=""
tentativas_restantes=10
letras_usadas=[]



os.system ('cls')

matriz_palavras = [
         ["opala","camaro","golf","corola","santana","maverick","fusca","omega","ferrari"],
         ["hoquei","futebol","voleibol","ciclismo","natacao","basquete","corrida","rugby","handebol"],
         ["onibus","caminhao","motocicleta","bicicleta","metro","charrete","bonde","skate","lancha"]]


print("Seja bem vindo ao Jogo ADVINHE A PALAVRA!\n")
print("REGRAS: ")
print("*Voce tera duas dicas: o numero de letras e o assunto que a palavra esta relacionada.")
print("*Voce tera ate 10 chances de dizer uma letra que complete a palavra")
print("*Se acertar 3 voce tera uma unica chance de dizer a palavra, ou entao, GAME OVER!")
inicio=bool(input("Boa Sorte! Aperte ENTER para iniciar o jogo\n"))




def sortear():
    global coluna_sorteada
    global linha_sorteada
    global palavra_sorteada
    global quantidade_caracteres

    coluna_sorteada=random.randint(0, 9)
    linha_sorteada=random.randint(0, 2)
    palavra_sorteada=(matriz_palavras[linha_sorteada][coluna_sorteada])
    quantidade_caracteres = len(palavra_sorteada)

def preencher_lacunas():
     global contador
     global palavra_em_formacao

     contador=0
     palavra_em_formacao=[]
     while contador<quantidade_caracteres:
        palavra_em_formacao.append("_")
        contador+=1
    
def solicita_escolha_letra():
     global letra_escolhida
     letra_escolhida=str(input("Escolha uma letra: "))
     letras_usadas.append(letra_escolhida)
     

def analisar_letra_escolhida():    
    global contador
    global palavra_em_formacao
    global palavra_sorteada
    global auxiliar
    contador=0
    while contador<quantidade_caracteres:
          if palavra_sorteada[contador]==letra_escolhida.lower():
             palavra_em_formacao[contador]=letra_escolhida.upper()
             auxiliar=True
          contador+=1
    
def exibir_informacoes():
    os.system('cls')
    print("Letras usadas: " + str(letras_usadas))
    print("Numero de tentativas restantes: " + str(tentativas_restantes) + "\n")
    if linha_sorteada==0:
            print("Dica: Modelo de carro\n")
    elif linha_sorteada==1:
            print("Modalidade de esporte\n")
    else:
            print("Dica: Veiculo de transporte\n")
    print(palavra_em_formacao)


def executar():
    global acertos
    global erros
    global auxiliar
    sortear()
    preencher_lacunas()
    exibir_informacoes()

    while (acertos<3) and (erros<7):
        solicita_escolha_letra()
        analisar_letra_escolhida()
        if auxiliar==True: 
            acertos+=1
            auxiliar=False
        else: 
            erros+=1 
        tentativas_restantes=10-(acertos+erros)
        exibir_informacoes()


        if acertos==3: 
            palavra_adivinhada=input("Responda qual e a palavra: ")
            if palavra_adivinhada.upper()==palavra_sorteada.upper():
                os.system('cls')
                print("Parabens! Voce acertou!!")
            else:
                os.system('cls')
                print("Infelizmente voce errou!!")
        if erros==7:
            os.system('cls')
            print("Infelizmente voce nao tem mais tentativas!")
            

if inicio==False:
     executar()
