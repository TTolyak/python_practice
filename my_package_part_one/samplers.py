import numpy as np

# пол
def sample_gender(N, prob_male=0.7):
    return np.random.choice(['м', 'ж'], size = N, replace = True, p = [prob_male, 1 - prob_male]).tolist()

# отделы, 1-ый качественный признак
def sample_department(N):
    values = ['Web-разработчик', 'Web-дизайнер', 'Разработчик ядра', 'Системный администратор', 'Тестировщик']
    departments = np.random.choice(values, size=N, replace=True, p=[0.3, 0.15, 0.05, 0.3, 0.2])
    return departments.tolist()

# уровень программиста, 2-ой качественный признак
def sample_level(N):
    values = ['Junior', 'Middle', 'Senior']
    level = np.random.choice(values, size = N, replace = True, p = [0.5, 0.45, 0.05])
    return level.tolist()

# портфолио GitHub, 3-ий качественный признак
def sample_github(N):
    return np.random.choice(['Портфолио имеется', 'Портфолио отсутствует'], size = N, replace = True, p = [0.65, 0.35]).tolist()