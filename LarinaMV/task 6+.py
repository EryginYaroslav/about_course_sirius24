# Сначала на вход поступает длина последовательности N. 
#Затем элементы последовательности – целые числа.
#Напишите программу, которая подсчитывает количество положительных чисел среди элементов последовательности.

N= input("Введите натуральное число N: ")
count = 0
for i in range(int(N)):
  i=int(input())
  if i > 0:
    count+=1
print ("Количество положительных элементов: ", count)