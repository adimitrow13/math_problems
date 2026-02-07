import numpy as np
import matplotlib.pyplot as plt

# 1) Зададени точки от условието
x_points = np.array([6, 7, 8, 9, 10, 11, 13, 14], dtype=float)
y_points = np.array([-1.192, -0.996, -1.382, -1.053, 0.624, 0.549, 0.388, 0.844], dtype=float)

# 2) Функция за Лагранжова интерполация
def lagrange_interpolation(xp, yp, x):
    total = 0.0
    n = len(xp)
    for i in range(n):
        term = yp[i]
        for j in range(n):
            if j != i:
                term *= (x - xp[j]) / (xp[i] - xp[j])
        total += term
    return total

# 3) Интерполация за декември (x=12) и март (x=15)
x_dec, x_mar = 12.0, 15.0
y_dec = lagrange_interpolation(x_points, y_points, x_dec)
y_mar = lagrange_interpolation(x_points, y_points, x_mar)

print(f"Приблизителна стойност за декември (x=12): {y_dec:.6f}")
print(f"Приблизителна стойност за март     (x=15): {y_mar:.6f}")

# 4) Подготовка за графика
x_plot = np.linspace(6, 15, 400)
y_plot = [lagrange_interpolation(x_points, y_points, xi) for xi in x_plot]

# 5) Графика
plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, label='Лагранжов интерп. полином (степ.7)', color='blue')
plt.scatter(x_points, y_points, color='red', label='Дадени точки')
plt.scatter([x_dec, x_mar], [y_dec, y_mar], color='green', s=50, label='Декември & Март')
plt.axvline(x_dec, color='green', linestyle='--')
plt.axvline(x_mar, color='green', linestyle='--')
plt.title('Лагранжова интерполация за декември и март')
plt.xlabel('x (месец като число)')
plt.ylabel('Индекс на цените')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
