text = input("Please enter a text: ")

# تعریف شمارنده‌ها
letter_count = 0  # شمارنده حروف
digit_count = 0   # شمارنده اعداد

# بررسی هر کاراکتر در متن ورودی
for char in text:
    if char.isalpha():    # بررسی حرف بودن کاراکتر
        letter_count += 1
    elif char.isdigit():  # بررسی عدد بودن کاراکتر
        digit_count += 1

# نمایش نتایج شمارش
print("Letter count:", letter_count)
print("Digit count:", digit_count)