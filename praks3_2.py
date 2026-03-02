import math

def f(x):
    return (4*x -7)/(x-2)

def df(x):
    return -(1/((x-2)**2))

# Alglähend
x = 0.5

# Newtoni meetod
while True:
    x_new = x - f(x) / df(x)
    
    # Lõpetamistingimus: |x_n - x_{n-1}| <= 10^-5
    if abs(x_new - x) <= 1e-5:
        break
        
    x = x_new

print(f"Lahendiks on: {x_new}")