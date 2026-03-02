import math

def f(x):
    return -2 * x * math.exp(-x) + math.exp(-2 * x) + x**2

def df(x):
    return -2 * math.exp(-x) + 2 * x * math.exp(-x) - 2 * math.exp(-2 * x) + 2 * x

# Alglähend
x = 0.0

# Newtoni meetod
while True:
    x_new = x - f(x) / df(x)
    
    # Lõpetamistingimus: |x_n - x_{n-1}| <= 10^-5
    if abs(x_new - x) <= 1e-5:
        break
        
    x = x_new

print(f"Lahendiks on: {x_new}")