# формирует список значений для конкретных полов соответственно, принимает список полов и списки значений для полов
def assemble_by_gender(genders, male_values, female_values):
    male_i = 0
    female_i = 0
    result = []

    for i in genders:
        if i == 'м':
            m_value = male_values[male_i]
            result.append(m_value)
            male_i += 1
        else:
            f_value = female_values[female_i]
            result.append(f_value)
            female_i += 1
    return result