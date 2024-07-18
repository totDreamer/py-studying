import matplotlib.pyplot as plt

x_values = list(range(0, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=2, c=y_values, cmap=plt.cm.Blues)

# Назначение заголовка диаграммы и меток осей
ax.set_title('Square Numbers', fontsize=20)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Square of Value', fontsize=10)

# Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()