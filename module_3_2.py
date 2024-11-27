# Задача "Рассылка писем"

def  send_email(message, recipient, *,sender = "university.help@gmail.com"):
    #print(recipient,sender)
    r1 = recipient.endswith(('.com', '.ru', '.net')) #Метод endwith() возвращает True, если строка заканчивается указанным суффиксом
    #print(r1)
    r2 = sender.endswith(('.com', '.ru', '.net')) #Метод endwith() возвращает True, если строка заканчивается указанным суффиксом
    #print(r2)
    if r1 and r2: #true
        if "@" not in recipient and sender:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient} >>@ нет")
            return
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} >>не верны расширения')
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        return


#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')