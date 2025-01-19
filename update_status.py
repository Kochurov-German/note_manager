from datetime import datetime

def main():
    # Список возможных статусов
    statuses = ["выполнено", "в процессе", "отложено"]

    # Запрашиваем дату выполнения заметки с обработкой ошибок
    while True:
        issue_date_str = input("Введите дату выполнения заметки в формате ГГГГ-ММ-ДД: ")
        try:
            issue_date = datetime.strptime(issue_date_str, "%Y-%m-%d")
            break  # Если дата введена правильно, выходим из цикла
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")

    # Проверяем, истек ли срок выполнения заметки
    current_date = datetime.now()
    if current_date > issue_date:
        print("Предупреждение: Дедлайн заметки истек!")

    # Запрашиваем у пользователя текущий статус
    current_status = input("Введите текущий статус заметки: ")
    print(f"Текущий статус заметки: {current_status}")

    # Запрос на изменение статуса
    while True:
        print("\nДоступные статусы:")
        print("1 - выполнено")
        print("2 - в процессе")
        print("3 - отложено")

        new_status_input = input("Введите номер нового статуса заметки или введите статус текстом "
                                 "(или оставьте пустым для завершения): ").strip()

        if new_status_input == "":
            # Если пользователь оставил ввод пустым, завершаем программу
            print("Завершение программы.")
            return

        # Проверяем, введен ли статус в текстовом формате
        if new_status_input in statuses:
            current_status = new_status_input
            print(f"Статус заметки обновлен на: {current_status}")
            break
        elif new_status_input in ["1", "2", "3"]:
            # Если введенный номер статуса корректный, обновляем статус
            new_status = statuses[int(new_status_input) - 1]
            current_status = new_status
            print(f"Статус заметки обновлен на: {current_status}")
            break
        else:
            # Если статус некорректный, сообщаем об этом и повторяем запрос
            print("Некорректный ввод. Пожалуйста, выберите номер статуса из списка или введите статус текстом.")

    # Выводим обновленный статус
    print(f"\nОбновленный статус заметки: {current_status}")

if __name__ == "__main__":
    main()