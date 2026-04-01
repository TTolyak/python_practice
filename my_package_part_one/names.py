import numpy as np


def generate_full_names(genders):
    male_first = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Иван', 'Евгений', 'Михаил', 'Николай']
    male_last = ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Павлов', 'Семёнов', 'Морозов']
    female_first = ['Анна', 'Мария', 'Елена', 'Ольга', 'Наталья', 'Екатерина', 'Татьяна', 'Ирина', 'Светлана', 'Юлия']
    female_last = ['Иванова', 'Петрова', 'Сидорова', 'Смирнова', 'Кузнецова', 'Попова', 'Васильева', 'Павлова', 'Семёнова', 'Морозова']

    full_names = []
    for gender in genders:
        if gender == 'м':
            name = np.random.choice(male_first)
            surname = np.random.choice(male_last)
            full_names.append(f"{surname} {name}")
        else:
            name = np.random.choice(female_first)
            surname = np.random.choice(female_last)
            full_names.append(f"{surname} {name}")

    return full_names