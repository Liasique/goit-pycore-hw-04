#TODO

# 1 Open the file using with open(path, "r", encoding="utf-8")
def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            # 2 Loop through each line with for line in file:
            for line in file:
                line = line.strip()  # remove spaces and \n from the line
                # 3 Split the line by comma → line.split(',')
                name, salary_str = line.split(',')  # split the line into name and salary
                # 4 convert salary into → int()
                salary = int(salary_str)
                print(name, salary) 
            pass
    except FileNotFoundError:
        print("File didnt find.")
        #call function
total_salary("task1/text.py")


# 5 Add all salaries together and count how many

# 6 Return the total and average as a tuple → (total, average)

# 7 Use try...except to catch file errors or wrong data



'''
Завдання 1

У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Наприклад:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.



Вимоги до завдання:

Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


Рекомендації для виконання:

Використовуйте менеджер контексту with для читання файлів.
Пам'ятайте про встановлення кодування при відкриті файлів
Для розділення даних у кожному рядку можна застосувати метод split(',').
Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.


Критерії оцінювання:

Функція повинна точно обчислювати загальну та середню суми.
Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
Код має бути чистим, добре структурованим і зрозумілим.


Приклад використання функції:

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

Очікуваний результат:

Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000


'''