# دریافت عدد اول
num1 = float(input("adad aval ro vared kon: "))

# دریافت عدد دوم
num2 = float(input("adad dovom ra vared kon: "))

# دریافت عملگر ریاضی
operation = input("amaliat ro vared kon (+, -, *, /): ")

# محاسبه نتیجه
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:  # جلوگیری از تقسیم بر صفر
        result = num1 / num2
    else:
        result = "khata! tathim bar 0 momken nist."
else:
    result = "amaliat motabar nist!."

# نمایش نتیجه
print("natije:", result)