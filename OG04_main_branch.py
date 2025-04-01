# Напишите программу, которая выводит случайное число от 1 до 100 (используйте модуль random).

import random # Импортируем модуль random

# Генерируем случайное число от 1 до 100
def true_number():
    true_number = random.randint(1, 100)
    print("Компьютер загадал число от 1 до 100. Попробуйте угадать!")

    while True:
        try:
            user_number = int(input("Введите ваше предположение:")) # Запрашиваем у пользователя число

            if user_number < true_number:
                print("Загаданное число больше. Попробуйте еще раз.")
            elif user_number > true_number:
                print("Загаданное число меньше. Попробуйте еще раз.")
            else:
                print("Поздравляем! Вы угадали число!")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

true_number() # Запускаем игру