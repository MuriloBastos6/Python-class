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
