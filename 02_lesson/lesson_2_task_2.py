year = int(input("Введите год:"))


def is_year_leap(year):
    if year % 4 == 0:
        print("Високосный год")

    else:
        print("Обычный год")


is_year_leap(year)
