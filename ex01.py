import math # biblioteca math

# print("Hello World")

"""
expressao = input("Digite uma expressão: ")
resultado = eval(expressao)
print("Resultado:", resultado)
"""

a = 10
b = 20
c = a + b
# print(c)

a = "Python"
# print(type(a))

# nome = input("Digite o seu nome: ")
# sobrenome = input("Digite o seu sobrenome: ")
# print("Olá, " + nome + " " + sobrenome)

"""
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
print("Soma:", + x + y)
print("Soma: " + str(x + y))
"""

# x = int(input("Digite um número: "))
# y = math.sqrt(x) # Retorna a raiz quadrada de x
# z = math.pow(x, 3) # Retorna x elevado à potência de 3
# print("Raiz:", y)
# print("Potência:", z)

"""
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_futuro = 2050

print("Você tem " + str(ano_atual - ano_nascimento) + " anos")
print("Em 2050 você terá " + str(ano_futuro - ano_nascimento) + " anos")
"""

# Estrutura Condicional Simples

x = 10
if(x < 20):
  x = x + 5
print(x)

# Estrutura Condicional Composta

"""
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

if (numero_1 > numero_2):
  print("Maior", numero_1)
  print("Menor", numero_2)
elif (numero_2 > numero_1):
  print("Maior", numero_2)
  print("Menor", numero_1)
else:
  print("Os números são iguais")

print("Fim")
"""

"""
lado_A = float(input("Digite o primeiro lado: "))
lado_B = float(input("Digite o segundo lado: "))
lado_C = float(input("Digite o terceiro lado: "))

if (lado_A == lado_B and lado_A == lado_C):
  print("Equilátero")
elif(lado_A == lado_B or lado_A == lado_C or lado_B == lado_C):
  print("Isósceles")
else:
  print("EScaleno")
"""

"""
nota_A = float(input("Digite a primeiro nota: "))
nota_B = float(input("Digite a segundo nota: "))
nota_C = float(input("Digite a terceiro nota: "))
media = ((nota_A + nota_B + nota_C)/3)

if ((media >= 0) and (media < 3)):
  print("Reprovado")
elif (media >= 3) and (media < 7):
  print("Exame")
elif(media >= 7) and (media <= 10):
  print("Aprovado")
"""

"""
# Estruturas de Repetição - FOR
for i in range(10):
  print(i)

# Estruturas de Repetição - WHILE
x = 1
y = 10
while (x < y):
  print("Valor de y", y)
  y = y - 2
"""



idade = int(input("Digite uma idade: "))
while(idade < 0):
  idade = int(input("Idade Inválida. Digite a idade novamente: "))
print("Idade Válida")
  
  
    



















