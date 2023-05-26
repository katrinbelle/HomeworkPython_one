# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой 
#между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
#Сумма трехзначных чисел
tripeDigits=int(input("Введите число-> "))
flag=True
while flag:
    if tripeDigits >=100 and tripeDigits <1000:
        flag=False
    else: tripeDigits=int(input("Введите число повторно-> "))
print(int(int(tripeDigits/100)+tripeDigits/10%10+tripeDigits%10))
#Количество журавлей cltkfkb ltnb
countCrane=int(input("Введите число журавликов-> "))
if countCrane<=5: print("Не получается подсчитать")
else:
    boysTogether=countCrane//6
    print(f"Петя и Сережа сделали по {boysTogether}, катя сделала {(boysTogether+boysTogether)*2}")
#счастливый билет 
happyTisket=int(input("Введите номер билет, чтобы проверить->   "))
flagTwo=True
while flag:
    if tripeDigits>=100000 and tripeDigits<1000000:
        flagTwo=False
    else: happyTisket=int(input("Введите число повторно-> "))
ferstThreeHundred=happyTisket//1000000%10+happyTisket//10000%10+happyTisket//10000%10    
secondThreeHundred=happyTisket//100%10+happyTisket//10%10+happyTisket%10
if ferstThreeHundred==secondThreeHundred: print(f"{happyTisket} -это счастливый билет")
else: print(f"{happyTisket} -это не счастливый билет")
#Число долek
countSlice=int(input("Введите количество долек->    "))
sizeChocolate=input("Введите размер плитки->")
sizeChocolate=list(map(int,sizeChocolate.split()))
lenghtChocolate=int(sizeChocolate[0])
widhtChocolate=int(sizeChocolate[1])

if lenghtChocolate==countSlice: print("yes")
elif widhtChocolate==countSlice: print("yes")
else:
    minNumberSizeChocolate=lenghtChocolate
    if lenghtChocolate>widhtChocolate: minNumberSizeChocolate=widhtChocolate
    flag=True
    size=lenghtChocolate*widhtChocolate
    while flag:
        print(minNumberSizeChocolate)
        if minNumberSizeChocolate==countSlice:
            print("Да")
            flag=False
        elif minNumberSizeChocolate>=size:
            print("NO")
            flag=False
        else:  minNumberSizeChocolate+=2
       
     
