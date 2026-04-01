def get_unique_set(df, column):
    return set(df[column])

# dataFrame, столбец поиска, атрибут поиска, какой столбец хотим получить
def get_set_by_filter(df, filter_column, filter_value, target_column='Фамилия, имя'):
    return set(df[df[filter_column] == filter_value][target_column])

# или
def union(set1, set2):
    return set1 | set2

# и
def intersection(set1, set2):
    return set1 & set2

def difference(set1, set2):
    return set1 - set2

# симметрическая разность (элементы не находяться одновременно в обоих множествах)
def symmetric_difference(set1, set2):
    return set1 ^ set2