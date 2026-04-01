import numpy as np

# возраст
# N хочу 37, среднее тут 32, отклонение 7
def generate_age(N, mean, std, min_age = 18, max_age = 70):
    raw_ages = np.random.normal(mean, std, N)
    rounded_ages = np.round(raw_ages)
    clipped_ages = np.clip(rounded_ages, min_age, max_age)
    ages = [int(age) for age in clipped_ages]
    return ages

# вес
# N то же, среднее 80, отклонение 20
def generate_weight(N, mean, std, min_weight, max_weight):
    raw_weight = np.random.normal(mean, std, N)
    rounded_weight = np.round(raw_weight)
    clipped_weight = np.clip(rounded_weight, min_weight, max_weight)
    weight = [int(w) for w in clipped_weight]
    return weight

# рост
# N то же, среднее 175 мужч 165 женщ, отклонение 7 мужч 6 женщ
def generate_height(N, mean, std, min_height, max_height):
    raw_height = np.random.normal(mean, std, N)
    rounded_height = np.round(raw_height)
    clipped_height = np.clip(rounded_height, min_height, max_height)
    height = [int(h) for h in clipped_height]
    return height

# доход семьи
# среднее 25000, отклонение 12000
def generate_income(N, mean, std, min_income=0, max_income=100000):
    raw_income = np.random.normal(mean, std, N)
    rounded_income = np.round(raw_income)
    clipped_income = np.clip(rounded_income, min_income, max_income)
    income = [int(i) for i in clipped_income]
    return income