# from main_part_one import departments


def build_dict_by_column(df, key_column):
    departments = df[key_column].unique()

    result = {}
    for dept in departments:
        people_in_dept = df[df[key_column] == dept]
        people_without_dept = people_in_dept.drop(columns=[key_column]) # удаляем столбец из dataFrame
        list_of_tuples = [tuple(row) for row in people_without_dept.values]
        result[dept] = list_of_tuples
    return result

def build_dict_by_column_2key(df, key_column_one, key_column_two):
    unique_vals1 = df[key_column_one].unique()
    unique_vals2 = df[key_column_two].unique()
    result = {}

    for val1 in unique_vals1:
        for val2 in unique_vals2:
            filtered = df[(df[key_column_one] == val1) & (df[key_column_two] == val2)]
            if len(filtered) > 0: # проверяю наличие пустык строк
                without_keys = filtered.drop(columns=[key_column_one, key_column_two]) # удаляем уже два столба
                tuples_list = [tuple(row) for row in without_keys.values]
                result[(val1, val2)] = tuples_list
    return result