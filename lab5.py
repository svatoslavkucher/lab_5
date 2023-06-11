# Імпортуємо необхідний пакет
from num2words import num2words

# Вітання користувача
print("Привіт! Ця програма перетворює числа на словесні представлення.")

# Запитуємо номер від користувача
number = input("Введіть число: ")

# Перевіряємо, чи введено число
if number.isdigit():
    # Перетворюємо число на словесне представлення
    number_in_words = num2words(int(number), to='cardinal')
    # Виводимо словесне представлення числа
    print("Словесне представлення числа {}: {}".format(number, number_in_words))
else:
    # Виводимо повідомлення про некоректний ввід
    print("Введено некоректне число. Будь ласка, введіть число.")