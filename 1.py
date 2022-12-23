
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#Предыдущее решение:
#print ('Задача 1')
#from random import randint
#list = []
#i = 1
#n = int(input('Введите количество элементов в списке: '))
#for i in range(n):
#    list.append(randint(1,9))
#    i += 1
#print(f'Ваш список из {n} элементов: {list}')
#j=1
#sum=0
#while j < len(list):
#    sum=sum+list[j]
#    j+=2
#print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum}')

#Новое решение:
print ('Пример 1')
from random import randint as rand
n = int(input('Введите количество элементов в списке: '))
my_list = [rand(0, 9) for i in range(n)]
print(f'Ваш список из {n} элементов: {my_list}')
naNechetPoz = list(num for i, num in enumerate(my_list) if i % 2)
print(f'На нечетных позициях элементы: {naNechetPoz} Сумма элементов списка, стоящих на нечётной позиции: {sum(naNechetPoz)}')


#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

#Предыдущее решение:
#print ('Задача 2')
#from random import randint
#list1 = []
#i = 1
#n = int(input('Введите количество элементов в списке: '))
#for i in range(n):
#    list1.append(randint(1,9))
#    i += 1
#print(f'Ваш список из {n} элементов: {list1}')
#count=0
#j=1
#if n%2==0:
#    while count<len(list1)//2:
#        m=list1[count]*list1[len(list1)-j]
#        print(m)
#        count+=1
#        j+=1
#    else:
#        while count<len(list1)//2:
#            m=list1[count]*list1[len(list1)-j]
#            print('Произведения пар чисел списка:')
#            print(m)
#            print(list1[len(list1)//2]**2)
#            count+=1
#            j+=1

#Новое решение:
print ('Пример 2')
import random
n1 = int(input('Введите количество элементов в списке: '))
my_list2 = [random.randint(0, 9) for i in range(n1)]
print(f'Ваш список из {n1} элементов: {my_list2}')

pair_list2 = [my_list2[i] * my_list2[-i - 1] for i in range(int(n1 / 2))]
print(pair_list2)

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#Предыдущее решение:
#print ('Задача 3')
#list2 = [18.6, 19.8, 6.5, 63.1, 4.9]
#print(f'Ваш список: {list2}')
#def dif(list2):
#    dif_max_min = []
#    for i in range(len(list2)):
#        dif_max_min.append(list2[i] % 1)
#    return max(dif_max_min) - min(dif_max_min)
#print('Разница между максимальным и минимальным значением дробной части элементов: ', round(dif(list2), 2))


#Новое решение:
print ('Пример 3')
import random
n3 = int(input('Введите количество элементов в списке: '))
my_list3 = [random.uniform(0, 9) for i in range(n1)]
print(f'Ваш список: {my_list3}')
diff_max_min_list = list(i % 1 for i in my_list3 if i % 1 != 0)
diff_max_min_list = list(round(i, 2) for i in diff_max_min_list)
print('Разница между максимальным и минимальным значением дробной части элементов: ', max(diff_max_min_list) - min(diff_max_min_list))