ticket = int(input('Введите количество билетов: '))
itog = 0.0 #сумма билетов
ticketStandart = 1390 #возратная группа от 25 и выше
ticketJune = 990 #возрастная группа от 18 до 25
for i in range(ticket):
    age = int(input('Введите возраст: '))
    if 18 <= age < 25:
        itog = itog + ticketJune
    if age >= 25:
        itog = itog + ticketStandart

if ticket > 3:
    itog *= 0.9
print('Итого'+ ' ' + str(itog) + ' ' + 'рублей')
