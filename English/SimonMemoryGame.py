import random
import time
import string

colors = ["Red", "Green", "Blue", "Yellow"]

def display_sequence(sequence):
    for color in sequence:
        print(color)
        time.sleep(1)  
        print("\033c", end="")  

def check_user_input(sequence):
    user_input = []
    for i in range(len(sequence)):
        user_color = input(f"Repeat color {i+1}: ").capitalize()
        user_input.append(user_color)
    
    return user_input == sequence

def trigger_easter_egg():
    print("\033c", end="")  
    print("🎉 Congratulations! You have triggered a secret Easter Egg! 🎉")
    time.sleep(1)

    print("\n[SYSTEM ERROR]: Memory has been corrupted...")
    time.sleep(0.5)

    for _ in range(50):  
        print(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=50)))
        time.sleep(0.1)

    print("\033c", end="")  
    print("Everything seems to be returning to normal... or almost.")
    time.sleep(1)
    print("Keep playing, and remember, the game may still be... defective.")

def simon_game():
    sequence = []
    score = 0

    print("Welcome to the Simon Game!")
    time.sleep(1)
    
    while True:
        sequence.append(random.choice(colors))
        
        # Easter egg trigger if the sequence contains "Red", "Green", "Blue", "Yellow"
        if sequence == ["Red", "Green", "Blue", "Yellow"]:
            trigger_easter_egg()

        print("\033c", end="")  # Clear the screen
        print("Here is the sequence to reproduce:")
        display_sequence(sequence)

        print("Repeat the sequence in the same order.")
        if not check_user_input(sequence):
            print(f"You made a mistake. Your score is {score}.")
            break
        
        score += 1
        print(f"Well done! Your current score is {score}.")
        time.sleep(1)

if __name__ == "__main__":
    simon_game()