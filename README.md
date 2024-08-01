### Python - Características

- Lançada na Holanda em 1991 por Guido van Rossum;
- Seu nome (Python) teve a sua origem no grupo humorístico
britânico Monty Python;
- Open Source e compatível com a GPL (General Public License)
- Imperativa, orientada a objetos e funcional (ou seja, abrange todos os principais paradigmas da programação);
- Usada nas mais diversas plataformas: desktop, web, mobile, dispositivos embarcados, análise de dados;
- Parte integrante dos sistemas operacionais Linux;

### Python - Instalação

- Usaremos a versão mais recente do interpretador do Python;
- No windows, baixe o [Python](https://www.python.org/downloads/)
- Abra um terminal e digite python (windows) ou python3 (linux). Este comando retornará a versão do Python que está instalada em seu sistema.;
- Deve aparecer algo do tipo;
![](/assets/img/python-versao.PNG "")

### Python - Executar no VSC (Visual Studio Code)

- Abra o Visual Studio Code;
- Acesse a aba de extensões;
- Procure pela extensão do Python. Encontre a extensão oficial do Python desenvolvida pela Microsoft (geralmente é a primeira da lista);
- Instale a extensão.
- Crie um arquivo com a extensão <nome>.py e no terminal executamos com o comando python <nome>.py
- ![](/assets/img/python-vsc.PNG "")
  
### Python - Tipos de Dados

- int - Números inteiros
- float - Números de ponto flutuante (decimais)
- str - Cadeias de caracteres (strings)
- bool - Valores booleanos (True ou False)
- list - Listas (mutáveis, ordenadas)
- tuple - Tuplas (imutáveis, ordenadas)
- dict - Dicionários (mutáveis, pares de chave-valor)
- set - Conjuntos (mutáveis, não ordenados, elementos únicos)

```py
# Tipo int
numero_inteiro = 10

# Tipo float
numero_decimal = 3.14

# Tipo str
texto = "Olá, mundo!"

# Tipo bool
booleano = True

# Tipo list
lista = [1, 2, 3, 4, 5]

# Tipo tuple
tupla = (1, 2, 3, 4, 5)

# Tipo dict
dicionario = {"chave1": "valor1", "chave2": "valor2"}

# Tipo set
conjunto = {1, 2, 3, 4, 5}
```

### Python - Estrutura Sequencial
É a execução de instruções de maneira linear, uma após a outra, na ordem em que aparecem no código.

**Características da Estrutura Sequencial**

1. Execução Linear: As instruções são executadas uma após a outra, de cima para baixo.
2. Sem Desvios ou Repetições: Não há saltos (como loops ou condicionais) ou repetições de blocos de código.
3. Simples e Direta: Ideal para operações simples e diretas onde a ordem das operações é importante.

### Python - Atribuição Múltipla

Permite a atribuição de valores a várias variáveis ao mesmo tempo em uma única linha de código.
```py
# Exemplo 1
a, b, c = 1, 2, 3
print(a)  # Saída: 1
print(b)  # Saída: 2
print(c)  # Saída: 3

# Exemplo 2
x, y = 5, 10
x, y = y, x
print(x)  # Saída: 10
print(y)  # Saída: 5
```

### Python - Entrada de Dados

- a função `input()` é utilizado para receber dados digitados pelo usuário;
- Os dados são armazenados em variáveis;
- Retorna os dados informados como sendo do tipo string;
  
```py
# Solicita ao usuário que digite algo
nome = input("Digite seu nome: ")

# Exibe a entrada do usuário
print("Olá, " + nome + "!")
```

Por padrão, `input()` retorna os dados como uma string. Se você precisa de um tipo diferente (como um número inteiro ou um número de ponto flutuante), você precisa converter a string. Aqui estão alguns exemplos:

```py
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
print("Soma: ", + x + y)
```

### Python - Operadores
| Operador  | Python        |
| :----:    | :----       |
| =         | atribuição    |
| +         | soma          |
| -         | subtração     |
| *         | multiplicação |
| **        | exponenciação |
| /       | divisão (real) |
| //       | divisão (inteira) |
| %       | resto da divisão de x por y |

### Python - Operadores Lógicos
| Operador | Python |
| :----:   | :----: |
| E        | and    |
| OU       | or     |
| =        | ==     |
| !=       | !=     |

### Python - Estrutura Condicional Simples
É usada para executar um bloco de código se uma determinada condição for verdadeira.

### Python - Estrutura Condicional Composta
É usada para executar um bloco de código se uma condição for verdadeira e outro bloco de código se a condição for falsa.

### Python - Estruturas de Repetição - FOR
O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, string, ou um objeto iterável) e executar um bloco de código para cada item nessa sequência.

### Python - Estruturas de Repetição - WHILE
O loop while é usado para executar um bloco de código repetidamente enquanto uma condição especificada for verdadeira. 

`range` é uma função que gera uma sequência de números. É comumente usada em loops, especialmente em loops for, para iterar sobre uma sequência de números. A função range pode ser usada de várias maneiras, dependendo do número de argumentos fornecidos.


### Python - Estruturas de Dados

- Lista
- Tupla
- Dicionário

### Python - Estruturas de Dados - Lista

### Python - Estruturas de Dados - Tupla

### Python - Estruturas de Dados - Dicionário