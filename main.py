import json
import csv

# Шаг 3: Считываем данные из JSON файла
with open('input.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Шаг 4: Применяем преобразование (в данном случае, никакого преобразования не требуется)

# Шаг 5: Сохраняем измененный набор данных в формате DSV (знак табуляции)
output_file = 'output.tsv'

with open(output_file, 'w', encoding='utf-8', newline='') as tsv_file:
    # Создаем объект для записи в файл с разделителями
    tsv_writer = csv.writer(tsv_file, delimiter='\t')

    # Записываем заголовки
    headers = ["userId", "userName", "emails", "registrationDate", "lastLoginDate", "accountStatus", "publications", "birthDate", "gender"]
    tsv_writer.writerow(headers)

    # Записываем данные
    for item in data:
        row = [
            item["userId"],
            item["userName"],
            ', '.join(item["emails"]),  # Соединяем emails в строку через запятую
            item["registrationDate"],
            item["lastLoginDate"],
            item["accountStatus"],
            ', '.join([pub["name"] for pub in item["publications"]]),  # Соединяем названия публикаций в строку через запятую
            item["birthDate"],
            item["gender"]
        ]
        tsv_writer.writerow(row)

print(f"Данные сохранены в файле {output_file}.")
