import math
# #Задача 1
# Числа, кратные 3 или 5
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
x = 1000
sumultiplesSum = 0
multiplesList = list()
while x > 0:
    x-=1
    if x % 3 == 0:
        multiplesList.append(x)
    elif x % 5 == 0:
        multiplesList.append(x)
print("Сумма чисел кратных 3 и 5 : ", sum(multiplesList))
print('_________________________________________________________')

# Задача 2
# Четные числа Фибоначчи
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
y = 4000000
x = 0
fibonacciSequence = [1, 2]
fibonacciSum = 0
while x < y:
    x = fibonacciSequence[-1] + fibonacciSequence[-2]
    fibonacciSequence.append(x)
for item in fibonacciSequence:
    if item % 2 == 0:
        fibonacciSum+=item
print('Сумма чисел ряда Фибоначчи меньше ' + str(y) + ':', fibonacciSum)
print('_______________________________________________________')



# Задача 3
# Наибольший простой делитель
# Простые делители числа 13195 - это 5, 7, 13 и 29.

# Каков самый большой делитель числа 600851475143, являющийся простым числом? (НЕ РЕШЕНО - не может найти для больших чисел, для маленьких находит !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
x = 13195
y = math.ceil(x/2)
exitFlag = False
while y > 0:
    if x % y == 0:
        z = math.ceil(math.sqrt(y))
        while z > 0:
            if y % z == 0:
                print('Самый большой простой делитель это: ' + str(z))
                exitFlag = True
                break
            z-=1
    y-=1
    if exitFlag:
      break
print('_________________________________________________________')
# Задача 4
# Наибольшее произведение-палиндром
# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
x = 999
y = 999

while x > 0:
    m = list(str(x*y))
    n = list(m)
    n.reverse()
    if m == n:
        print('Самый большой палиндром :', m)
        print('_________________________________________________________')
        break 
    x-=1


# Задача 5
# Наименьшее кратное
# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

# Какое самое маленькое число делится нацело на все числа от 1 до 20? (НЕ РЕШЕНО !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! находит если проверять на числа до 10)
x = 2
while True:
    u = 1
    y = True
    while u < 10:
        if x % u != 0:
            y = False
            break
        u+=1
    if y == True:
        print(x)
        break
    x+=2

# Задача 6
# Разность между суммой квадратов и квадратом суммы
# Сумма квадратов первых десяти натуральных чисел равна

# 12 + 22 + ... + 102 = 385
# Квадрат суммы первых десяти натуральных чисел равен

# (1 + 2 + ... + 10)2 = 552 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.

# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
sum1 = 0
sum2 = 0
x = 0
k = 100
while x <= k:
    sum1+=x*x
    x+=1
x = 0
while x <= k:
    sum2+=x
    if x == k:
        sum2 = sum2**2
    x+=1
print('Разность между суммой квадратов и квадратом суммы первых ста натуральных чисел:', sum2 - sum1)
print('_________________________________________________________')