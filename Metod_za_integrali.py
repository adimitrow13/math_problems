import numpy as np

def f(x):
    return (1/np.sqrt(2*np.pi) * np.exp(-x**2)/2)        #np.exp(2 * x) * np.cos(3 * x) (e^2x * cos3x) самия интеграл
#np.sqrt(), np.exp()= e^x , np.pi()

def simpson(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = y[0] + y[-1] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2])
    return h * S / 3

# Начални стойности
a, b = -3,3 #границите на интеграла
n = 2
eps = 1e-5 # <--  10^(-x)

S_n = simpson(a, b, n)
S_2n = simpson(a, b, 2 * n)

while abs(S_2n - S_n) > eps / 15:
    n *= 2
    S_n = S_2n
    S_2n = simpson(a, b, 2 * n)

print(f"Приближението на интеграла е: {S_2n:.5f}, при n = {2 * n}")
