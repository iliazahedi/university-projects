import random

# Price per pound in GBP
PRICE_PER_POUND = 1.2  

# Conversion factor (1 pound = 0.453592 kg)
POUND_TO_KG = 0.453592

# Possible prizes
PRIZES = [
    "Fishing Hook",
    "Fishing Bucket",
    "Fishing Hat",
    "Fishing Boat",
    "Fishing Outfit",
    "Fishing Bait"
]

def fish_game():
    max_weight = 0  # To store the heaviest fish
    
    while True:
        input("\nThe fisherman is fishing... (Press Enter)")
        
        # Random fish weight between 1 and 120 pounds
        fish_weight_pound = random.randint(1, 120)
        fish_weight_kg = fish_weight_pound * POUND_TO_KG
        
        print(f"\nThe fisherman caught a fish weighing {fish_weight_pound:.2f} pounds!")
        print(f"Fish weight in kilograms: {fish_weight_kg:.2f} kg")
        
        # Calculate payment
        if fish_weight_kg > 50:
            payment = fish_weight_pound * PRICE_PER_POUND * 2
            print("Big fish! Payment is doubled!")
        else:
            payment = fish_weight_pound * PRICE_PER_POUND
            
        print(f"Payment to fisherman: £{payment:.2f}")
        
        # Check weight record
        if fish_weight_kg > max_weight:
            max_weight = fish_weight_kg
            print("\nNew record! You win prizes!")
            
            # Select 4 random prizes
            selected_prizes = random.sample(PRIZES, 4)
            print("Your prizes:")
            for i, prize in enumerate(selected_prizes, 1):
                print(f"{i}. {prize}")
        else:
            print("\nFish weight is less than previous record. No prizes.")
        
        # Ask to continue
        choice = input("\nContinue fishing? (yes/no): ").lower().strip()
        if choice != 'yes':
            print("Game over!")
            break

# Start game
print("=== FISHING GAME ===")
fish_game()
