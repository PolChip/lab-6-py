import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('students.csv', encoding='utf-8', sep = ',') # Загрузка данных из CSV-файла (encoding='utf-8' чтение русских слов)

# 1. Гистограмма распределения баллов
plt.figure(figsize=(10, 5))
data['Score'].hist(bins=20, color='#F2DBD5', edgecolor='#D9B2A9')
plt.title('Распределение баллов студентов')
plt.xlabel('Баллы')
plt.ylabel('Количество студентов')
plt.grid(alpha=0.5)
plt.show()

# 2. Столбчатая диаграмма по группам
plt.figure(figsize=(10, 5))
data.groupby('Group')['Score'].mean().plot(kind='bar', color='#FE76B7', edgecolor='#620940')
plt.title('Средний балл по группам')
plt.xlabel('Группа')
plt.ylabel('Средний балл')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.5)
plt.show()
