import pandas as pd  # Библиотека для работы с данными в табличном формате

try:
    data = pd.read_csv('students.csv', encoding='utf-8') # Загрузка данных из CSV-файла (encoding='utf-8' чтение русских слов)
    print("Данные успешно загружены!")
except FileNotFoundError:
    print("Ошибка: Файл students.csv не найден!")
    exit()
except Exception as e:
    print(f"Произошла ошибка при загрузке файла: {e}")
    exit()

print("\n1. Первые 5 строк данных:") # Выводим 5 первых строк датасета для ознакомления
print(data.head())  # По умолчанию выводит 5 строк

print("\n2. Информация о данных:") # Выводим информации о структуре данных
print(data.info())  # Показывает типы данных, количество ненулевых значений и использование памяти

print("\n3. Описательная статистика числовых данных:") # Выводим сводную статистику по числовым столбцам
print(data.describe())  # Для числовых столбцов (Age, Score) показывает count, mean, std, min, max и квантили

print("\n4. Анализ успеваемости:") # Выводим среднего балла студентов
average_score = data['Score'].mean()  # Вычисляем среднего арифметического
median_score = data['Score'].median()  # Вычисляем среднее значение в упорядоченном ряду
print(f"Средний балл студентов: {average_score:.2f}")
print(f"Медианный балл студентов: {median_score:.2f}")

print("\n5. Распределение студентов по группам:") # 6. Анализ распределения по группам
group_distribution = data['Group'].value_counts()  # Подсчет количества студентов в каждой группе
print(group_distribution)

# Дополнительный анализ: распределение по возрасту
print("\n6. Распределение студентов по возрасту:")
age_distribution = data['Age'].value_counts().sort_index()  # Подсчет студентов по возрастам с сортировкой
print(age_distribution)

# Визуализация распределения баллов (дополнительно)
try:
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    data['Score'].hist(bins=20, edgecolor='black')
    plt.title('Распределение баллов студентов')
    plt.xlabel('Баллы')
    plt.ylabel('Количество студентов')
    plt.axvline(average_score, color='red', linestyle='dashed', linewidth=1, label=f'Средний балл: {average_score:.2f}')
    plt.legend()
    plt.show()
except ImportError:
    print("\nДля визуализации установите matplotlib: pip install matplotlib")
