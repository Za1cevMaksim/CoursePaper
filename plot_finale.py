import pandas as pd
import matplotlib.pyplot as plt




file_path = 'Result_1000.xlsx'

table=[]
for i in range (10,1001):
    res_1000 = pd.read_excel(file_path, sheet_name=f'1000_{i}', usecols='B:D')
    if i==100 or i==500 or i==1000:
        print(res_1000)
    table.append(res_1000)




name_func=["Дерево отрезков","Дерево Фенвика", "Декартово дерево"]

for_plot_init=[]
for_plot_init_mem=[]
for_plot_sum=[]
for_plor_update=[]
for i in table:
    for_plot_init.append(list(i.iloc[0]))
    for_plot_init_mem.append(list(i.iloc[1]))
    for_plot_sum.append(list(i.iloc[2]))
    for_plor_update.append(list(i.iloc[3]))


data = list(zip(*for_plot_init))

# Генерируем шаги (x-координаты)
steps = range(10,len(data[0])+10)
plt.figure(figsize=(10, 6))
# Рисуем каждую функцию
for i, function_data in enumerate(data):
    plt.plot(steps, function_data, label=name_func[i])


# Настройка сетки
plt.grid(True)  # Включаем сетку


# Добавляем заголовок и метки осей
plt.title('График зависимости времени выполнения операции инициализации от размерности входного массива')
plt.xlabel('Размерность входного массива данных')
plt.ylabel('Время в миллисекундах')
plt.legend()

yticks = range(0, 1200, 100)
plt.yticks(yticks)


# Отображаем график
plt.show()


data = list(zip(*for_plot_init_mem))

plt.figure(figsize=(10, 6))
# Рисуем каждую функцию
for i, function_data in enumerate(data):
    plt.plot(steps, function_data, label=name_func[i])


# Настройка сетки
plt.grid(True)  # Включаем сетку
plt.minorticks_on()  # Включаем дополнительные деления (минорные тики)
plt.grid(which='both', linestyle='--', linewidth=0.5)  # Настраиваем сетку для основных и минорных делений

# Добавляем заголовок и метки осей
plt.title('График зависимости объема памяти на инициализацию от размерности входного массива')
plt.xlabel('Размерность входного массива данных')
plt.ylabel('Объем в Кб.')
plt.legend()

yticks = range(0, 1200, 100)
plt.yticks(yticks)

# Отображаем график
plt.show()

data = list(zip(*for_plot_sum))
plt.figure(figsize=(10, 6))
# Рисуем каждую функцию
for i, function_data in enumerate(data):
    plt.plot(steps, function_data, label=name_func[i])


# Настройка сетки
plt.grid(True)  # Включаем сетку
plt.minorticks_on()  # Включаем дополнительные деления (минорные тики)
plt.grid(which='both', linestyle='--', linewidth=0.5)  # Настраиваем сетку для основных и минорных делений

# Добавляем заголовок и метки осей
plt.title('График зависимости времени выполнения операции суммы на отрезке от размерности входного массива')
plt.xlabel('Размерность входного массива данных')
plt.ylabel('Время в миллисекундах')
plt.legend()


# Отображаем график
plt.show()



data = list(zip(*for_plor_update))
plt.figure(figsize=(10, 6))
# Рисуем каждую функцию
for i, function_data in enumerate(data):
    plt.plot(steps, function_data, label=name_func[i])


# Настройка сетки
plt.grid(True)  # Включаем сетку
plt.minorticks_on()  # Включаем дополнительные деления (минорные тики)
plt.grid(which='both', linestyle='--', linewidth=0.5)  # Настраиваем сетку для основных и минорных делений

# Добавляем заголовок и метки осей
plt.title('График зависимости времени на операцию обновления от размерности входного массива')
plt.xlabel('Размерность входного массива данных')
plt.ylabel('Время в миллисекундах')
plt.legend()


# Отображаем график
plt.show()