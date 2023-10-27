#Arquivo Control
from Model import somarInicioFim #Conecta a classe model e control
from Model import tabuada
from Model import inicioFim
from Model import impares
from Model import somar10numeros
from Model import calcularMedia
from Model import parImpar
from Model import fatorial

import this
this.num = 1#acionar o While
from Model import leresomaratezero



import this
this.opcao = -1 #Declarando a variável
def exercicio01():
    inicio = int(input("Informe o início: "))
    fim    = int(input("Informe o fim: "))
    print(somarInicioFim(inicio,fim))
def exercicio02():
    num = int(input("Informe o número que deseja multiplicar: "))
    fim = int(input("Informe até onde deve ser multiplicado: "))
    print(tabuada(num,fim))
def exercicio03():
    inicio = int(input("Informe o valor inicial: "))
    fim    = int(input("Informe o valor final: "))
    print(inicioFim(inicio, fim))
def exercicio04():
    inicio = int(input("Informe o início: "))
    fim    = int(input("Informe o final: "))
    print(impares(inicio, fim))
def menu():
    print("\nEscolha uma das opções abaixo: \n" +
          "0. Sair\n" +
          "1. Exercício 01\n" +
          "2. Exercício 02\n" +
          "3. Exercício 03\n" +
          "4. Exercício 04\n" +
          "5. Exercício 05\n" +
          "6. Exercicio 06\n" +
          "7. Exercício 07\n" +
          "13.Exercício 13\n")


    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu() #Chamar o menu
        if this.opcao == 0:
            print("Obrigado!")
        elif this.opcao == 1:
            exercicio01()
        elif this.opcao == 2:
            exercicio02()
        elif this.opcao == 3:
            exercicio03()
        elif this.opcao == 4:
            exercicio04()
        elif this.opcao == 5:
            exercicio05()
        elif this.opcao == 9:
            Exercício09()
        elif this.opcao == 10:
            Exercício10()
        elif this.opcao == 11:
            Exercício11()
        elif this.opcao == 12:
            Exercício12()
        elif this.opcao == 13:
            Exercício13()
        else:
             print("Erro! Escolha uma opção válida!")

def exercicio05():
    for i in range(10):
        num = int(input("informe {} informe número:".format(i + 1)))
        soma = somar10numeros(num)
    print("A soma dos numeros digitados é: {}".format(soma))

def Exercício09():
    while (this.num != 0):
        this.num = num = int(input("informe um valor: "))
        soma = somar10numeros(num)
    print("A soma dos valores é: {}".format(soma))

def Exercício10(num):
    while (this.num != 0):
        this.num = int(input("Informe um número: "))
        if parImpar(this.num) == True:
            soma = somar10numeros(this.num)
            this.i += 1 #contar quantos numeros foram digitados
    print("A média dos numeros digitados é: {}".format(calcularMedia(soma, this.i)))

def Exercício11():
    while(this.num !=0):
        this.num = int(input("Informe um número"))
        #Primeira digitação do usuário
        if this.num !=0:
            if this.i == 0:
                maior = this.num
                menor = this.num
        this.i += 1
        #A partir da segunda volta...
        if this.num > maior:
           maior = this.num
        if this.num < menor:
            menor = this.num

            if this.num  < menor:
                menor = this.num
    print("O maior número digitado é: '{maior}' \ne o menor número digitado é: '{menor}'")

def Exercício12():
    for i in range(20):
        this.num = int(input("Informe um valor: "))
        #A soma dos numeros positivos
        if this.num >= 0:
            soma = somar10numeros(this.num)
            #A quantidade de valores  negativos
        else:
            this.negativo += 1
    print(f"Há {this.negativo} números negativos\nA soma dos positivos é {soma}")

def Exercício13():
    num = int(input("Informe um número:"))
    print(fatorial(num))

def exercicio14():
    quantidade = in(input("Informe a quantidade de jogadores: "))
    altura = -1
    for i in range(0, quantidade, 1):
        altura = float(input(f"1+1}" altura: "))
        if altura < 0:
            print("Erro! Informe uma altura positiva!")
        altura = float(input(1 + 1)" altura: "))
     if altura < 0:
         soma = somar10numeros(altura)
         print(f"A media de altura desse time é: {calcularMedia(soma, quantidade)}"

def Exercicio15():
    this.venc = ""
    for i in range(0, 16, 1):
        nota = float(input("Informe a primeira nota: "))
        while(nota < 0 or nota > 10):
            print("Erro, informe uma nota entre 0 e 10")
            nota = float(input(f))
        cand = input(f"'{i + 1}'candidata: ")

        if i ==0:
            maior = nota

        if nota > maior:
           maior = nota
           this.venc = cand

            print(f"A vencedora é: {venc}, sua nota foi: {maior}")






