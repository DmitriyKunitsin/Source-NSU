import csv
import math
from datetime import datetime 

count_separator = 100

def get_average(f):
    clean_vals = [v for v in f if not math.isnan(v)]
    return sum(clean_vals) / len(clean_vals) if clean_vals else 0

def filter_all_by_time(dates, f1, f2, f3, f4, start_str=None, end_str=None):
    """
    Возвращает список всех данных для записей, попадающих в диапазон времени.
    Каждый элемент: (datetime, field1, field2, field3, field4)
    """
    if not dates or not f1 or len(dates) != len(f1):
        return []

    start = datetime.fromisoformat(start_str) if start_str else min(dates)
    end = datetime.fromisoformat(end_str) if end_str else max(dates)

    result = []
    for i, dt in enumerate(dates):
        if start <= dt <= end:
            result.append((dt, f1[i], f2[i], f3[i], f4[i]))
    return result

# Имя файла с данными (поменяй на своё)
file_name = "Черн_ДТП(Омск).csv"
# Открываем файл в кодировке UTF-8
with open(file_name, "r", encoding="utf-8") as f:
    # Читаем CSV с разделителем ;
    reader = csv.DictReader(f, delimiter=";")
    counter = 0
    date_time = []
    field_1 = []
    field_2 = []
    field_3 = []
    field_4 = []
    # Проходим по всем строкам 
    for row in reader:
        # row — это словарь, где ключи — имена столбцов
        # Например: row["created_at"], row["field1"], row["field2"] и т.д.
        counter+=1
        # Выводим несколько полей для примера
        #print(f"Время: {row['created_at']}")
        dt = datetime.fromisoformat(row['created_at'])
        date_time.append(dt)
        #print(f"  field1 = {row['field1']}")# Датчик темпратуры (находится у стенки)
        field_1.append(float(row['field1']))
        #print(f"  field2 = {row['field2']}")# Тепловой поток
        field_2.append(float(row['field2']))
        #print(f"  field3 = {row['field3']}")# Датчик влажности
        field_3.append(float(row['field3']))
        #print(f"  field4 = {row['field4']}")# Датчик температуры ( висит в воздухе )
        field_4.append(float(row['field4']))
    
    # clean_vals = [v for v in field_1 if not math.isnan(v)]
    # average_field1 = sum(clean_vals) / len(clean_vals)
    # print(f"Среднее арифмитическое для field1 : {average_field1} ")
    # print("-" * 30)
    # clean_vals = [v for v in field_2 if not math.isnan(v)]
    # average_field2 = sum(clean_vals) / len(clean_vals)
    # print(f"Среднее арифмитическое для field2 : {average_field2} ")
    # print("-" * 30)
    # clean_vals = [v for v in field_3 if not math.isnan(v)]
    # average_field3 = sum(clean_vals) / len(clean_vals)
    # print(f"Среднее арифмитическое для field3 : {average_field3} ")
    # print("-" * 30)
    # clean_vals = [v for v in field_4 if not math.isnan(v)]
    # average_field4 = sum(clean_vals) / len(clean_vals)
    # print(f"Среднее арифмитическое для field4 : {average_field4} ")
    print("ОМСК")
    print(f"Всего элементов {counter}")
    print('-'*count_separator)
    filtered_12_30_to_13_30 = filter_all_by_time(date_time,field_1,field_2,field_3,field_4 ,
                                start_str= "2026-04-02T12:30:00+07:00", 
                                end_str="2026-04-02T13:30:00+07:00")
    print(
    "Средние с 12:30 по 13:30:\n",
    "f1=", get_average([r[1] for r in filtered_12_30_to_13_30]),
    "f2=", get_average([r[2] for r in filtered_12_30_to_13_30]),
    "f3=", get_average([r[3] for r in filtered_12_30_to_13_30]),
    "f4=", get_average([r[4] for r in filtered_12_30_to_13_30])
    )
    print(f"Всего элементов {len(filtered_12_30_to_13_30)}")
    print('-'*count_separator)
    filtered_13_30_to_14_30 = filter_all_by_time(date_time,field_1,field_2,field_3,field_4 ,
                                start_str= "2026-04-02T13:30:00+07:00", 
                                end_str="2026-04-02T14:30:00+07:00")
    print(
    "Средние с 13:30 по 14:30:\n",
    "f1=", get_average([r[1] for r in filtered_13_30_to_14_30]),
    "f2=", get_average([r[2] for r in filtered_13_30_to_14_30]),
    "f3=", get_average([r[3] for r in filtered_13_30_to_14_30]),
    "f4=", get_average([r[4] for r in filtered_13_30_to_14_30])
    )
    print(f"Всего элементов {len(filtered_13_30_to_14_30)}")
    print('-'*count_separator)
    average_two_between = []
    min_len = min(len(filtered_12_30_to_13_30), len(filtered_13_30_to_14_30))

    for i in range(min_len):
        # Берём кортежи из двух диапазонов
        t1 = filtered_12_30_to_13_30[i]   # (dt, f1, f2, f3, f4)
        t2 = filtered_13_30_to_14_30[i]
        
        # Усредняем каждое поле (начиная с индекса 1, т.к. индекс 0 — это время)
        avg_f1 = (t1[1] + t2[1]) / 2
        avg_f2 = (t1[2] + t2[2]) / 2
        avg_f3 = (t1[3] + t2[3]) / 2
        avg_f4 = (t1[4] + t2[4]) / 2
        
        # Время можно взять любое, например, среднее между двумя датами
        avg_time = t1[0] + (t2[0] - t1[0]) / 2
        
        average_two_between.append((avg_time, avg_f1, avg_f2, avg_f3, avg_f4))
    print(
    "Средние двух диапазонов: \n",
    "f1=", get_average([r[1] for r in average_two_between]),
    "f2=", get_average([r[2] for r in average_two_between]),
    "f3=", get_average([r[3] for r in average_two_between]),
    "f4=", get_average([r[4] for r in average_two_between])
    )
    print(f"Всего элементов {len(average_two_between)}")
    print('-'*count_separator)

# + к воздуху - к земле
file_name = "Оранж_ДТП(Пл_инжиниринг).csv"
with open(file_name, "r", encoding="utf-8") as f:
    # Читаем CSV с разделителем ;
    reader = csv.DictReader(f, delimiter=";")
    counter = 0
    date_time = []
    field_1 = []
    field_2 = []
    field_3 = []
    field_4 = []
    # Проходим по всем строкам 
    for row in reader:
        # row — это словарь, где ключи — имена столбцов
        # Например: row["created_at"], row["field1"], row["field2"] и т.д.
        counter+=1
        # Выводим несколько полей для примера
        #print(f"Время: {row['created_at']}")
        dt = datetime.fromisoformat(row['created_at'])
        date_time.append(dt)
        #print(f"  field1 = {row['field1']}")# Датчик темпратуры (находится у стенки)
        field_1.append(float(row['field1']))
        #print(f"  field2 = {row['field2']}")# Тепловой поток
        field_2.append(float(row['field2']))
        #print(f"  field3 = {row['field3']}")# Датчик влажности
        field_3.append(float(row['field3']))
        #print(f"  field4 = {row['field4']}")# Датчик температуры ( висит в воздухе )
        field_4.append(float(row['field4']))
    print("Инжиринг")
    print(f"Всего элементов {counter}")
    print('-'*count_separator)
    filtered_minus_zero = filter_all_by_time(date_time,field_1,field_2,field_3,field_4 ,
                                start_str= "2026-03-26T12:24:00+07:00", 
                                end_str="2026-03-26T16:38:00+07:00")
    # print(
    # "Средние с 12:30 по 13:30:\n",
    # "f1=", get_average([r[1] for r in filtered_minus_zero]),
    # "f2=", get_average([r[2] for r in filtered_minus_zero]),
    # "f3=", get_average([r[3] for r in filtered_minus_zero]),
    # "f4=", get_average([r[4] for r in filtered_minus_zero])
    # )
    print(f"Всего элементов {len(filtered_minus_zero)}")
    print('-'*count_separator)
    filtered_plus_air = filter_all_by_time(date_time,field_1,field_2,field_3,field_4 ,
                                start_str= "2026-03-26T16:39:00+07:00", 
                                end_str="2026-03-26T16:50:00+07:00")
    # print(
    # "Средние с 13:30 по 14:30:\n",
    # "f1=", get_average([r[1] for r in filtered_plus_air]),
    # "f2=", get_average([r[2] for r in filtered_plus_air]),
    # "f3=", get_average([r[3] for r in filtered_plus_air]),
    # "f4=", get_average([r[4] for r in filtered_plus_air])
    # )
    print(f"Всего элементов {len(filtered_plus_air)}")
    print('-'*count_separator)
    average_two_between_two = []
    min_len = min(len(filtered_minus_zero), len(filtered_plus_air))

    for i in range(min_len):
        # Берём кортежи из двух диапазонов
        t1 = filtered_minus_zero[i]   # (dt, f1, f2, f3, f4)
        t2 = filtered_plus_air[i]
        
        # Усредняем каждое поле (начиная с индекса 1, т.к. индекс 0 — это время)
        avg_f1 = (t1[1] + t2[1]) / 2
        avg_f2 = (t1[2] + t2[2]) / 2
        avg_f3 = (t1[3] + t2[3]) / 2
        avg_f4 = (t1[4] + t2[4]) / 2
        
        # Время можно взять любое, например, среднее между двумя датами
        avg_time = t1[0] + (t2[0] - t1[0]) / 2
        
        average_two_between_two.append((avg_time, avg_f1, avg_f2, avg_f3, avg_f4))
    print(
    "Средние двух диапазонов: \n",
    "f1=", get_average([r[1] for r in average_two_between_two]),
    "f2=", get_average([r[2] for r in average_two_between_two]),
    "f3=", get_average([r[3] for r in average_two_between_two]),
    "f4=", get_average([r[4] for r in average_two_between_two])
    )
    print(f"Всего элементов {len(average_two_between_two)}")
    print('-'*count_separator)

    mean_f1_omsk = get_average([r[1] for r in average_two_between])
    mean_f2_omsk = get_average([r[2] for r in average_two_between])
    mean_f3_omsk = get_average([r[3] for r in average_two_between])
    mean_f4_omsk = get_average([r[4] for r in average_two_between])

    mean_f1_eng = get_average([r[1] for r in average_two_between_two])
    mean_f2_eng = get_average([r[2] for r in average_two_between_two])
    mean_f3_eng = get_average([r[3] for r in average_two_between_two])
    mean_f4_eng = get_average([r[4] for r in average_two_between_two])

    coeff_f1 = mean_f1_omsk / mean_f1_eng if mean_f1_eng != 0 else 1
    coeff_f2 = mean_f2_omsk / mean_f2_eng if mean_f2_eng != 0 else 1
    coeff_f3 = mean_f3_omsk / mean_f3_eng if mean_f3_eng != 0 else 1
    coeff_f4 = mean_f4_omsk / mean_f4_eng if mean_f4_eng != 0 else 1

    coefficient = 1.11
    new_list = []
    for item in average_two_between_two:
        multiplied = (
            item[0],                    
            item[1] * coeff_f1,
            item[2] * coeff_f2,
            item[3] * coeff_f3,
            item[4] * coeff_f4
        )
        new_list.append(multiplied)
    print(
    "Средние двух диапазонов: \n",
    "f1=", get_average([r[1] for r in new_list]),
    "f2=", get_average([r[2] for r in new_list]),
    "f3=", get_average([r[3] for r in new_list]),
    "f4=", get_average([r[4] for r in new_list])
    )
    print(f"Всего элементов {len(new_list)}")
    print('-'*count_separator)
    print("Коэффициенты:\n",
    "f1=", f"{coeff_f1:.2f}",
    "f2=", f"{coeff_f2:.2f}",
    "f3=", f"{coeff_f3:.2f}",
    "f4=", f"{coeff_f4:.2f}")

