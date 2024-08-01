"""
x = int(input("Digite o primeiro número: "))
dobro = 2 * x
print("Dobro: ", dobro)

alunos = {3035: "Alexandre", 8965: "Maria", 6758: "José"}
alunos[9090] = "João"
print(alunos)


x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

if (x > y):
  print(x * y)
else:
  print(x/y)

lista = [10, 80, [15, 20, 30], "PYTHON"]
print(lista[2][1])
"""

num = int(input("Digite um número: "))
for i in range(1, num):
  if (i % 2 == 0):
    print(i)