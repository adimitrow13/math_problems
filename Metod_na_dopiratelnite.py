import numpy as np
import matplotlib.pyplot as plt

# 1) Дефинираме новата функция и нейната производна
def f(x):
    return np.sin(x) - np.exp(-x) #np.sin(x);np.cos(X); e^-x = np.exp(-x)

def df(x):
    return np.cos(x) + np.exp(-x)

# 2) Функция за автоматичен избор на x0 по интервала [a,b]
def find_initial_guess(f, a, b, steps=1000):
    xs = np.linspace(a, b, steps)
    fs = f(xs)
    for i in range(len(xs)-1):
        if fs[i] * fs[i+1] < 0:
            return 0.5 * (xs[i] + xs[i+1])
    return 0.5 * (a + b)

# 3) Newton–Raphson с производна
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            raise ZeroDivisionError("Производната почти е нула.")
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    raise RuntimeError("Не се сближи в рамките на зададения брой итерации.")

# 4) Задаваме интервала и намираме x0
a, b = 6, 7  # Променен интервал на [0, 1]
x0 = find_initial_guess(f, a, b)
print(f"Автоматично избрано x0 = {x0:.3f}")

# 5) Стартираме Newton–Raphson
root, iters = newton_raphson(f, df, x0)
print(f"Приблизителен корен: {root:.3f} (итерации: {iters})")

# 6) Графика с маркиран корен
x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label=r'$f(x)=\sin x - e^{-x}$')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f'Корен ≈ {root:.3f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton–Raphson за $f(x)=\sin x - e^{-x}$')
plt.legend()
plt.grid(True)
plt.show()
