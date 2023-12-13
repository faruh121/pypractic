
#ФОРМАТИРОВАНИЕ СТРОК

# a = "ПРИвет миР"
# #не нормально
# print("Строка - ",a)
# #Нормально делает
# print("a.capitalize()",a.capitalize())
# #переводит буквы в нижниий регистр
# print("a.lower()",a.lower())
# #переводит буквы в верхний регистр
# print("a.upper()",a.upper())
# #переводит в регистр первые буквы в верхний регистр
# print("a.title()",a.title())
# #переводит  регистр c верхнего на нижний
# print("a.swapcase()",a.swapcase())
# #методы поиска подстроик в строке
# print("a.count(И)",a.count("И"))
# #индекс первого вхождения + если добавить r то будет искать с конца
# print("a.find('И')",a.find('И'))
# #Разница между find в том , что если элемента в слове нет то индекс выводит ошибку а  find нет + если добавить r то будет искать с конца
# print("a.index('И')",a.index('И'))

# #Метода проверки строк
# #Проверяет на пробелы
# print("a.isalnum()",a.isalnum())
# #проверяет состоит ли из букв
# print("a.isalpha()",a.isalpha())
# #Cостоит ли в строке число
# print("a.isdigit()",a.isdigit())
# #Проверяет находится ли ВСЕ числа в нижнем регистре
# print("a.islower()",a.islower())
# #есть ли пробельные симвыолы \n \t
# print("a.isspace()",a.isspace())
# #Проверяет находится ли ВСЕ числа в верхнем регистре
# print("a.upper()",a.upper())

# #метооды формата строк
# print("a.center(12px)",a.center(12))    #текст по центру также можно сделать символ заполнения a.center(12px,"*") так
# print('a.expandtabs()',a.expandtabs()) #возвращает копию строки, в которой символы табуляции т.е.. «\t» расширены с использованием пробела, необязательно с использованием данного tabsize ( по умолчанию 8)
# print("a.ljust()",a.ljust())#по левому краю строку выровнять
# print("a.rjust()",a.rjust())#по правому краю строку выровнять
# print("a.lstrip()",a.lstrip())#удалаяет символы если указать c лева
# print("a.rstrip()",a.rstrip())#удалаяет символы если указать с права

# #cрезы строк 
# stri = "abcdef"
# print("Строка - ",stri)
# print("stri[2:5]",stri[2:5]) # вырезает в диапозоне от 2:5 или подругому если срез начинает [:3]то выводит с конца и так же наоборот так же если написать [:] то выведет копию строки
# print("stri[2:5]",stri[2:5:2]) # тут я добавил шаг то есть будет вывдоить каждый второй если будет [::2]
# #чтобы перебрать по символам любой итерируемый объект нужно
# for char in stri:
#     print(char)

#ЛИСТЫ


# append(element): Добавляет элемент в конец списка.

# extend(iterable): Расширяет список, добавляя элементы из другого итерируемого объекта, такого как другой список.

# insert(index, element): Вставляет элемент в указанную позицию списка.

# remove(element): Удаляет первое вхождение элемента из списка.

# pop(index): Удаляет и возвращает элемент по указанному индексу. Если индекс не указан, удаляется и возвращается последний элемент.

# index(element): Возвращает индекс первого вхождения элемента в списке.

# count(element): Возвращает количество вхождений элемента в списке.

# sort(): Сортирует список в порядке возрастания.

# reverse(): Изменяет порядок элементов списка на обратный.

# copy(): Создает копию списка.



# n = "Привет как дела"
# nl = list(n) #преобразование строки в список
# print(nl)

# nl[0]="Пока" #замена элемента в списке

# print(n.split()) #из списка в строку

# print(n.join())#наоброт



#генератор списка
# list1 = [expresion for item in sequance]



# list1 = [i*i for i in range(6)]
# print(list1)



# list2 = [i+'*'for i in'example'] #прибавляет каждой букву звездочку
# print(list2)

# list3 = [i*5 for i in'abcdf']  #каждый эелемент 5 раз 
# print(list3)

# #list = [exp for i in seq if cond]

# import random
# list4 = [random.randint(1,10)for _ in range(random.randint(5,10))]#рандомные числа в списке
# print(list4)


# list5 = [i*i for i in range(1,11) if i %2==0]

# print(list5)

# cust = ['Bob','Anna','Bob','Joe','Nicki']
# list6 = [i for i in cust if i!='Bob' and i!='Joe']
# print(list6)

# new_list = []
# for i in cust:
#     if i!='Bob' and i!='Joe':
#         new_list.append(i.upper())
# print(new_list)


# list7 = [x*y for x in range(1,4 )for y in range(1,4)]
# print(list7)

# new_list1 = []
# for y in range(1,4):
#     for x in range(1,4):
#         new_list1.append(x*y)
# print(new_list1)

# #Срезы списков


# list1 = ['user',12,200.34,False,True]
# print(list1[1:3])

# for i in range(24):
#     for x in range(60):
#         for s in range(60):
#             print(f'{i} : {x} : {s}')
#             import time 
#             time.sleep(1)

# list8 = [[x*y for x in range(1,4)for y in range(1,4)]]
# print(list8)


# import random
# el = 'Hello123233rere'
# passw = ''
# for i in range(random.randint(10,15)):
#     passw +=random.choice(el)
# print(passw)
    



#Функции