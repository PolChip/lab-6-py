import pandas as pd  # Библиотека для работы с данными в табличном формате


data = pd.read_csv('students.csv', encoding='utf-8', sep = ',') # Загрузка данных из CSV-файла

print("\nСредний балл по группам:")
print(data.groupby('Group')['Score'].mean())  # Средний балл для каждой группы

print("\nМедианный возраст по группам:")
print(data.groupby('Group')['Age'].median())  # Медиана возраста по группам

data['Passed'] = data['Score'].apply(lambda x: 1 if x >= 60 else 0)  # Добавляем новый столбец Passed (1, если балл ≥ 60, иначе 0)
print("\nПолные данные с результатами:")
print(data)  # Вывод всех данных с новым столбцом
