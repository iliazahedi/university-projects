# دریافت عدد از کاربر
Number = int(input("yek adad vared kon"))

# بررسی پالیندروم بودن عدد (برابری عدد با معکوسش)
if str(Number) == str(Number)[::-1]:
    print("its palindrome")
else:
    print("its not palindrome")