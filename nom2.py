import pandas as pd  # Библиотека для работы с данными в табличном формате


data = pd.read_csv('students.csv', encoding='utf-8', sep = ',') # Загрузка данных из CSV-файла (encoding='utf-8' чтение русских слов)

high_scorers = data[data['Score'] > 80] # Фильтрация: балл > 80

top_students = high_scorers.sort_values('Score', ascending=False) # Сортировка по убыванию балла

# Поиск возрастных экстремумов
oldest = data.loc[data['Age'].idxmax()]  # Самый старший
youngest = data.loc[data['Age'].idxmin()]  # Самый младший

# Вывод результатов
print("Топ студенты (балл > 80):")
print(top_students[['Name', 'Score']])

print(f"\nСамый старший: {oldest['Name']}, {oldest['Age']} лет")
print(f"Самый младший: {youngest['Name']}, {youngest['Age']} лет")