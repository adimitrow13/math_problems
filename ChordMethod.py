import numpy as np
import matplotlib.pyplot as plt


def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    #Решаване на f(x) = 0 чрез метода на хордите (regula falsi)
    # f-Функцията
    # a, b - начални граници (трябва да ограждат корен)
    #tol - толеранс за спиране
    #max_iter - макс брой итерации
    fa, fb = f(a), f(b)

    #Проверка дали някой от краищата е корен
    if fa == 0:
        return a, 0, [a]
    if fb == 0:
        return b, 0, [b]
    #Проверка дали интервалът съдържа корен
    if fa * fb > 0:
        raise ValueError("Функцията трябва да има различни знаци в точките a и b")

    iter_count = 0
    c_old = a #начална стойност за предишно изчислено c
    c_values = []

    while iter_count < max_iter:
        c = b - (fb *(b - a))/(fb - fa) #Формула на метода на хордите
        fc = f(c)
        c_values.append(c)

        #Проверка дали с e точен корен
        if fc == 0 or abs(c-c_old) < tol:
            return c, iter_count, c_values

        #Поддържане на интервам с различни знаци
        if fc * fa < 0:
            b, fb =c, fc #заместваме b c c
        else:
            a, fa = c, fc #заместваме а c c

        c_old = c
        iter_count += 1

    return c, iter_count, c_values

#Графично представяне на функцията:
def plot_position(f, a, b, c_values, root, zoom=0):
    x=np.linspace(a - zoom,b + zoom,100) #Генериране на х стойности за графиката
    y = f(x)
    plt.plot(x, y, label='f(x)', color ='blue') #Графика на функцията
    plt.axhline(0, color='black', linestyle='--') #Оста OX
    plt.axvline(root,color='red', linestyle='--',label=f'Корен ~ {root:.6f}') #Вертикална линия при корена



    #Изобразяване на всички стъпки по метода
    for i in range(len(c_values) -1):
        c = c_values[i] #Текущо приближение p_i
        fc = f(c)

        #Поставяне на точка за текущата стъпка c
        plt.scatter(c, fc, color='blue', marker='o', label='Стъпка c' if i == 0 else"")

        #Вертикална линия от f(c) до оста OX
        plt.plot([c, c], [0, fc], color='gray', linestyle='--')

        #Лъч (хордата) между f(p_i) и f(b)
        plt.plot([c, b], [fc, f(b)], color='orange',linestyle='--' )

        #Обновяване на границите според метода на хордите
        if f(c) * f(a) < 0:
            b = c #Коренът е в [a, c]
        else:
            a = c #Коренът е в [c, b]

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()

#Изчисляване на абсолютна и относителна грешка
def absolute_error(true_value, approx_value):
    return abs(true_value - approx_value)
def relative_error(true_value, approx_value):
    return abs(true_value -approx_value) / abs(true_value) if true_value != 0 else float('inf')

def f1(x):
    return x ** 3 - x - 2

a, b = 1, 2
root, iterations, c_values = regula_falsi(f1, a, b)
plot_position(f1, a, b, c_values, root)

print(f"Приблизителен корен: {root}")
print(f"Брой итерации: {iterations}")

