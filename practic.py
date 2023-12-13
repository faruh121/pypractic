# n = int(input("Введите размер квадрата:"))
# for i in range(n):
#     print(" * "*n)


# s = int(input("Введите ширину прямоугольника:"))
# m = int(input("Введите высоту прямоугольника:"))
# for i in range(s):
#     print(" * " *m)

# n = int(input("Введите размер квадрата:"))
# for i in range(n):
#     for j in range(n):
#         print('*'if i in [0,n-1] or j in [0,n-1] else ' ',end=' ')
#     print()

# s = int(input("Введите ширину:"))
# d = int(input("Введите длинну:"))

# for n in range(s):
#     for x in range(d):
#         print('*'if n in [0,s-1] or x in [0,d-1] else ' ',end=' ')
#     print()
# while True:
#     zad = int(input("Какую задачу от 1 до 4: "))



#     if zad==1:
#         num = int(input("Введите число:"))
#         choice = int(input("Cделайте выбор - 1 количество цифр в числе, 2 сумму этих цифр, 3 cредне арифметическое этих цфир, 4 количество нулей введеного вами числа:"))
#         listsum = []
#         listcol = []
#         cnt = 0
#         cnt1= 0
#         while choice not in range(1,5):
#             print("Такого варианта нет выберете из предложеных:")
#             choice = int(input("Cделайте выбор - 1 количество цифр в числе, 2 сумму этих цифр, 3 cредне арифметическое этих цфир, 4 количество нулей введеного вами числа:"))

#         else:
#             while num!=0:
#                 cnt+=1
#                 num//=10
#             listcol.append(cnt)
#             if choice == 1:
#                 print(listcol[0])
#             elif choice == 2:
#                 while num!=0:
#                     num//=10
#                     cnt1+=1
#                     listsum.append(cnt1+1)
#                 print(sum(listsum))
#             elif choice == 3:
#                 srednearif = sum(listsum) / len(listcol)
#                 print(srednearif)
            
#     elif zad==2:
#         r = int(input("Размер клетки:"))
#         for i in range(6):
#             print(('*'*r +'_'*r)*8)
        

#     # # Написать программу, которая проверяет пользователя 
#     # # на знание таблицы умножения. Программа выводит на 
#     # # экран два числа, пользователь должен ввести их произведение. Разработать несколько уровней сложности (личаются сложностью и количеством вопросов). Вывести 
#     # # пользователю оценку его знаний.
#     elif zad==3:
#         import random
#         #1 dif
#         sl1 = random.randint(2,4)
#         sl1_1 = random.randint(5,6)

#         sl12_1 = random.randint(3,5)
#         sl12_2 = random.randint(6,7)

#         #2 dif
#         sl2 = random.randint(6,7)
#         sl2_1 = random.randint(8,9)

#         sl21_1 = random.randint(7,8)
#         sl21_2 = random.randint(9,10)
#         #dif 3 
#         sl3 = random.randint(8,9)
#         sl3_1 = random.randint(10,11)

#         sl31_1 = random.randint(9,10)
#         sl31_2 = random.randint(11,12)


#         cntschetzad = 0
#         cnttab = cntschetzad
#         while True:
#             slojnost = int(input("1 - новичок;\n2 - хорошист;\n3 - гений;\nВыберите сложность: "))

#             if slojnost==1:
#                 for i in range(sl1,sl1_1):
#                     for x in range(sl12_1+1,sl12_2):
#                         a = int(input("Введите ответ:" + str(i) + "*"+str(x) + " = "))
#                         cntschetzad+=1
#                     if a == i*x:
#                         cnttab +=0
#                     elif a!=i*x:
#                         cnttab -=1
#             if slojnost==2:
#                 for i in range(sl2,sl2_1):
#                     for x in range(sl21_1+1,sl21_2):
#                         n = int(input("Введите ответ:" + str(i) + "*"+str(x) + " = "))
#                         cntschetzad+=1
#                     if n == i*x:
#                         cnttab +=0
#                     elif n!=i*x:
#                         cnttab -=1
#             if slojnost==3:
#                 for i in range(sl3,sl3_1):
#                     for x in range(sl31_1+1,sl31_2):
#                         n = int(input("Введите ответ:" + str(i) + "*"+str(x) + " = "))
#                         cntschetzad+=1
#                     if n == i*x:
#                         cnttab +=0
#                     elif n!=i*x:
#                         cnttab -=1
#             if cnttab<0:
#                 print("Не твой уровень( твой счет - ",cnttab,"из",cntschetzad)
#             elif cnttab==1:
#                 print("Ты плох твой счет - ",cnttab,"из",cntschetzad)
#             elif cnttab>1:
#                 print("Не плохо твой счет - ",cnttab,"из",cntschetzad)
#             vib = int(input("для продолжения нажмите любую цифру иначе 1 для отмены: "))
#             if vib==1:
#                 print("Удачи!")
#                 break
#             else:
#                 print("loading......")

    #Нарисовать ромб
    # elif zad==4:
    #     for i in range(10):
    #         print(" "* (10-i), "+" * (2*i +1))
    #     for i in range(10 - 2, -1, -1):
    #         print(" " * (10 - i), "+" * (2*i +1))

    # else:
    #     print("Такой задачи нет....")
    # qw = input("Желаете продолжить да / иначе любой символ: ")
    # if qw=="да":
    #     print("Продолжаем.....")
    # else:
    #     print("удачи!")

#строки практика

# Задание 1
# Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите 
# на экран
# def flip():
#     print(input("Введите строку а програма выведет ее наоборот: ")[::-1])
# flip()

# # Задание 2
# # Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба 
# # количества на экран.
# w = input("Введите строрку а програм а выведет кол во букв символов")
# cntbuk = 0
# cntcifr = 0
# for i in w:
#     if i.isalpha():
#         cntcifr+=1
#     elif i.isdigit():
#         cntbuk+=1
# print("Кол- во цифр - ", cntcifr)
# print("Кол- во букв - ",cntbuk)

# #     Задание 3
# # Пользователь вводит с клавиатуры строку и символ 
# # для поиска. Посчитайте сколько раз в строке встречается 
# # искомый символ. Полученное число выведите на экран.
# z = input("Введите строку: ")
# s = input("Cимвол для поиска: ")
# print(z.find(s))


# #Задание 4
# # Пользователь вводит с клавиатуры строку и слово 
# # для поиска. Посчитайте сколько раз в строке встречается 
# # искомое слово. Полученное число выведите на экран.
# p = input("Введите строку: ")
# o = input("Cлово для поиска: ")
# cnt = 0
# if p == o:
#     cnt+=1
# else:
#     print("Слова нет!")



# Задание 5
# Пользователь вводит с клавиатуры строку, слово для 
# поиска, слово для замены. Произведите в строке замену 
# одного слова на другое. Полученную строку отобразите 
# на экране

# y = input("Введите строку: ")
# f = input("Поиск:")
# s = input("слово для замены:")

# strq= ''
# find1 = y.find(f)
# if find1 != -1:
#     strq +=y[:find1] +s +y[find1+len(f):]
# print(strq)  

# list1 = input("Введите список: ").split()
# num = input("Введите число, а программа выведет сколько раз данное число присутствуетв списке: ")
# print(list1.count(num))



# import math

# #1

# list1 = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
# list2 = []
# sum1 = 0
# sum2 = 0
# sum3 = 0
# sum4 = 0
# #1
# for i in list1:
#     if i<0:
#         sum1+=i
# #2
#     if i%2==0:
#         sum2+=i
# #3
#     if i%2==1:
#         sum3+=i
# #4
# print(f'Сумма отрицательных чисел - {sum1}')
# print(f'Сумма четных чисел - {sum2}')
# print(f'Суммане четных чисел - {sum3}')
# for x in range(len(list1)):
#     if x%3==0:
#         print(math.prod(x))

        


# #5
# print("Сумма максимальных и минимальных элементов в списке")
# print(max(list1)*min(list1))

# #6
# print("Сумма элементов находящиеся между первым и последним положительных элементов")

# for a in range(len(list1)):
#     if a>0 and a<max(list1):
#         list2.append(a)
# print(sum(list2))




# #2
# qrr = [i*i for i in range(14)]
# list3 = []
# list4 = []
# list5 = []
# list6 = []

# #1
# for q in qrr:
#     if q%2==0:
#         list3.append(q)
#     if q%2==1:
#         list4.append(q)
#     if q<0:
#         list5.append(q)

#     if q>=0:
#         list6.append(q)

# print(f'Четные{list3},не четные{list4},отрицательные{list5},положительные{list6}')


# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/
# try:
#     n = input("Введите ваше выражение: ")
#     print(eval(n))
# except SyntaxError:
#     print("Вы ввели не правельный знак! введите знак по типу * / + -")

# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.


# list1 = [i*i for i in range(25)]
# cnt = 0
# cnt1 = 0
# cnt2 = 0

# for cheklist in list1:
#     if cheklist<0:
#         cnt+=1
#     if cheklist>0:
#         cnt1+=1
#     if cheklist==0:
#         cnt2+=1

# print(f'Отрицательные элементы - {cnt}\nПоложительные - {cnt1}\nНулевые - {cnt2}')
# print(f'Максимальный элемент - {max(list1)}\nМинимальный элемент - {min(list1)}')











