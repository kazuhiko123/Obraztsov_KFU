if __name__ == "__main__":
    main()

class NotEnoughMoneyError(Exception):
    pass

def validate_name(name: str) -> str:
    if not name:
        raise ValueError("Имя не может быть пустым")
    return name.strip()

def validate_age(age: str) -> int:
    try:
        age_int = int(age)
    except ValueError:
        raise ValueError("Возраст должен быть числом")
    if age_int < 12:
        raise ValueError("Слишком маленький возраст")
    return age_int

def validate_tickets(count: str) -> int:
    try:
        tickets = int(count)
    except ValueError:
        raise ValueError("Некорректное количество билетов")
    if tickets <= 0 or tickets > 5:
        raise ValueError("Количество билетов должно быть от 1 до 5")
    return tickets

def validate_budget(budget: str) -> float:
    try:
        money = float(budget)
    except ValueError:
        raise ValueError("Некорректный бюджет")
    if money < 0:
        raise ValueError("Бюджет не может быть отрицательным")
    return money

def calculate_total(tickets: int) -> int:
    return tickets * 500

def main():
    print("Добро пожаловать в систему бронирования билетов!")
    print("Стоимость одного билета: 500 руб.")

    while True:
        try:
            name_input = input("Введите ваше имя: ")
            name = validate_name(name_input)
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

    while True:
        try:
            age_input = input("Введите ваш возраст: ")
            age = validate_age(age_input)
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

    while True:
        try:
            tickets_input = input("Введите количество билетов (макс. 5): ")
            tickets = validate_tickets(tickets_input)
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

    while True:
        try:
            budget_input = input("Введите сумму денег для оплаты: ")
            budget = validate_budget(budget_input)
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.\n")

    total = calculate_total(tickets)

    try:
        if budget < total:
            raise NotEnoughMoneyError(
                f"Недостаточно средств. Требуется: {total} руб., у вас: {budget} руб.")
    except NotEnoughMoneyError as e:
        print(f"\n{e}")
        return

    # Успешное бронирование
    change = budget - total
    print(f"Билеты успешно забронированы для {name}!")
    print(f"К оплате: {total} руб.")
    print(f"Внесено: {budget} руб. Сдача: {change} руб." if change > 0 else f"Внесено ровно {budget} руб.")
    print("Благодарим за покупку.")



