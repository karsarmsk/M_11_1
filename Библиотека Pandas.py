# import pandas as pd # Импортируем библиотеку Pandas.
#
# series_example = pd.Series([4, 7, -5, 3]) # Создаём объект Series, содержащий числа.
#
# print(series_example) # Выводим объект на экран.

import pandas as pd # Импортируем библиотеку Pandas.
# Создаем таблицу
# family = {'Семья': ['Папа', 'Мама', 'Сын', 'Дочь'],
#           'Имя' : ['Сергей', 'Светлана', 'Александр', 'Ольга'],
#         'Год рождения': [1963, 1966, 1986, 1988],
#         'Рост': [172, 169, 178, 168]} # Создаём словарь с нужной информацией о городах.
#
# df = pd.DataFrame(family) # Превращаем словарь в DataFrame, используя стандартный метод библиотеки.
#
# print(f'{df}\n') # Выводим DataFrame на экран.
# Читаем файл Exel с такими же данными
excel_data = pd.read_excel('family.xlsx')
df = pd.DataFrame(excel_data, columns=['Семья', 'Имя', 'Год рождения','Рост'])
# Добавляем  сына
new_son = {'Семья':'Сын', 'Имя': 'Юрий', 'Год рождения':1990, 'Рост':180}
df1 = pd.DataFrame([new_son])
new_list = pd.concat([df1,df], ignore_index=True)
print(f'{new_list}\n')
# Вывод с условием по росту
print(new_list[new_list['Рост'] > 170])



