import numpy as np
import matplotlib.pyplot as plt

# 1) Определяме възлите x
x = np.array([-0.4000, 0.600, 1.600, 2.600, 3.600, 4.600, 5.600, 6.600], dtype=float)

# 2) Изчисляваме стойностите за двете функции

# f(x) = пети корен от x (за отрицателни x ползваме знак) np.sign(x) * np.abs(x)**(1/5)
f_values = np.array([-0.1508, 0.0582, 1.1817, 2.0095, 2.6144, 3.08465, 3.4676, 3.7900], dtype=float) #y_values

# g(x) = 2^x — правим основата float, за да избегнем грешката
#g_values = 2.0 ** x

# 3) Функция за разделени разлики
def divided_diff(x, y):
    n = len(y)
    coef = y.copy().astype(float)
    # coef[i] ще стане f[x0...xi]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

# 4) Функция за полином на Нютон, оценен в xi
def newton_polynomial(x, coef, xi):
    n = len(coef)
    result = coef[-1]
    for k in range(n - 2, -1, -1):
        result = coef[k] + (xi - x[k]) * result
    return result

# 5) Изчисляваме коефициентите (разделените разлики)
f_coef = divided_diff(x, f_values)
#g_coef = divided_diff(x, g_values)

# 6) Апроксимация за x*
x_approx = 2.53
f_approx = newton_polynomial(x, f_coef, x_approx)
#g_approx = newton_polynomial(x, g_coef, x_approx)

print(f"Апроксимация на f(2.53): {f_approx:.6f}")
#print(f"Апроксимация на g(0.25) = 2^x: {g_approx:.6f}")

# 7) Визуализация на полиномите
x_plot = np.linspace(-2, 2, 200)
f_poly = [newton_polynomial(x, f_coef, xi) for xi in x_plot]
#g_poly = [newton_polynomial(x, g_coef, xi) for xi in x_plot]

plt.figure(figsize=(8, 5))
plt.plot(x_plot, f_poly, label="Newton полином за x*=2.53", linewidth=2)
#plt.plot(x_plot, g_poly, label="Newton полином за 2^x",  linewidth=2)
plt.scatter(x, f_values, color='red', label="Възли за x*=2.53")
#plt.scatter(x, g_values, color='green', label="Възли за 2^x")
plt.axvline(x_approx, color='black', linestyle='--', label=f'x = {x_approx}')
plt.title("Интерполация с полиноми на Нютон")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.grid(True)
plt.show()
