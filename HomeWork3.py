#Задача 1
import numpy as np
from math import factorial
arr=np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
arr
def mean_value(array):
    return sum(array)/len(array)
print(f'Среднее арифметическое для данной выборки М(Х) = {mean_value(arr): .2f}')

def mean_square_deviation(array):
    square_dev=(array-mean_value(array))**2
    return (sum(square_dev)/len(square_dev))**(1/2)

print(f'Среднее квадратичное отклонение для данной выборки SD = {mean_square_deviation(arr): .4f}')
def dispers(array, no_off=False):


    square_dev=(array-mean_value(array))**2
    return sum(square_dev)/(len(square_dev)-1) if no_off else sum(square_dev)/len(square_dev)
print(f'Смещенная оценка дисперсии для данной выборки D = {dispers(arr): .4f}\n'
      f'Немещенная оценка дисперсии для данной выборки D = {dispers(arr, True): .4f}'
     )

# Задача2
def combinations(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))
P1=(combinations(3,2)/combinations(8,2))*(combinations(5,3)*combinations(7,1)/combinations(12,4))
print(f'Вероятность события "из первой корзины не вытащили ни одного белого мяча'
      f', из второй вытащили 3 белых мяча"\nP(A1) = {P1: .4f}'
     )
P2=(combinations(5,1)*combinations(3,1)*combinations(5,2)*combinations(7,2))/(combinations(8,2)*combinations(12,4))
print(f'Вероятность события "из первой корзины вытащили 1 белый мяч'
      f', из второй вытащили 2 белых мяча"\nP(A2) = {P2: .4f}')
P3=(combinations(5,2)*combinations(5,1)*combinations(7,3))/(combinations(8,2)*combinations(12,4))
print(f'Вероятность события "из первой корзины вытащили 2 белых мяча'
      f', из второй вытащили 1 белый мяч"\nP(A2) = {P3: .4f}'
     )    

print(f'Вероятность того, что из вытащенных мячей 3 белые Р(А) = {P1+P2+P3: .4f}')    
# Задача 3
PB=1/3
PA=PB*0.9+PB*0.8+PB*0.6
print(f'Полная вероятность наступления события А Р(А) = {PA: .4f}')
PAB1=PB*0.9/PA
PAB2=PB*0.8/PA
PAB3=PB*0.6/PA
print(f'Вероятность того, что выстрел произвёл первый спортсмен: {PAB1: .4f};\n'
      f'Вероятность того, что выстрел произвёл второй спортсмен: {PAB2: .4f};\n'
      f'Вероятность того, что выстрел произвёл третий спортсмен: {PAB3: .4f}.'
     )
# Задача 4
PD=0.25*0.8+0.25*0.7+0.5*0.9
print(f'Полная вероятность наступления события D, P(D) = {PD}.') 
PDSA=0.25*0.8/PD
PDSB=0.25*0.7/PD
PDSC=0.5*0.9/PD
print(f'Вероятность того, что студент учится на факультете А: {PDSA: .4f};\n'
      f'Вероятность того, что студент учится на факультете B: {PDSB: .4f};\n'
      f'Вероятность того, что студент учится на факультете C: {PDSC: .4f}.'
      )
# Задача 5
P3=0.1*0.2*0.25
print(f'Вероятность того, что из строя выйдут все детали Р(3) = {P3: .4f}')
P2=0.1*0.2*0.75+0.1*0.25*0.8+0.2*0.25*0.9
print(f'Вероятность того, что из строя выйдут только 2 детали Р(2) = {P2: .4f}')
P0=0.9*0.8*0.75
print(f'Вероятность того, что из строя не выйдет ни одной детали Р(0) = {P0: .4f}')
P_0=1-P0
print(f'Вероятность того, что выйдет из строя хотя бы одна деталь Р(>=1) = {P_0: .4f}')
P1=0.1*0.8*0.75+0.2*0.9*0.75+0.25*0.9*0.8
print(f'Вероятность того, что выйдет из строя одна деталь Р(1) = {P1: .4f}')
    
