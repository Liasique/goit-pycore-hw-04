def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

#TERMINAL/
"""
(base) ➜  goit-pycore-hw-04 /usr/local/bin/python3 /Users/olga/Developer/GOIT/Projects/1.Python/goit-pycore-hw-04.git/goi
t-pycore-hw-04/task4/cli.py
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add Olga 123456
Contact added.
Enter a command: phone Olga
123456
Enter a command: change Olga 09877
Contact updated.
Enter a command: phone Olga
09877
Enter a command: all
Olga: 09877
Enter a command: heLLO
How can I help you?
Enter a command: exit
Good bye!
(base) ➜  goit-pycore-hw-04 git:(main) ✗ """





'''	
		Будь-який CLI складається з трьох основних елементів:

		Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків,
		  виділення з рядка ключових слів та модифікаторів команд.
		Функції обробники команд - набір функцій, які ще називають handler, 
		вони відповідають за безпосереднє виконання команд.
		Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача 
		даних та повернення користувачеві відповіді від функції - handler-а.
	
	
		1  бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер 
		телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг
         
		2  Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати
		  ім'я користувача, як ключ, і номер телефону як значення.


		Вимоги до завдання:

Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду 
та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних 
функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.


	"hello" → How can I help you?
		add [ім'я] [номер телефону] → Contact added.
		change [ім'я] [новий номер телефону] → Contact updated.
		phone [ім'я] → [номер телефону]
		all → усі збережені контакти з номерами телефонів
		exit → Good bye!
        
        
        
        
        def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

		if __name__ == "__main__":
    	main()
        
        
        Критерії оцінювання:

Бот повинен перебувати в нескінченному циклі, чекаючи команди користувача.
Бот завершує свою роботу, якщо зустрічає слова: "close" або "exit".
Бот не чутливий до регістру введених команд.
Бот приймає команди:
"hello", та відповідає у консоль повідомленням "How can I help you?"
"add username phone". За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл.
"change username phone". За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику.
"phone username" За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.
"all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!" та завершить своє виконання.
Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.
Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.

		'''