from my_package_part_two import filters, sorters, sets_operations, dict_builders, dict_filters, output
import shutil
import pandas as pd

shutil.copyfile('ishodVarNum.xlsx', 'WorkVarNum.xlsx') # копирнули
data_frame = pd.read_excel('WorkVarNum.xlsx') # прочли

with open('results.txt', 'w', encoding ='utf-8') as f:
    f.write("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЧАСТИ 2\n")
    f.write("=" * 50 + "\n\n")

# 1. ВЫВОД ПРОЧТЕННОЙ ТАБЛИЦЫ
for i in data_frame.columns.tolist():
    print(i)
    print(data_frame[i])
    print("-" * 50)

with pd.ExcelWriter('results.xlsx', engine = 'openpyxl') as writer:
    data_frame.to_excel(writer, sheet_name = 'Исходная таблица', index = False)

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("=== ИСХОДНЫЕ ДАННЫЕ ===\n")
    for i in data_frame.columns.tolist():
        f.write(f"{i}\n")
        f.write(f"{data_frame[i]}\n")
        f.write("-" * 50 + "\n")
    f.write("\n")

# 2. СОРТИРОВКА
print("\n=== СОРТИРОВКА ===")
with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n=== СОРТИРОВКА ===\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer: pass
# По весу
print("\n--- По весу (от лёгких к тяжёлым) ---")
sorted_weight_asc = sorters.sort_by_weight(data_frame, ascending=True)
print(sorted_weight_asc[['Фамилия, имя', 'Вес']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По весу (от лёгких к тяжёлым) ---\n")
    f.write(str(sorted_weight_asc[['Фамилия, имя', 'Вес']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_weight_asc.to_excel(writer, sheet_name='Вес (возр)', index=False)

print("\n--- По весу (от тяжёлых к лёгким) ---")
sorted_weight_desc = sorters.sort_by_weight(data_frame, ascending=False)
print(sorted_weight_desc[['Фамилия, имя', 'Вес']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По весу (от тяжёлых к лёгким) ---\n")
    f.write(str(sorted_weight_desc[['Фамилия, имя', 'Вес']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_weight_desc.to_excel(writer, sheet_name='Вес (убыв)', index=False)

# По уровню разраба
print("\n--- По уровню (Junior → Middle → Senior) ---")
sorted_level_asc = sorters.sort_by_level(data_frame, ascending=True)
print(sorted_level_asc[['Фамилия, имя', 'Уровень']])

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По уровню (Junior → Middle → Senior) ---\n")
    f.write(str(sorted_level_asc[['Фамилия, имя', 'Уровень']]))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_level_asc.to_excel(writer, sheet_name='Уровень (возр)', index=False)

# По росту
print("\n--- По росту (от низких к высоким) ---")
sorted_height_asc = sorters.sort_by_height(data_frame, ascending=True)
print(sorted_height_asc[['Фамилия, имя', 'Рост']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По росту (от низких к высоким) ---\n")
    f.write(str(sorted_height_asc[['Фамилия, имя', 'Рост']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_height_asc.to_excel(writer, sheet_name='Рост (возр)', index=False)

print("\n--- По росту (от высоких к низким) ---")
sorted_height_desc = sorters.sort_by_height(data_frame, ascending=False)
print(sorted_height_desc[['Фамилия, имя', 'Рост']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По росту (от высоких к низким) ---\n")
    f.write(str(sorted_height_desc[['Фамилия, имя', 'Рост']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_height_desc.to_excel(writer, sheet_name='Рост (убыв)', index=False)


# По доходу
print("\n--- По доходу (от бедных к богатым) ---")
sorted_income_asc = sorters.sort_by_income(data_frame, ascending=True)
print(sorted_income_asc[['Фамилия, имя', 'Доход семьи']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По доходу (от бедных к богатым) ---\n")
    f.write(str(sorted_income_asc[['Фамилия, имя', 'Доход семьи']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_income_asc.to_excel(writer, sheet_name='Доход (возр)', index=False)

print("\n--- По доходу (от богатых к бедным) ---")
sorted_income_desc = sorters.sort_by_income(data_frame, ascending=False)
print(sorted_income_desc[['Фамилия, имя', 'Доход семьи']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По доходу (от богатых к бедным) ---\n")
    f.write(str(sorted_income_desc[['Фамилия, имя', 'Доход семьи']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_income_desc.to_excel(writer, sheet_name='Доход (убыв)', index=False)


# По году рождения (возрасту)
print("\n--- По году рождения (от старших к младшим) ---")
# ascending=True — сначала старшие (меньший год рождения)
sorted_birth_asc = sorters.sort_by_birth_year(data_frame, ascending=True)
print(sorted_birth_asc[['Фамилия, имя', 'Год рождения']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По году рождения (от старших к младшим) ---\n")
    f.write(str(sorted_birth_asc[['Фамилия, имя', 'Год рождения']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_birth_asc.to_excel(writer, sheet_name='Возраст (старш)', index=False)

print("\n--- По году рождения (от младших к старшим) ---")
sorted_birth_desc = sorters.sort_by_birth_year(data_frame, ascending=False)
print(sorted_birth_desc[['Фамилия, имя', 'Год рождения']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По году рождения (от младших к старшим) ---\n")
    f.write(str(sorted_birth_desc[['Фамилия, имя', 'Год рождения']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_birth_desc.to_excel(writer, sheet_name='Возраст (младш)', index=False)


# По отделу (по алфавиту)
print("\n--- По отделу (по алфавиту А-Я) ---")
sorted_dept_asc = sorters.sort_by_department(data_frame, ascending=True)
print(sorted_dept_asc[['Фамилия, имя', 'Отдел']].head(15))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По отделу (по алфавиту А-Я) ---\n")
    f.write(str(sorted_dept_asc[['Фамилия, имя', 'Отдел']].head(15)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_dept_asc.to_excel(writer, sheet_name='Отдел (А-Я)', index=False)

print("\n--- По отделу (по алфавиту Я-А) ---")
sorted_dept_desc = sorters.sort_by_department(data_frame, ascending=False)
print(sorted_dept_desc[['Фамилия, имя', 'Отдел']].head(15))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- По отделу (по алфавиту Я-А) ---\n")
    f.write(str(sorted_dept_desc[['Фамилия, имя', 'Отдел']].head(15)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sorted_dept_desc.to_excel(writer, sheet_name='Отдел (Я-А)', index=False)

# 3. ФИЛЬТРАЦИЯ
print("\n=== ФИЛЬТРАЦИЯ DATAFRAME ===")
with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n=== ФИЛЬТРАЦИЯ DATAFRAME ===\n")

# Подготавливаем Excel для фильтрации
with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    pass

# 3.1 Фильтрация по полу
print("\n--- Только мужчины ---")
males = filters.filter_by_gender(data_frame, 'м')
print(males[['Фамилия, имя', 'Пол', 'Отдел']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Только мужчины ---\n")
    f.write(str(males[['Фамилия, имя', 'Пол', 'Отдел']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    males.to_excel(writer, sheet_name='Мужчины', index=False)

print("\n--- Только женщины ---")
females = filters.filter_by_gender(data_frame, 'ж')
print(females[['Фамилия, имя', 'Пол', 'Отдел']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Только женщины ---\n")
    f.write(str(females[['Фамилия, имя', 'Пол', 'Отдел']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    females.to_excel(writer, sheet_name='Женщины', index=False)


# 3.2 Фильтрация по отделу
print("\n--- Только Web-разработчики ---")
web_devs = filters.filter_by_department(data_frame, 'Web-разработчик')
print(web_devs[['Фамилия, имя', 'Отдел', 'Уровень']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Только Web-разработчики ---\n")
    f.write(str(web_devs[['Фамилия, имя', 'Отдел', 'Уровень']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    web_devs.to_excel(writer, sheet_name='Web-разработчики', index=False)

print("\n--- Только тестировщики ---")
testers = filters.filter_by_department(data_frame, 'Тестировщик')
print(testers[['Фамилия, имя', 'Отдел', 'Уровень']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Только тестировщики ---\n")
    f.write(str(testers[['Фамилия, имя', 'Отдел', 'Уровень']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    testers.to_excel(writer, sheet_name='Тестировщики', index=False)


# 3.3 Фильтрация по уровню
print("\n--- Только Junior ---")
juniors = filters.filter_by_level(data_frame, 'Junior')
print(juniors[['Фамилия, имя', 'Уровень', 'Отдел']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Только Junior ---\n")
    f.write(str(juniors[['Фамилия, имя', 'Уровень', 'Отдел']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    juniors.to_excel(writer, sheet_name='Junior', index=False)

print("\n--- Только Senior ---")
seniors = filters.filter_by_level(data_frame, 'Senior')
print(seniors[['Фамилия, имя', 'Уровень', 'Отдел']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Только Senior ---\n")
    f.write(str(seniors[['Фамилия, имя', 'Уровень', 'Отдел']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    seniors.to_excel(writer, sheet_name='Senior', index=False)


# 3.4 Фильтрация по портфолио GitHub
print("\n--- С портфолио на GitHub ---")
with_portfolio = filters.filter_by_github(data_frame, True)
print(with_portfolio[['Фамилия, имя', 'Портфолио GitHub', 'Отдел']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- С портфолио на GitHub ---\n")
    f.write(str(with_portfolio[['Фамилия, имя', 'Портфолио GitHub', 'Отдел']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    with_portfolio.to_excel(writer, sheet_name='С портфолио', index=False)

print("\n--- Без портфолио на GitHub ---")
without_portfolio = filters.filter_by_github(data_frame, False)
print(without_portfolio[['Фамилия, имя', 'Портфолио GitHub', 'Отдел']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Без портфолио на GitHub ---\n")
    f.write(str(without_portfolio[['Фамилия, имя', 'Портфолио GitHub', 'Отдел']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    without_portfolio.to_excel(writer, sheet_name='Без портфолио', index=False)


# 3.5 Фильтрация по весу (диапазон)
print("\n--- Люди с весом от 60 до 80 кг ---")
weight_range = filters.filter_by_weight(data_frame, 60, 80)
print(weight_range[['Фамилия, имя', 'Вес', 'Пол']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Люди с весом от 60 до 80 кг ---\n")
    f.write(str(weight_range[['Фамилия, имя', 'Вес', 'Пол']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    weight_range.to_excel(writer, sheet_name='Вес 60-80', index=False)


# 3.6 Фильтрация по росту (диапазон)
print("\n--- Люди с ростом от 165 до 180 см ---")
height_range = filters.filter_by_height(data_frame, 165, 180)
print(height_range[['Фамилия, имя', 'Рост', 'Пол']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Люди с ростом от 165 до 180 см ---\n")
    f.write(str(height_range[['Фамилия, имя', 'Рост', 'Пол']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    height_range.to_excel(writer, sheet_name='Рост 165-180', index=False)


# 3.7 Фильтрация по доходу (диапазон)
print("\n--- Люди с доходом от 30000 до 60000 ---")
income_range = filters.filter_by_income(data_frame, 30000, 60000)
print(income_range[['Фамилия, имя', 'Доход семьи', 'Отдел']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Люди с доходом от 30000 до 60000 ---\n")
    f.write(str(income_range[['Фамилия, имя', 'Доход семьи', 'Отдел']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    income_range.to_excel(writer, sheet_name='Доход 30-60', index=False)


# 3.8 Фильтрация по возрасту
print("\n--- Люди младше 30 лет ---")
young = filters.filter_by_age(data_frame, max_age=30)
print(young[['Фамилия, имя', 'Год рождения']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Люди младше 30 лет ---\n")
    f.write(str(young[['Фамилия, имя', 'Год рождения']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    young.to_excel(writer, sheet_name='Младше 30', index=False)

print("\n--- Люди старше 40 лет ---")
old = filters.filter_by_age(data_frame, min_age=40)
print(old[['Фамилия, имя', 'Год рождения']].head(10))

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Люди старше 40 лет ---\n")
    f.write(str(old[['Фамилия, имя', 'Год рождения']].head(10)))
    f.write("\n")

with pd.ExcelWriter('results.xlsx', engine = 'openpyxl', mode='a') as writer:
    old.to_excel(writer, sheet_name = 'Старше 40', index = False)

# 4. МНОЖЕСТВА
print("\n=== РАБОТА С МНОЖЕСТВАМИ ===")
with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n=== РАБОТА С МНОЖЕСТВАМИ ===\n")

print("\n--- Формирование множеств ---")

# Отдел
web_devs = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Web-разработчик')
testers = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Тестировщик')
sys_admins = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Системный администратор')
designers = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Web-дизайнер')
kernel_devs = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Разработчик ядра')

# Уровень
juniors = sets_operations.get_set_by_filter(data_frame, 'Уровень', 'Junior')
middles = sets_operations.get_set_by_filter(data_frame, 'Уровень', 'Middle')
seniors = sets_operations.get_set_by_filter(data_frame, 'Уровень', 'Senior')

# Портфолио
with_portfolio = sets_operations.get_set_by_filter(data_frame, 'Портфолио GitHub', 'Портфолио имеется')
without_portfolio = sets_operations.get_set_by_filter(data_frame, 'Портфолио GitHub', 'Портфолио отсутствует')

print(f"Web-разработчики ({len(web_devs)} чел.): {web_devs}")
print(f"Тестировщики ({len(testers)} чел.): {testers}")
print(f"Junior ({len(juniors)} чел.): {juniors}")
print(f"Senior ({len(seniors)} чел.): {seniors}")
print(f"С портфолио ({len(with_portfolio)} чел.): {with_portfolio}")

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write(f"\nWeb-разработчики ({len(web_devs)} чел.): {web_devs}\n")
    f.write(f"Тестировщики ({len(testers)} чел.): {testers}\n")
    f.write(f"Junior ({len(juniors)} чел.): {juniors}\n")
    f.write(f"Senior ({len(seniors)} чел.): {seniors}\n")
    f.write(f"С портфолио ({len(with_portfolio)} чел.): {with_portfolio}\n")

# Работа с множествами
print("\n--- Операции с множествами ---")

# Объединение
web_or_testers = sets_operations.union(web_devs, testers)
print(f"Web ИЛИ тестировщики ({len(web_or_testers)} чел.): {web_or_testers}")

# Пересечение
senior_with_portfolio = sets_operations.intersection(seniors, with_portfolio)
print(f"Senior с портфолио ({len(senior_with_portfolio)} чел.): {senior_with_portfolio}")

# Разность
web_not_senior = sets_operations.difference(web_devs, seniors)
print(f"Web-разработчики, не Senior ({len(web_not_senior)} чел.): {web_not_senior}")

# Симметрическая разность: либо Web, либо тест, но не оба
web_xor_testers = sets_operations.symmetric_difference(web_devs, testers)
print(f"Только Web ИЛИ только тестировщики ({len(web_xor_testers)} чел.): {web_xor_testers}")

# Более сложные комбинации
print("\n--- Комбинированные операции ---")

# Junior-тестировщики
junior_testers = sets_operations.intersection(juniors, testers)
print(f"Junior-тестировщики ({len(junior_testers)} чел.): {junior_testers}")

# Senior-разработчики (все отделы) с портфолио
senior_with_portfolio_all = sets_operations.intersection(seniors, with_portfolio)
print(f"Senior с портфолио (все отделы) ({len(senior_with_portfolio_all)} чел.): {senior_with_portfolio_all}")

# Web-разработчики без портфолио
web_no_portfolio = sets_operations.difference(web_devs, with_portfolio)
print(f"Web-разработчики без портфолио ({len(web_no_portfolio)} чел.): {web_no_portfolio}")

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Операции с множествами ---\n")
    f.write(f"Web ИЛИ тестировщики ({len(web_or_testers)} чел.): {web_or_testers}\n")
    f.write(f"Senior с портфолио ({len(senior_with_portfolio)} чел.): {senior_with_portfolio}\n")
    f.write(f"Web-разработчики, не Senior ({len(web_not_senior)} чел.): {web_not_senior}\n")
    f.write(f"Только Web ИЛИ только тестировщики ({len(web_xor_testers)} чел.): {web_xor_testers}\n")
    f.write("\n--- Комбинированные операции ---\n")
    f.write(f"Junior-тестировщики ({len(junior_testers)} чел.): {junior_testers}\n")
    f.write(f"Senior с портфолио (все отделы) ({len(senior_with_portfolio_all)} чел.): {senior_with_portfolio_all}\n")
    f.write(f"Web-разработчики без портфолио ({len(web_no_portfolio)} чел.): {web_no_portfolio}\n")

# Уникальные значения столбов
print("\n--- Уникальные значения в столбцах ---")

unique_departments = sets_operations.get_unique_set(data_frame, 'Отдел')
unique_levels = sets_operations.get_unique_set(data_frame, 'Уровень')
unique_genders = sets_operations.get_unique_set(data_frame, 'Пол')
unique_github = sets_operations.get_unique_set(data_frame, 'Портфолио GitHub')

print(f"Уникальные отделы: {unique_departments}")
print(f"Уникальные уровни: {unique_levels}")
print(f"Уникальные полы: {unique_genders}")
print(f"Уникальные статусы GitHub: {unique_github}")

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write("\n--- Уникальные значения в столбцах ---\n")
    f.write(f"Уникальные отделы: {unique_departments}\n")
    f.write(f"Уникальные уровни: {unique_levels}\n")
    f.write(f"Уникальные полы: {unique_genders}\n")
    f.write(f"Уникальные статусы GitHub: {unique_github}\n")

# Для Excel сохраним информацию о множествах в текстовом виде (так как множества не таблицы)
with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    sets_info = pd.DataFrame({
        'Множество': ['Web-разработчики', 'Тестировщики', 'Junior', 'Senior', 'С портфолио'],
        'Количество': [len(web_devs), len(testers), len(juniors), len(seniors), len(with_portfolio)],
        'Элементы': [str(web_devs), str(testers), str(juniors), str(seniors), str(with_portfolio)]
    })
    sets_info.to_excel(writer, sheet_name='Множества', index=False)

