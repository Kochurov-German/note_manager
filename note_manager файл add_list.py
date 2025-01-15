from greetings import username, content, status, created_date, issue_date, title

username = input('Введите имя пользователя: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки (например, "Активна", "Выполнена"): ')
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дату истечения заметки в формате "день-месяц-год": ')

titles = []
for i in range(5):
    title = input(f"Введите заголовок заметки {i + 1}")
    titles.append(title)

print('\nВы ввели следующие данные: ')
print('Имя пользователя: ', username)
print('Заголовки заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки: ',issue_date)