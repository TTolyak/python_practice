from my_package_part_two import filters, sorters, sets_operations
import shutil
import pandas as pd

# копирнули и прочли
shutil.copyfile('ishodVarNum.xlsx', 'WorkVarNum.xlsx')
data_frame = pd.read_excel('WorkVarNum.xlsx')


txt_results = []
txt_results.append("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЧАСТИ 2")
txt_results.append("=" * 50)
txt_results.append("")

# Подготовка для txt
txt_results.append(" ИСХОДНЫЕ ДАННЫЕ ")
for col in data_frame.columns.tolist():
    txt_results.append(f"{col}")
    txt_results.append(f"{data_frame[col]}")
    txt_results.append("-" * 50)
txt_results.append("")

# исходная таблица для excel (отдельно сохраним позже)

# 2. сортировка
txt_results.append(" СОРТИРОВКА ")
txt_results.append("")

excel_sheets = {}
excel_sheets['Исходная таблица'] = data_frame

sorted_weight_asc = sorters.sort_by_weight(data_frame, ascending=True)
txt_results.append(" По весу (от лёгких к тяжёлым) ")
txt_results.append(str(sorted_weight_asc[['Фамилия, имя', 'Вес']].head(10)))
txt_results.append("")
excel_sheets['Вес (возр)'] = sorted_weight_asc

sorted_level_asc = sorters.sort_by_level(data_frame, ascending=True)
txt_results.append(" По уровню (Junior → Middle → Senior) ")
txt_results.append(str(sorted_level_asc[['Фамилия, имя', 'Уровень']]))
txt_results.append("")
excel_sheets['Уровень (возр)'] = sorted_level_asc

sorted_height_asc = sorters.sort_by_height(data_frame, ascending=True)
txt_results.append(" По росту (от низких к высоким) ")
txt_results.append(str(sorted_height_asc[['Фамилия, имя', 'Рост']].head(10)))
txt_results.append("")
excel_sheets['Рост (возр)'] = sorted_height_asc

sorted_income_asc = sorters.sort_by_income(data_frame, ascending=True)
txt_results.append(" По доходу (от бедных к богатым) ")
txt_results.append(str(sorted_income_asc[['Фамилия, имя', 'Доход семьи']].head(10)))
txt_results.append("")
excel_sheets['Доход (возр)'] = sorted_income_asc

sorted_birth_asc = sorters.sort_by_birth_year(data_frame, ascending=True)
txt_results.append(" По году рождения (от старших к младшим) ")
txt_results.append(str(sorted_birth_asc[['Фамилия, имя', 'Год рождения']].head(10)))
txt_results.append("")
excel_sheets['Возраст (старш)'] = sorted_birth_asc

sorted_dept_asc = sorters.sort_by_department(data_frame, ascending=True)
txt_results.append(" По отделу (по алфавиту А-Я) ")
txt_results.append(str(sorted_dept_asc[['Фамилия, имя', 'Отдел']].head(15)))
txt_results.append("")
excel_sheets['Отдел (А-Я)'] = sorted_dept_asc

# 3. фильтрация
txt_results.append(" ФИЛЬТРАЦИЯ DATAFRAME ")
txt_results.append("")

males = filters.filter_by_gender(data_frame, 'м')
txt_results.append(" Только мужчины ")
txt_results.append(str(males[['Фамилия, имя', 'Пол', 'Отдел']].head(10)))
txt_results.append("")
excel_sheets['Мужчины'] = males

web_devs_filter = filters.filter_by_department(data_frame, 'Web-разработчик')
txt_results.append(" Только Web-разработчики ")
txt_results.append(str(web_devs_filter[['Фамилия, имя', 'Отдел', 'Уровень']].head(10)))
txt_results.append("")
excel_sheets['Web-разработчики'] = web_devs_filter

seniors_filter = filters.filter_by_level(data_frame, 'Senior')
txt_results.append(" Только Senior ")
txt_results.append(str(seniors_filter[['Фамилия, имя', 'Уровень', 'Отдел']].head(10)))
txt_results.append("")
excel_sheets['Senior'] = seniors_filter

with_portfolio_filter = filters.filter_by_github(data_frame, True)
txt_results.append(" С портфолио на GitHub ")
txt_results.append(str(with_portfolio_filter[['Фамилия, имя', 'Портфолио GitHub', 'Отдел']].head(10)))
txt_results.append("")
excel_sheets['С портфолио'] = with_portfolio_filter

weight_range = filters.filter_by_weight(data_frame, 60, 80)
txt_results.append(" Люди с весом от 60 до 80 кг ")
txt_results.append(str(weight_range[['Фамилия, имя', 'Вес', 'Пол']].head(10)))
txt_results.append("")
excel_sheets['Вес 60-80'] = weight_range

height_range = filters.filter_by_height(data_frame, 165, 180)
txt_results.append(" Люди с ростом от 165 до 180 см ")
txt_results.append(str(height_range[['Фамилия, имя', 'Рост', 'Пол']].head(10)))
txt_results.append("")
excel_sheets['Рост 165-180'] = height_range

income_range = filters.filter_by_income(data_frame, 30000, 60000)
txt_results.append(" Люди с доходом от 30000 до 60000 ")
txt_results.append(str(income_range[['Фамилия, имя', 'Доход семьи', 'Отдел']].head(10)))
txt_results.append("")
excel_sheets['Доход 30-60'] = income_range

young = filters.filter_by_age(data_frame, max_age=30)
txt_results.append(" Люди младше 30 лет ")
txt_results.append(str(young[['Фамилия, имя', 'Год рождения']].head(10)))
txt_results.append("")
excel_sheets['Младше 30'] = young

old = filters.filter_by_age(data_frame, min_age=40)
txt_results.append(" Люди старше 40 лет ")
txt_results.append(str(old[['Фамилия, имя', 'Год рождения']].head(10)))
txt_results.append("")
excel_sheets['Старше 40'] = old

# 4. множества
txt_results.append(" РАБОТА С МНОЖЕСТВАМИ ")
txt_results.append("")

web_devs_set = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Web-разработчик')
kernel_devs_set = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Разработчик ядра')
testers_set = sets_operations.get_set_by_filter(data_frame, 'Отдел', 'Тестировщик')  # если есть такой отдел
seniors_set = sets_operations.get_set_by_filter(data_frame, 'Уровень', 'Senior')
with_portfolio_set = sets_operations.get_set_by_filter(data_frame, 'Портфолио GitHub', 'Портфолио имеется')

txt_results.append(" Формирование множеств ")
txt_results.append(f"Web-разработчики ({len(web_devs_set)} чел.): {web_devs_set}")
txt_results.append(f"Senior ({len(seniors_set)} чел.): {seniors_set}")
txt_results.append(f"С портфолио ({len(with_portfolio_set)} чел.): {with_portfolio_set}")
txt_results.append("")

# операции с множествами
txt_results.append(" Операции с множествами ")

web_or_testers = sets_operations.union(web_devs_set, testers_set) if testers_set else web_devs_set
txt_results.append(f"Web ИЛИ тестировщики ({len(web_or_testers)} чел.): {web_or_testers}")

senior_with_portfolio = sets_operations.intersection(seniors_set, with_portfolio_set)
txt_results.append(f"Senior с портфолио ({len(senior_with_portfolio)} чел.): {senior_with_portfolio}")

web_not_senior = sets_operations.difference(web_devs_set, seniors_set)
txt_results.append(f"Web-разработчики, не Senior ({len(web_not_senior)} чел.): {web_not_senior}")
txt_results.append("")

# комбинированные операции
txt_results.append(" Комбинированные операции ")

senior_with_portfolio_all = sets_operations.intersection(seniors_set, with_portfolio_set)
txt_results.append(f"Senior с портфолио (все отделы) ({len(senior_with_portfolio_all)} чел.): {senior_with_portfolio_all}")
txt_results.append("")

# уникальные значения
txt_results.append(" Уникальные значения в столбцах ")

unique_departments = sets_operations.get_unique_set(data_frame, 'Отдел')
unique_github = sets_operations.get_unique_set(data_frame, 'Портфолио GitHub')

txt_results.append(f"Уникальные отделы: {unique_departments}")
txt_results.append(f"Уникальные статусы GitHub: {unique_github}")

# данные о множествах для excel (в виде таблицы)
sets_df = pd.DataFrame({
    'Множество': ['Web-разработчики', 'Senior', 'С портфолио'],
    'Количество': [len(web_devs_set), len(seniors_set), len(with_portfolio_set)],
    'Элементы': [str(web_devs_set), str(seniors_set), str(with_portfolio_set)]
})
excel_sheets['Множества'] = sets_df


# TXT
with open('results.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(txt_results))

# XLSX
with pd.ExcelWriter('WorkVarNum.xlsx', engine='openpyxl') as writer:
    for sheet_name, df in excel_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)


print("\n ИСХОДНЫЕ ДАННЫЕ ")
for col in data_frame.columns.tolist():
    print(col)
    print(data_frame[col])
    print("-" * 50)

print("\n СОРТИРОВКА ")
print("\n По весу (от лёгких к тяжёлым) ")
print(sorted_weight_asc[['Фамилия, имя', 'Вес']].head(10))
print("\n По уровню (Junior → Middle → Senior) ")

print("\n ФИЛЬТРАЦИЯ DATAFRAME ")
print("\n Только мужчины ")
print(males[['Фамилия, имя', 'Пол', 'Отдел']].head(10))
print("\n Только Web-разработчики ")
print(web_devs_filter[['Фамилия, имя', 'Отдел', 'Уровень']].head(10))


print("\n РАБОТА С МНОЖЕСТВАМИ ")
print("\n Формирование множеств ")
print(f"Web-разработчики ({len(web_devs_set)} чел.): {web_devs_set}")
print("\n Операции с множествами ")
print(f"Web ИЛИ тестировщики ({len(web_or_testers)} чел.): {web_or_testers}")
print("\n Комбинированные операции ")
print(f"Senior с портфолио (все отделы) ({len(senior_with_portfolio_all)} чел.): {senior_with_portfolio_all}")
print("\n Уникальные значения в столбцах ")
print(f"Уникальные отделы: {unique_departments}")