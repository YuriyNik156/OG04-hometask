def find_max_of_three():
    print("Введите три числа:")
    try:
        # Запрашиваем три числа у пользователя
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        num3 = float(input("Введите третье число: "))

        # Находим наибольшее число
        max_num = max(num1, num2, num3)

        print(f"Наибольшее число: {max_num}")
    except ValueError:
        print("Пожалуйста, вводите только числа.")


# Запускаем программу
find_max_of_three()