def main():
    titles = []  # Список для хранения заголовков заметок

    while True:
        title = input("Введите заголовок (или оставьте пустым для завершения): ")
        if title == "":  # Если пользователь ввел пустую строку, завершаем цикл
            break
        titles.append(title)  # Добавляем заголовок в список

    # Выводим список заголовков
    print("\nЗаголовки заметки:")
    for title in titles:
        print(f"- {title}")

if __name__ == "__main__":
    main()