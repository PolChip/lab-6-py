import pandas as pd

data = pd.read_csv('students_with_gaps.csv', encoding='utf-8', sep = ',') # Загрузка данных из CSV-файла (encoding='utf-8' чтение русских слов)

# Проверка пропусков
print("Количество пропусков по столбцам:")
print(data.isnull().sum()) # выводит количество NaN (пустые ячейки) по столбцам

# Заполнение пропусков в Score средним баллом
mean_score = data['Score'].mean()
data['Score'] = data['Score'].fillna(mean_score)

# Удаление строк с пропусками в Group
data = data.dropna(subset=['Group'])

# Проверка результата
print("\nПосле обработки пропусков:")
print(data.isnull().sum())

# Сохранение очищенных данных
data.to_csv('students_clean.csv', index=False)