import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text



sizes=[100,500,1000]

file_path = 'Result_new.xlsx'

res_100 = pd.read_excel(file_path, sheet_name='100', usecols='B:D')
res_500 = pd.read_excel(file_path, sheet_name='500', usecols='B:D')
res_1000 = pd.read_excel(file_path, sheet_name='1000', usecols='B:D')
res_5000 = pd.read_excel(file_path, sheet_name='5000', usecols='B:D')
res_10000 = pd.read_excel(file_path, sheet_name='10000', usecols='B:D')


name_func=["Дерево отрезков","Дерево Фенвика", "Декартово дерево"]

for i in range(3,4):
    for_plot=[]
    for_plot.append(list(res_100.iloc[i]))
    for_plot.append(list(res_500.iloc[i]))
    for_plot.append(list(res_1000.iloc[i]))
    #for_plot.append(list(res_5000.iloc[i]))
    #for_plot.append(list(res_10000.iloc[i]))

    s_new = np.linspace(min(sizes), max(sizes), num=100)
    data_t = list(zip(*for_plot))

    plt.figure(figsize=(10, 6))

    # Рисуем каждую функцию
    for i, function_data in enumerate(data_t):
        plt.plot(sizes, function_data, marker='o', label=name_func[i])

    texts = []
    for i, function_data in enumerate(data_t):
        for j, value in enumerate(function_data):
            formatted_value = f'{value:.6f}'
            texts.append(plt.text(sizes[j], function_data[j], formatted_value, ha='center', va='bottom'))

    # Корректируем размещение меток
    adjust_text(texts, arrowprops=dict(arrowstyle='->'))

    # Настройка сетки
    plt.grid(True)  # Включаем сетку
    plt.minorticks_on()  # Включаем дополнительные деления (минорные тики)
    plt.grid(which='both', linestyle='--', linewidth=0.5)  # Настраиваем сетку для основных и минорных делений


    # Добавляем заголовок и метки осей
    plt.title('Время на операцию суммы на отрезке')
    plt.xlabel('Размерность изначального массива данных')
    plt.ylabel('Время в секундах')
    plt.legend()

    # Отображаем график
    plt.show()