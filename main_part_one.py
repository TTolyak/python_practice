import pandas as pd
from my_package_part_one import generators as g, samplers as s, utils as u, names as n
N = 37

numbers = list(range(1, N + 1)) # 1 столбец
age_start = g.generate_age(N, 32, 7, 18, 70) # возраст, но не 3 столбец!
age_end = [2026 - age for age in age_start] # вот это уже 3 столбец, год рождения
genders = s.sample_gender(N, 0.7) # пол, 4 столбец

count_male = genders.count('м')
count_female = genders.count('ж')

# далее пойдет вес
male_weight = g.generate_weight(count_male, 80, 7, 50, 150) # мужик
female_weight = g.generate_weight(count_female, 65, 6, 40, 100) # женщина

weight = u.assemble_by_gender(genders, male_weight, female_weight) # столбец веса, 5 столб

# далее пойдет рост
male_height = g.generate_height(count_male, 170, 7, 150, 220)
female_height = g.generate_height(count_female, 160, 6, 140, 200)

height = u.assemble_by_gender(genders, male_height, female_height) # итог рост, 6 столбец

departments = s.sample_department(N) # 7 столбец - отдел

levels = s.sample_level(N) # 8 столбец - уровень

incomes = g.generate_income(N, mean = 25000, std = 12000, min_income = 0, max_income = 100000) # 9 столбец - доход семьи

github = s.sample_github(N) # 10 столбец - GitHub

names = n.generate_full_names(genders) # имена, 2 столб

data_frame_dict = {
    'Номер' : numbers ,
    'Фамилия, имя' : names ,
    'Год рождения' : age_end ,
    'Пол' : genders ,
    'Вес' : weight ,
    'Рост' : height ,
    'Отдел' : departments ,
    'Уровень' : levels ,
    'Доход семьи' : incomes ,
    'Портфолио GitHub' : github
}
data_frame = pd.DataFrame(data_frame_dict)
data_frame.to_excel('ishodVarNum.xlsx', index = False)
data_frame.to_csv('ishodVarNum.csv', index = False)"���������" 
