import random

# انتخاب یک عدد تصادفی بین ۱ تا ۱۰۰
number = random.randint(1, 100)

# شمارنده برای تعداد حدس‌ها
guess_count = 0

print("A random number between 1 and 100 has been selected! Try to guess it!")

while True:
    guess = int(input("Your guess: "))  # دریافت حدس کاربر و تبدیل به عدد صحیح
    guess_count += 1  # افزایش شمارنده حدس

    if guess < number:
        print("Too small!")

    elif guess > number:
        print("Too big!")

    else:
        print(f"Congratulations! You guessed it right! The number was {number}!")
        print(f"Total guesses: {guess_count}")
        break