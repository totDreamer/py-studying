import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [y**3 for y in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=2)

ax.set_xlabel('Cube Numbers', fontsize=10)
ax.set_ylabel('Value', fontsize=10)
ax.set_title('Cubes', fontsize=14)

ax.axis([1, 5, 1, 125])

plt.show()