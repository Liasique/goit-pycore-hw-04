#TODO
    # 0. create cats.txt
	# 1. create function  get_cats_info(path)
	# 2. This function:
	# 	- takes the file path as input ( cats.txt)
	#   - reads each line from the file
	#   - splits each line with (,)
	#   - creates a dictionary with:
	#   	"id" = first part
	#   	"name" = second part
	#   	"age" = third part
	#   -  adds each dictionary to a list
	#   - returns the list of dictionaries


def get_cats_info(path):
    cats = []  # create empty list to store cat dictionaries

    try:
        with open(path, "r", encoding="utf-8") as file:  # open the file
            for line in file:  # go through each line
                # remove spaces and /n and split by comma
                cat_id, name, age = line.strip().split(',')

                # create dictionary for one cat
                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                # add this cat to the list
                cats.append(cat)

    except FileNotFoundError:
        print("File not found.")

    return cats 

#test
cats = get_cats_info("cats.txt")
print(cats)

'''
Завдання 2

У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.



Вимоги до завдання:

Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


Рекомендації для виконання:

Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.


Критерії оцінювання:

Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим.


Приклад використання функції:

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)



Очікуваний результат:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]



'''