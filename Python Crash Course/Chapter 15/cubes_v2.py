import matplotlib.pyplot as plt

x_values = list(range(5000))
y_values = [y**3 for y in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=1, c=y_values, cmap=plt.cm.Blues)

ax.set_xlabel('Cube Numbers', fontsize=10)
ax.set_ylabel('Value', fontsize=10)
ax.set_title('Cubes', fontsize=14)

ax.axis([1, 5000, 1, 5000**3])

plt.show()