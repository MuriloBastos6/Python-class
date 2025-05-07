# texto= ''' este texto
# não é
# linear
# '''
#
# print(texto)
#
# titulo = 'Inicio'
# _ = '!@-' * 20
#
# print(_  + titulo + _)
from pyexpat.errors import messages

# soma = 7 + 5
#
# texto = 'o resultado de 7 + 5 é: '
#
# print(texto , soma)

# numero = 10
# texto = 'o valor é: %d' %  numero
# print(texto)
# print('agora são %d:%d.' % (16, 30))
# print('percetagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.000314))
#  print('decimal: %d, octal: %o, hexadecimal: %x'
#
# numero1 = int(input("digite um numero"))
# numero2 = int(input("digite outro numero"))
#
# resultado = numero1 * numero2
# texto = 'valor de {} vezes {}  é {}'.format(numero1, numero2, resultado)
# print(texto)


# jeito mais usado

# numero1 = int(input("digite um numero"))
# numero2 = int(input("digite outro numero"))
#
# resultado = numero1 * numero2
#
# texto = f'valor de {numero1} vezes {numero2}  é {resultado}'
# print(texto)

# s = 'Olá mundo!'
#
# #tamanho da string
# number = len(s)
# print(number)

# s = 'Olá, mundo!'
#
# #substitui uma substring por outra coisa.
# s1 = s.replace("mundo", "inferno")
#
# print(s1)

# s = 'AAAAAAAAAAAAA'
#
# #substitui uma substring por outra coisa.
# s1 = s.replace("A", "b", 3)
#
# print(s1)

s = 'Olá, mundo!'

# print(s.startswith('Olá'))
# print(s.endswith('mundo'))
# print(s.find('abacate'))
# print(s.count('m'))
#
# # Como "capitalizar" (transformar a primeira letra da primeira
# #palavra em maiúscula).
# s = "ordem e progresso"
# print(s.capitalize())
# # Como verificar se uma string só possui números.
# print('12345'.isdigit())
# print('12345abc'.isdigit())
# # Como verificar se uma string é alfanumérica (só possui letras e
# #números).
# print('12345abc'.isalnum())

# #String.find: procura uma substring em uma string e retorna o
# #indice:
# s = "Pedro, Paulo e Maria"
# print(s.find("a"))
# #Além disso, ela recebe um argumento adicional que especifica o
# #índice pelo qual ela deve começar sua procura:
# print(s.find("a", 10))
# #Ord: Retorna o valor decimal de um caractere
# print(ord('😏'))
# #chr: retorna o caractere de um valor decimal.
# print(chr()).

# s = 'isso é um texto'
#
# print(s.title())
# print(s.upper())
# print(s.lower())

# texto='isso é '
# texto2=' um texto'
# print(texto+texto2)
# texto=texto.rstrip()
# texto2=texto2.lstrip()
# print(texto+texto2)

#frase = 'Só noia nessa poha'

#acessar indice espesifico da string entre [] o numero do indice
#print(frase[0])

#comprimento = len(frase)-1
#print(frase[-2])
#fatia do string
#print(frase[4:10])
#fatiar a string por ordem
# print(frase[::-1])
# frase ='bando de alunos noia do caralho!'
#
# palavras = frase.split()
# print(palavras[::-1])
# print('- '.join(palavras[::-1]))

# email = 'Murilo@fiap.com'
# usuario, sep, dominio = email.partition('@')
# print(usuario, sep, dominio);

# '42'.zfill(5) #'00042'
# '42'.rjust(5,  "*") #'***42'
# '42'.ljust(5, "-") #'42---'
#
# tabela = str.maketrans("aeiou", "@#$%&")
#
# print("substituir vogais".translate(tabela))
#
# #'s5bst3t53r v4g13s'

# bicycles = ['treck', 'cannondale', 'redline', 'specialazed']
# print(bicycles)
# bicycles[0] = 'bmx'
# print(bicycles[0])
# bicycles.append('harley')
# print(bicycles)
# bicycles.insert(1, 'ducati')
# print(bicycles)
# del bicycles[2]
# print(bicycles)
#
# tracks = ['breath', 'on the run', 'time', ]
# lista = tracks
# print(lista)
# tracks.remove('breath')
# tracks.remove('on the run')
# tracks.append('roles')
#
#
# print(lista)

<<<<<<< HEAD
# fibonacci = [0, 1]
#
# n = int(input('digite um numero: '))
#
# for i in range(2, n):
#     fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
# print(fibonacci)


# fibonacci = [0, 1]
# a = 0
# b = 1
# n = 2
#
# while n < 10:
#     n += 1
#     c = a + b
#     fibonacci.append(c)
#     a = b
#     b = c
# print(fibonacci)


# def  saudacao(nome):
#     print(f'Olá {nome}, seu noia!')
#
# saudacao('batata')

# def  saudacao(nome):
#     '''
#     ESSA FUNCÇÂO SERVE PARA SAUDAR UM ALUNO NOIA
#     '''
#     return (f'Olá {nome}, seu noia!')
#
# mensagem = saudacao('batata')
#
# print(mensagem)

# def calcular_media(a, b):
#     return (a + b) / 2
#
# n1 = float(input('digite sua media:'))
# n2 = float(input('digite sua media:'))
#
# media = calcular_media(a=n1, b=n2)
#
# print(media)

# def somar(a = 2, b = 3):
#     return a + b
#
# resultado = somar()
# print(resultado)

# def altera_a(a):
#     a = a + 1
#     print(a)
# a = 2
# altera_a(a)
#
# print(a)

# def alterar_lista(lista):
#     lista.append(2)
#     lista.append(5)
#
#     print(lista)
#
# lista = [1, 7, 8, 3]
# alterar_lista(lista[:])
#
# print(lista)

# def soma_total(*numeros):
#     '''
#     Esta função aceita um numero arbitrário de argumentos e retorna a soma de todos.
#     '''
#
#     return sum(numeros)
#
# print(soma_total(1, 2, 3))
# print(soma_total(10, 20, 30, 40))
# print(soma_total())


# def exibir_informacoes(**informacoes):
#     '''
#     Esta função aceita um numero arbitrario de argumentos nomeados e os exibe.
#     '''
# for chave, valor in informacoes.items():
#     print(f"{chave}: {valor}")
#
# exibir_informacoes(nome="ana", idade=35, cidade="sao paulo")
# exibir_informacoes(produto="notebook", preco=2500.00, modelo="dell")


##utilizando eval na especificação de escopo global

# # Definindo uma expressão matemática em forma de string
# x = 2
# expressao = ('print("x + 3 * 5")')
# # Usando eval para avaliar a expressão
#
# eval(expressao, {}, {'x': x})
# # Exibindo o resultado

#definindo uma expresão matematica em forma de string
# x = 3
#
# def minha_funcao():
#     global x
#     x=4
# minha_funcao()
# print(x)
#
# code_str = """
# result = []
# for i in range(10):
#     if i % 2 == 0:
#         result.append(i)
# print(result)
# """
# # Usando eval para executar a string como código Python
# exec(code_str)


# def fatorial(n):
#     if n < 2:
#         return 1
#
#
#     fat = 1
#     for i in range(2, n + 1):
#         fat *= i
#
#     return fat
# print(fatorial(8))
#
# def fatorial(n):
#     if n < 2:
#         return 1
#
#     return n * fatorial(n - 1)
#
# print(fatorial(999))


def multiplicaçao(m,n):
    if m == 0 or n == 0:
        return 0
    if n == 1:
        return m

    return m + multiplicaçao(m, n -1)
print(multiplicaçao(5, 2))

def contaegem_regressiva(m):
    print(m)
    if m == 0:
        return 0
    return contaegem_regressiva(m-1)

contaegem_regressiva(5)

frase = 'Meu ovo '

vogais = ['a', 'e', 'i', 'o', 'u']


def vogal():
    if
=======
# opcao = 'a'
# #
# # match opcao:
# #      case 'a':
# #          print("opcao A selecionada")
# #      case 'b':
# #          print("opcao B selecionada")
# #      case _:
# #       print("opção invalidada")


>>>>>>> 1b3b550fd757c3e64a80c313832ef837ecb018b5
