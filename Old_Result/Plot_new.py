import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text



sizes=[2000]

file_path = 'Result_2000.xlsx'

res_2000 = pd.read_excel(file_path, sheet_name='2000', usecols='B:D')


name_func=["Дерево отрезков","Дерево Фенвика", "Декартово дерево"]

table=[]
for i in range(0,len(res_2000),7):
    table.append(res_2000[i:i+7])
print(table[90])
print(table[990])
print(table[-1])


for_plot=[]
for j in range(0,len(res_2000),7):
    for_plot.append(list(res_2000.iloc[j+3]))


data = list(zip(*for_plot))

# Генерируем шаги (x-координаты)
steps = range(10,len(data[0])+10)

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

#yticks = range(0, 4400, 200)  инициализация
#plt.yticks(yticks)

#yticks = range(0, 10, 1)
#plt.yticks(yticks)

# Отображаем график
plt.show()






