import os

first_file_name = input("Введите название первого файла:")
last_file_name = input("Введите название второго файла:")

first_number = int(first_file_name.split(".")[0])
last_number = int(last_file_name.split(".")[0])  # Извлекаем номера из файлов

folder_path = "files"  # Папка с файлами
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Папка {folder_path} создана")

for number in range(first_number, last_number + 1):
    curent_file_name = f"files {number}.txt"  # Создаем файлы
    with open(curent_file_name, 'w', encoding="utf-8") as file:  # Записываем файлы
        file.write(f"Содержимое файла {curent_file_name}")
    print(f"Файл {curent_file_name} создан")


def copy_file(client_path, credit_path):  # Копируем файлы в файл for_buh.txt
    try:
        with open(client_path, 'r', encoding="utf-8") as client_file:
            content = client_file.read()
        with open(credit_path, 'a', encoding="utf-8") as credit_file:
            credit_file.write(content + '\n')  # Добавляем символ новой строки
        print(f"Скопированы данные из {client_path} в {credit_path}.")
    except IOError:
        print("Ошибка при копировании файла")


buh_file = "for_buh.txt"

file_list = sorted([file for file in os.listdir(folder_path) if file.endswith('.txt')],
                   key=lambda x: int(x.split(".")[0]))

for file_name in file_list:
    client_file_path = os.path.join(folder_path, file_name)
    copy_file(client_file_path, buh_file)
