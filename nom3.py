import pandas as pd

data = pd.read_csv('students_with_gaps.csv', encoding='utf-8', sep = ',') # Загрузка данных из CSV-файла (encoding='utf-8' чтение русских слов)

# Проверка пропусков
print("Количество пропусков по столбцам:")
print(data.isnull().sum()) # выводит количество NaN (пустые ячейки) по столбцам

mean_score = data['Score'].mean() # Вычисляет ср. знач. в столбце Score
data['Score'] = data['Score'].fillna(mean_score) # заменяем пустые знач Score на ср балл

# Удаление строк с пропусками в Group
data = data.dropna(subset=['Group'])

print("\nПосле обработки пропусков:")
print(data.isnull().sum()) # Проверку на наличие пропущенных данных

# Сохранение очищенных данных
data.to_csv('students_clean.csv', index=False)
