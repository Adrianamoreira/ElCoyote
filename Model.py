#Arquivo Model

import this
this.soma = 0
this.num = 0



#1.Faça um algoritmo que calcule a soma dos números inteiros de 1 a 100.
# while = Utilizo quando eu não sei quantas vezes vou repetir
# for   = Quando eu sei quantas repetições acontecerão
def somarInicioFim(inicio, fim):
    soma = 0 #Instanciei a variável
    for i in range(inicio,fim+1,1):
        soma += i
    return soma

#2. Construa um programa que exiba a tabuada de 1 até N.
def tabuada(num, fim):
    multiplicacao = "" #Instanciando uma variável do tipo texto
    for i in range(1,fim+1, 1):
        multiplicacao += "{} * {} = {}\n".format(num, i, num * i)
    return multiplicacao

#3. Faça um algoritmo que escreva na tela os números
# de um número inicial a um número final. Os números inicial
# e final devem ser informados pelo usuário;
def inicioFim(inicio, fim):
    mostrar = ""
    for i in range(inicio, fim+1, 1):
        mostrar += "{} ".format(i)
    return mostrar

#4. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200;
def impares(inicio, fim):
    impar = ""
    for i in range(inicio, fim+1, 1):
        if i % 2 != 0:
            impar += "{}\n".format(i)
    return impar

def somar10numeros(num):
        this.soma += num
        return this.soma

def leresomaratezero (num):
    this.soma += +num
    return this.soma

#Escreva um algorítimo que calcule a média dos números digitados do usuário, se eles forem pares termine a leitura se usuário digitar zero

def calcularMedia (soma, quantidade):
    return soma / quantidade
def parImpar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def contarValores():
    if valor < 0:
        this.num+= 1
    return this.num

#Escreva um programa que lido um número fatorial
def fatorial(num):
    aux = num
    fat = 1
    while(num> 1):
        fat = fat + num
        num -= 1
        return f"0 fatorial de {aux} é {fat}"

    # Escreva um algorítimo que calcule a média dos números digitados do usuário, se eles forem pares termine a leitura se usuário digitar zero

    def MediaVolei(quantidade):
        return

    def parImpar(num):
        if num % 2 == 0:
            return True
        else:
            return False


#





