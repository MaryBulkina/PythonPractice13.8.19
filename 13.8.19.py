tickets = int(input("Введите количество билетов"))
visitors = tickets

sum = 0

while visitors != 0:
    age_for_visitors = int(input(f"Укажите возраст посетителя {visitors}"))
    if age_for_visitors < 18:
        print("Вход бесплатный")
    elif 25 > age_for_visitors >= 18:
        sum += 990
        print("Стоимость билета составляет 990 рублей")
    elif 120 > age_for_visitors >= 25:
        sum += 1390
        print("Стоимость билета составляет 1390 рублей")
    else:
        print("Введены некорректные данные, повторите ввод данных")
        continue
    visitors -= 1

if tickets > 3:
    sale = sum - ((sum / 100) * 10)
    print(f"Сумма к оплате, с учетом скидки 10% за покупку 3х и более билетов, составляет {sale} рублей.")
else:
    print(f"Сумма к оплате составляет {sum} рублей.")
