# Пользователь вводит число, программа должна вычислить сумму его цифр.

def sum_of_digits():
    try:
        # Запрашиваем ввод числа у пользователя
        number = input("Введите число: ")

        # Убираем возможный знак "-" и проверяем, является ли ввод числом
        if number.startswith('-'):
            number = number[1:]

        if not number.isdigit():
            print("Пожалуйста, введите корректное число.")
            return

        # Преобразуем строку в список цифр и вычисляем их сумму
        digit_sum = sum(int(digit) for digit in number)

        print(f"Сумма цифр числа: {digit_sum}")
    except ValueError:
        print("Произошла ошибка. Убедитесь, что вы вводите число.")


# Запускаем функцию
sum_of_digits()