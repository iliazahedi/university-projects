# ساختن یک لیست خالی برای اعداد زوج
even_numbers = []

# حلقه از ۱ تا ۱۰۰
for number in range(1, 101):
    if number % 2 == 0:
        even_numbers.append(number)

# چاپ لیست اعداد زوج
print(even_numbers)
