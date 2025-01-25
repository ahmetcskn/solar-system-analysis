import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('solar_system_orbits.csv')

def gradiant_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].Distance_from_Sun_AU
        y = points.iloc[i].Orbital_Period_Days

        m_gradient += -(2/n) * x * (y-(m_now * x + b_now))
        b_gradient += -(2 / n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m,b

m = 0
b = 0
L = 0.0001
epochs = 500

for i in range(epochs):
    m, b = gradiant_descent(m, b, data, L)

print(m, b)

x_min = data.Distance_from_Sun_AU.min()
x_max = data.Distance_from_Sun_AU.max()
x_range = [x for x in range(int(x_min), int(x_max) + 1)]

plt.scatter(data.Distance_from_Sun_AU, data.Orbital_Period_Days, color="black")
plt.plot(list(x_range), [m * x + b for x in x_range], color="red")
plt.show()
