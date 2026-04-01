import pandas as pd

# пол
# за gender 'м' 'ж'
def filter_by_gender(df, gender):
    mask = df['Пол'] == gender
    filtered = df[mask]
    return filtered

# отдел
# за department принимаем 'Web-разработчик', 'Тестировщик' и т.д.
def filter_by_department(df, department):
    mask = df['Отдел'] == department
    filtered = df[mask]
    return filtered

# уровень
# за level принимаем 'Junior', 'Middle' или 'Senior'
def filter_by_level(df, level):
    mask = df['Уровень'] == level
    filtered = df[mask]
    return filtered

# портфолио гит
# за has... принимаем 'Портфолио имеется' и 'Портфолио отсутствует'
def filter_by_github(df, has_portfolio):
    if has_portfolio:
        mask = df['Портфолио GitHub'] == 'Портфолио имеется'
    else:
        mask = df['Портфолио GitHub'] == 'Портфолио отсутствует'
    filtered = df[mask]
    return filtered

# фильтр веса
# можем указать либо мин вес, либо макс вес, либо ничего (вернет dataFrame)
def filter_by_weight(df, min_weight=None, max_weight=None):
    if min_weight is None and max_weight is None: return df

    mask = pd.Series([True] * len(df))

    if min_weight is not None:
        mask = mask & (df['Вес'] >= min_weight)
    if max_weight is not None:
        mask = mask & (df['Вес'] <= max_weight)
    filtered = df[mask]
    return filtered

# фильтр роста
# аналогично весу
def filter_by_height(df, min_height = None, max_height = None):
    if min_height is None and max_height is None: return df

    mask = pd.Series([True] * len(df))

    if min_height is not None:
        mask = mask & (df['Рост'] >= min_height)
    if max_height is not None:
        mask = mask & (df['Рост'] <= max_height)
    return df[mask]

# доход семьи
# аналогично
def filter_by_income(df, min_income=None, max_income=None):
    if min_income is None and max_income is None: return df

    mask = pd.Series([True] * len(df))

    if min_income is not None:
        mask = mask & (df['Доход семьи'] >= min_income)
    if max_income is not None:
        mask = mask & (df['Доход семьи'] <= max_income)
    filtered = df[mask]
    return filtered

# возраст
def filter_by_age(df, min_age=None, max_age=None, current_year=2026):
    if min_age is None and max_age is None: return df
    mask = pd.Series([True] * len(df), index=df.index)
    year = current_year - df['Год рождения']

    if min_age is not None:
        mask = mask & (year >= min_age)
    if max_age is not None:
        mask = mask & (year <= max_age)
    filtered = df[mask]
    return filtered