# гендерная принадлежность, принимаем словарь и 'м' или 'ж'
def filter_dict_by_gender(dictionary, gender):
    filtered_dict = {}
    for key, tuples_list in dictionary.items(): # берем ключ и кортеж значений по отдельности key и tuples_list
        filtered_tuples = []
        for person_tuple in tuples_list: # построчно по кортежу людей
            if person_tuple[3] == gender: # если таблица неизменна, иначе будет плохо в индексах
                filtered_tuples.append(person_tuple)
        if filtered_tuples: # если не пустой список
            filtered_dict[key] = filtered_tuples
    return filtered_dict

# вес, в качестве параметров передаем диапазон от min_we до max_we
def filter_dict_by_weight(dictionary, min_weight, max_weight):
    filtered_dict = {}
    for key, tuples_list in dictionary.items():
        filtered_tuples = []
        for person_tuple in tuples_list:
            if min_weight <= person_tuple[4] <= max_weight:
                filtered_tuples.append(person_tuple)
        if filtered_tuples:
            filtered_dict[key] = filtered_tuples
    return filtered_dict

# рост, аналогично
def filter_dict_by_height(dictionary, min_height, max_height):
    filtered_dict = {}
    for key, tuples_list in dictionary.items():
        filtered_tuples = []
        for person_tuple in tuples_list:
            if min_height <= person_tuple[5] <= max_height:
                filtered_tuples.append(person_tuple)
        if filtered_tuples:
            filtered_dict[key] = filtered_tuples
    return filtered_dict

# возраст
def filter_dict_by_age(dictionary, min_year, max_year):
    filtered_dict = {}
    for key, tuples_list in dictionary.items():
        filtered_tuples = []
        for person_tuple in tuples_list:
            year = 2026 - person_tuple[2]
            if min_year <= year <= max_year:
                filtered_tuples.append(person_tuple)
        if filtered_tuples:
            filtered_dict[key] = filtered_tuples
    return filtered_dict