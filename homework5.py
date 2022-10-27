# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# f = input('Введите текст: ')
# search = 'абв'
# lst = []
# for i in f.split():
#     if search not in i:
#         lst.append(i)
# print(f'Результат: {" ".join(lst)}')

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# count = 0
# sum = int(input('введите начальное количество конфет: '))
# print('ход игрока1')
# while 0<sum :
#     num=int(input('введите количество конфет от 1 до 28, которое хотите забрать: '))
#     if 0<num<29:
#         if sum<num:
#             print('введено число меньше, чем осталось конфет')
#         else:
#             if count%2==0:
#                 sum=sum-num
#                 count+=1
#                 print('игрок1 забрал конфеты в количестве', num, 'шт, осталось', sum, 'шт')
#                 if sum==0:
#                     print('game over. игрок1 победил')
#                     break
#                 else:
#                     print('ход игрока2')           
#             else:
#                 sum=sum-num                
#                 count+=1
#                 print('игрок2 забрал конфеты в количестве', num, 'шт, осталось', sum, 'шт')
#                 if sum ==0:
#                     print('game over. игрок2 победил')
#                     break
#                 else:
#                     print('ход игрока1')
#     else:
#         print("неверно введено количество ")




# Создайте программу для игры в ""Крестики-нолики"".

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]                # ооочень коряво, но оно работает, не верила, что смогу
# print('Правила игры: первым ходит игрок1, на обозначенную позицию ставится Х. Затем ход переходит к игроку2, на обозначенную позицию ставится О. Далее по очереди. Игра длится, пока три Х или три О не выстроятся в линию, либо не закончатся ходы')
# print('|', arr[0],'|',arr[1],'|',arr[2],'|')
# print('|', arr[3],'|',arr[4],'|',arr[5],'|')
# print('|', arr[6],'|',arr[7],'|',arr[8],'|')
# count = 0
# while count<9 or not arr[0]==arr[1]==arr[2] or arr[3]==arr[4]==arr[5] or arr[6]==arr[7]==arr[8] or arr[0]==arr[3]==arr[6] or arr[1]==arr[4]==arr[7] or arr[2]==arr[5]==arr[8] or arr[0]==arr[4]==arr[8] or arr[6]==arr[4]==arr[2]:
#     num=int(input('введите номер ячейки, в которую хотите поместить знак: '))
#     if num<0 or num>9:
#         print("неверно введен номер ячейки")
#         num=int(input('введите номер ячейки, в которую хотите поместить знак: '))
#     elif 0<num<10:
#         if arr[num-1]=='x' or arr[num-1]=='o':
#             print("ячейка занята, выберите другую ")
#         else:
#             if count%2==0:
#                 arr[num-1]='x'
#                 count+=1
#                 print('|', arr[0],'|',arr[1],'|',arr[2],'|')
#                 print('|', arr[3],'|',arr[4],'|',arr[5],'|')
#                 print('|', arr[6],'|',arr[7],'|',arr[8],'|')
#                 if arr[0]==arr[1]==arr[2] or arr[3]==arr[4]==arr[5] or arr[6]==arr[7]==arr[8] or arr[0]==arr[3]==arr[6] or arr[1]==arr[4]==arr[7] or arr[2]==arr[5]==arr[8] or arr[0]==arr[4]==arr[8] or arr[6]==arr[4]==arr[2]:
#                     print('game over. игрок1 победил')
#                     break
#                 else:
#                     print('ход игрока2 (o)')
            
#             else:
#                 arr[num-1]='o'
#                 count+=1
#                 print('|', arr[0],'|',arr[1],'|',arr[2],'|')
#                 print('|', arr[3],'|',arr[4],'|',arr[5],'|')
#                 print('|', arr[6],'|',arr[7],'|',arr[8],'|')
#                 if arr[0]==arr[1]==arr[2] or arr[3]==arr[4]==arr[5] or arr[6]==arr[7]==arr[8] or arr[0]==arr[3]==arr[6] or arr[1]==arr[4]==arr[7] or arr[2]==arr[5]==arr[8] or arr[0]==arr[4]==arr[8] or arr[6]==arr[4]==arr[2]:
#                     print('game over. игрок2 победил')
#                     break
#                 else:
#                     print('ход игрока1 (x)')
#     else:
#         print('game over. ничья')


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# f = open('file.txt', 'r') 
# data1 = f.read()
# f.close() 

# count = 1
# encoding = ''

# for i in range(len(data1)):
#     if (i+1)==len(data1):
#         encoding += str(count) + data1[i]
#     elif data1[i]==data1[i+1]:
#         count+=1
#         i+=1
#     else:
#         encoding += str(count) + data1[i]
#         count = 1
#         i+=1
# f = open('dz.txt', 'w')
# f.write(encoding)
# print(encoding)
# f.close()


# решение задачи с конфетами с ботом
# import random
# count = 0
# sum = int(input('введите начальное количество конфет: '))
# print('ход игрока')
# num=int(input('введите количество конфет от 1 до 28, которое хотите забрать: '))

# while 0<sum :
#     if count%2==0:
#         sum=sum-num
#         count+=1
#         print('игрок забрал конфеты в количестве', num, 'шт, осталось', sum, 'шт')
#         if sum==0:
#             print('game over. игрок победил')
#             break
#         else:
#             print('ход бота')
#     else:
#         num = random.randint(1, 29)
#         if num>sum:
#             num=sum
#         else:
#             sum=sum-num                
#             count+=1
#             print('бот забрал конфеты в количестве', num, 'шт, осталось', sum, 'шт')
#             if sum ==0:
#                 print('game over. бот победил')
#                 break
#             else:
#                 print('ход игрока')
#                 num=int(input('введите количество конфет от 1 до 28, которое хотите забрать: '))
#     if 0<num<29:
#         if sum<num:
#             print('введено число меньше, чем осталось конфет')
#             num=int(input('введите количество конфет от 1 до 28, которое хотите забрать: '))
#     else:
#         print("неверно введено количество ")
#         num=int(input('введите количество конфет от 1 до 28, которое хотите забрать: '))

