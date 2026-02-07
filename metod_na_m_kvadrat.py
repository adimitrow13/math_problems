import numpy as np
import matplotlib.pyplot as plt

# Дадените стойности
x = np.array([-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0])
y = np.array([0.832, 0.106, -0.458, -0.430, 0.000, 0.458, 0.430, 0.106, 0.832])

# Строим матрица с [1, x, x^2, x^3]
degree = 3  # <-- промени n на желаната степен
A = np.vstack([x**i for i in range(degree + 1)]).T  #СМЕНЯНЕ НА СТЕПЕНТА

# Решаваме системата чрез най-малки квадрати
coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)

# Извеждаме полинома
print(f"Апроксимационен полином: P(x) = {coeffs[0]:.4f} + {coeffs[1]:.4f}x + {coeffs[2]:.4f}x² + {coeffs[3]:.4f}x³")

# Графика
x_vals = np.linspace(-2.1, 2.1, 400)
y_vals = coeffs[0] + coeffs[1]*x_vals + coeffs[2]*x_vals**2 + coeffs[3]*x_vals**3

plt.plot(x_vals, y_vals, label='Полином (степен 3)', color='blue')
plt.scatter(x, y, color='red', label='Дадени точки')
plt.title("Аппроксимация чрез метод на най-малките квадрати (степен 3)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
