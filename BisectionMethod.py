import matplotlib
matplotlib.use('Qt5Agg')

import numpy as np
from matplotlib import pyplot as plt

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Функцията трябва да е различна от a и b")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2  #средна точка
        if f(c) == 0:  #точно решение
            return c, iter_count
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2, iter_count



#Дефиниране на функцията
def f(x):
    return x ** 9 - x ** 7 + 2*x **2 - 1

#Автоматично намиране на корен
#def find_root_interval(f , start=-10, end=10, step=0.1):
    #Намира интервал [a,b],в който функцията f(x) сменя знак (и вероятно има корен)
    # f - целевата функция
    # start,end - граници за търсене
    # step - стъпка за проверка

    #x = start
    #while x < end:
        #if f(x) * f(x + step) <0:
            #return x, x+step
        #x += step
    #return None #ако не намерим интервал

#Решаване в интервала [а,б]
a, b = -5, 5
root, iterations = bisection_method(f, a, b)



#2
# interval = find_root_interval(f)
#if interval is not None:
    #a, b = interval
    #root, iterations = bisection_method(f, a, b)
#else:
    #print(" Не е намерен интервал със смяна на знак.")
    #exit()

print(f"Приблизителен корен: {root}")
print(f"Брой итерации: {iterations}")

#Графично представяне
x = np.linspace(-5, 5, 100)
y = f(x)

plt.plot(x, y, label='f(x) = x^3 - x^2 + 8*x + 12')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f'Корен = {root:.6f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

