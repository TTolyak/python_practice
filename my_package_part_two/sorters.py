import pandas as pd

def sort_by_weight(df, ascending = True):
    return df.sort_values(by = 'Вес', ascending = ascending, inplace = False, na_position = 'last')

def sort_by_height(df, ascending = True):
    return df.sort_values(by = 'Рост', ascending = ascending, inplace = False, na_position = 'last')

def sort_by_income(df, ascending = True):
    return df.sort_values(by = 'Доход семьи', ascending = ascending, inplace = False, na_position = 'last')

def sort_by_birth_year(df, ascending=True):
    return df.sort_values(by='Год рождения', ascending=ascending, inplace=False, na_position='last')

# уровень разраба, от джуна к сеньору или наоборот
def sort_by_level(df, ascending=True):
    df_copy = df.copy()

    level_order = ['Junior', 'Middle', 'Senior']
    df_copy['Уровень'] = pd.Categorical(df_copy['Уровень'], categories = level_order, ordered = True) # категория

    sorted_df = df_copy.sort_values(by = 'Уровень', ascending = ascending) # сорт

    sorted_df['Уровень'] = sorted_df['Уровень'].astype(str) # обратно столбец
    return sorted_df

# отдел по алфавиту
def sort_by_department(df, ascending=True):
    return df.sort_values(by='Отдел', ascending=ascending, inplace=False, na_position='last')