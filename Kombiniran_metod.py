import numpy as np
import matplotlib.pyplot as plt

# Примерна функция
def f(x):
    return np.sin(x) - np.exp(-x)

# Производната на функцията
def df(x):
    return np.cos(x) + np.exp(-x)

# Намиране на интервал, където функцията сменя знак
#def find_sign_change_interval(f, start=-10, end=10, step=0.1):
    #x_vals = np.arange(start, end, step)
    #for i in range(len(x_vals) - 1):
        #if f(x_vals[i]) * f(x_vals[i + 1]) < 0:
            #return x_vals[i], x_vals[i + 1]
    #raise ValueError("Не е намерен интервал със смяна на знак във функцията.")

# Комбиниран метод: модифицирана версия на метод на хордата + Нютон

def combined_method(f, df, a, b, tol=1e-7, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Невалиден интервал: f(a) и f(b) трябва да са с различен знак.")

    for i in range(max_iter):
        # Стъпка на хордата
        c = b - (f(b) * (b - a)) / (f(b) - f(a))

        # Стъпка на Нютон
        if df(c) == 0:
            raise ZeroDivisionError("Производната е нула при c. Методът не може да продължи.")

        new_c = c - f(c) / df(c)

        if abs(f(new_c)) < tol:
            print(f"Итерации: {i+1}")
            return new_c

        # Обнови интервала
        if f(a) * f(new_c) < 0:
            b = new_c
        else:
            a = new_c

    print("Максимален брой итерации.")
    return new_c

# Интервал
a, b = 6, 7

# Автоматично намиране на интервал с промяна на знак
#try:
 #   a, b = find_sign_change_interval(f, 0, 2, 0.01)
  #  print(f"Автоматично намерен интервал: [{a}, {b}]")
#except ValueError as e:
 #   print("Няма намерен интервал.")

root = combined_method(f, df, a, b)
print(f"Приблизителен корен: {root:.3f}")

# Графично представяне
x = np.linspace(-1, 2, 400)
y = f(x)

plt.plot(x, y, label='f(x) = sin(x) - e^(-x)')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f'Корен ≈ {root:.3f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Комбиниран метод')
plt.legend()
plt.grid(True)
plt.show()
