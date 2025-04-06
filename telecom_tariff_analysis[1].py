# 📊 Проект: Анализ тарифов телеком-компании

"""
Цель проекта:
Провести предварительный анализ поведения клиентов по тарифам "Smart" и "Ultra", и выяснить:
1. Какой тариф приносит больше выручки
2. Есть ли различия в выручке по регионам (Москва и другие)
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Загрузка таблицы с выручкой
df = pd.read_csv("monthly_revenue.csv")

# Группировка: средняя выручка по тарифам
df.groupby('tariff')['revenue'].mean().plot(kind='bar', title='Средняя выручка по тарифам')
plt.ylabel('Средняя выручка')
plt.show()

# Группировка: по тарифу и городу
df.groupby(['tariff', 'city'])['revenue'].mean().plot(kind='bar', title='Средняя выручка по тарифу и городу')
plt.ylabel('Средняя выручка')
plt.xticks(rotation=45)
plt.show()

# Гипотезы
alpha = 0.05
smart = df[df['tariff'] == 'smart']['revenue']
ultra = df[df['tariff'] == 'ultra']['revenue']
moscow = df[df['city'] == 'Москва']['revenue']
regions = df[df['city'] != 'Москва']['revenue']

# Проверка гипотез
test1 = stats.ttest_ind(smart, ultra, equal_var=False)
test2 = stats.ttest_ind(moscow, regions, equal_var=False)

print("Гипотеза 1: тарифы")
print("p-value:", test1.pvalue)
if test1.pvalue < alpha:
    print("Отклоняем H0: тарифы различаются")
else:
    print("Не отклоняем H0")

print("\nГипотеза 2: Москва vs регионы")
print("p-value:", test2.pvalue)
if test2.pvalue < alpha:
    print("Отклоняем H0: различия есть")
else:
    print("Не отклоняем H0")
