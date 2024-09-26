import math

x = 3
b = 1
a = 2
c = 3
e = 4
y = 5

conta1 = ((3 * (x ** 2)) + (2 * x) - 4)

conta2 = (1 / ((x ** 2) + (1)))

conta3 = ((5 * (x ** 3)) - ((2 * (x ** 2)) + (2 * 1)) + (7 * 3) - 10)

conta4 = ((3 * x) + (3 * 1)) / ((2 * x) - 5)

#conta5 = (((b ** 2) - (4 * a * c)) ** 0.5)

conta6 = ((x ** 4) - (2 * (x ** 2)) + (x - 7))

conta7 = ((x + 5) - 3) ** 0.5

conta9 = ((x ** 3) + (2 * x)) / ((x ** 2) - 4)

conta10 = (math.log(x) + (e ** x))

conta11 = ((x ** 2) + (1 ** 2)) - ((x ** 2) - (2 ** 2))

conta12 = ((a * (x ** 2)) + ((b * x) + c))

conta13 = (x ** 0.5) / (x + 1)

conta14 = (e ** (2 * x)) + ((4 * x) - 6)


conta15 = ((x ** 2) - 1) / (x + 2)

conta17 = (a * b) ** 0.5

conta18 = (1 / x) + (1 / (x ** 2)) + (1 / (x ** 3))

conta19 = ((3 * x) + (5 * 3)) / ((x ** 2) + 1)

conta20 = (2 * x) + (3 * y) == 5

def soma(x, y):
    result = x + y
    return result

for i in range(0, 10):
    print(i)

if (x > 10):
    print("Maior que 10")
else:
    print("Menor ou igual a 10")

while x < 100:
    print(x)
    x += 1

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

my_list = [1, 2, 3, 4]
for i in my_list:
    print(i)

try:
    result = 10 / 0
except ZeroDivisionError: print("Divisão por zero!")

def multiply(a, b):
    product = a * b
    return product

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

if x > 5:
    print("x is greater than 5")
elif x < 5:
    print("x is less than 5")
else:
    print("x is equal to 5")

def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    return num3

my_dict = {
    'key1': 'value1',
    'key2': 'value2', 
    'key3': 'value3'}
for key, value in my_dict.items():
    print(key, value)

with open('file.txt', 'r') as file:
    for line in file:
        print(line)

def calculate_area(radius):
    pi = 3.14
    area = pi * radius**2
    return area

import math
def calc_hypotenuse(a, b):
    hypotenuse = math.sqrt(a^2 + b^2)
    return hypotenuse

for i in range(0, 10):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")

my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 10
print(my_tuple)

def create_dict(keys, values):
    result_dict = {}
    for key in keys:
        result_dict[key] = values[key]
    return result_dict

print('''
1. True or False é uma expressão válida em Python. T
2. Um comentário em Python é criado usando #. T
3. Em Python, x = y = z = 10 é uma atribuição válida. T
4. Em Python, as strings são imutáveis. T
5. O loop for i in range(1, 10) vai de 1 até 10, incluindo F
5. O método append() adiciona um item ao final de uma lista. T
7. A instrução break é usada para sair de um loop imediatamente. T
8. O operador == é usado para atribuição em Python. F
9. As tuplas em Python são mutáveis. F
10. O método pop() remove e retorna o último item de uma lista. T
11. O operador is compara se duas variáveis referenciam o mesmo
objeto na memória. T
12. O operador // é usado para divisão inteira. T
13. Um dicionário em Python não pode ter chaves duplicadas. T
14. Em Python, a == b verifica se a e b têm o mesmo valor. T
15. A função len() retorna o número de elementos de uma lista ou
tupla. T
16. A função input() lê uma entrada do usuário como um número
inteiro. F
17. As listas em Python podem conter elementos de tipos diferentes. T
18. Uma string em Python pode ser concatenada usando o operador +. T
19. Em Python, None é o equivalente a null em outras linguagens. T
20. O loop while True: executa infinitamente até encontrar um
break. T
21. A função int() converte uma string para número inteiro, se
possível. T
22. Em Python, 4 ** 2 resulta em 16. T
23. O método sort() modifica a lista original em vez de retornar
uma nova lista. T
24. O método copy() de um dicionário retorna uma cópia rasa
(shallow copy). T
25. O Python distingue entre maiúsculas e minúsculas nas variáveis. T
26. O operador in é usado para verificar a presença de um elemento
em uma lista. T
27. As funções em Python podem retornar múltiplos valores. T
28. Em Python, try e except são usados para tratamento de
exceções. T
29. O operador not inverte o valor de uma expressão booleana. T
30. O método extend() de uma lista insere um único elemento no
final da lista. F
31. O índice de listas e strings começa a partir de 1 em Python.  F
32. O método strip() remove espaços em branco apenas no início
de uma string. F
33. Funções em Python são definidas com a palavra-chave
function. F
34. O Python suporta herança múltipla em classes. T 
35. As funções lambda podem ter múltiplas expressões. T
36. O comando pass é usado quando você não quer executar
nenhuma ação. T
37. O Python 3.0 introduziu a divisão de números inteiros como
resultado float por padrão. T
38. Em Python, print é uma função e deve ser usada com
parênteses. T
39. Em Python, os elementos de um conjunto (set) são ordenados. F
40. Uma função em Python pode ser definida dentro de outra função. T


''')