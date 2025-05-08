def bakery():
    print("👨‍🍳 Baker: Hi! What's your name?")
    name = input("You: ")

    print(f"👨‍🍳 Baker: Welcome, {name}! Please enter your 16-digit card number:")
    card_number = input("Card number: ")

    # Check if card number has exactly 16 digits and only digits
    if not (card_number.isdigit() and len(card_number) == 16):
        print("❌ Invalid card number! It must be exactly 16 digits.")
        return

    # Get password twice and check match
    password1 = input("Card password (first time): ")
    password2 = input("Card password (second time): ")

    if password1 != password2:
        print("❌ Passwords do not match! Try again.")
        return

    print("✅ Password accepted!")

    # Bread prices in Toman
    prices = {
        "sangak": 8000,
        "barbari": 6000,
        "taftoon": 4000,
        "lavash": 2000
    }

    total_price = 0

    while True:
        print("👨‍🍳 What kind of bread would you like? (sangak, barbari, taftoon, lavash)")
        bread_type = input("Bread type: ").strip().lower()

        if bread_type not in prices:
            print("❌ Invalid bread type! Please choose from the list.")
            continue

        print("How many breads do you want?")
        try:
            count = int(input("Bread quantity: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        cost = prices[bread_type] * count
        total_price += cost

        print(f"✅ {count} {bread_type} bread(s) ready for {name}. 🍞 Cost: {cost} Toman")

        again = input("Do you want more bread? (yes/no): ").strip().lower()
        if again != "yes":
            break

    print(f"🧾 {name}, your total payment is: {total_price} Toman. Thank you for your purchase! 🥖")

# Run the program
bakery()
