import numpy as np
import matplotlib.pyplot as plt

def polynomial_least_squares(x, y, degree):
     # Намира коефициентите на полином от дадена степен чрез метода на най-малките квадрати
     # Параметри:
     # x - numpy масив с входни данни (независима променлива)
     # y - numpy масив със зависими данни (зависима променлива)
     # degree - степен на полинома
     # Връща  масив с коефициентите на полинома(от най-високата до най-ниската степен)

     X = np.vander(x, degree +1)
     coeffs = np.linalg.lstsq(X, y,rcond=None)[0]

     return coeffs


#Примерна задача:
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 2.8, 3.6, 4.5, 5.1])

#Тествай с различни степени
degrees = [0, 1, 2, 3] #0-константа, 1-линейна, 2-квадратична ...

for d in degrees:
    coeffs = polynomial_least_squares(x, y, d)
    print(coeffs)



#Изчисляваме апроксимацията за х точките
y_fit = np.polyval(coeffs, x)

#Грешки
absolute_error = abs(y - y_fit)
relative_error = abs((y - y_fit)/ y) * 100 #за нормализация (връща резултат между 0 и 1)

mae = np.mean(absolute_error) #Средна абсолютна грешка
mre = np.mean(relative_error) #Средна относителна грешка

print(f"Абсолютни грешки: {absolute_error}")
print(f"Относителни грешки: {relative_error}\n")

print(f"Средна абсолютна грешка(MAE): {mae:.4f}")
print(f"Средна относителна грешка(MRE): {mre:.2f}%")

#Графично представяне за различни степени
x_fit = np.linspace(min(x), max(x), 100) #За гладка крива,която свързва данните
for d in degrees:
    coeffs = polynomial_least_squares(x, y, d)
    y_fit = np.polyval(coeffs, x_fit)
    plt.plot(x_fit, y_fit, label=f"Степен:{d}")

plt.legend()
plt.show()

