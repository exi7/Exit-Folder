import random
import time
import string

colors = ["Rouge", "Vert", "Bleu", "Jaune"]

def display_sequence(sequence):
    for color in sequence:
        print(color)
        time.sleep(1)  
        print("\033c", end="")  

def check_user_input(sequence):
    user_input = []
    for i in range(len(sequence)):
        user_color = input(f"Reproduisez la couleur {i+1}: ").capitalize()
        user_input.append(user_color)
    
    return user_input == sequence

def trigger_easter_egg():
    print("\033c", end="")  
    print("🎉 Félicitations ! Vous avez déclenché un Easter Egg secret ! 🎉")
    time.sleep(1)

    
    print("\n[ERREUR SYSTÈME]: La mémoire a été corrompue...")
    time.sleep(0.5)

    for _ in range(50):  
        print(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=50)))
        time.sleep(0.1)

    print("\033c", end="")  
    print("Tout semble revenir à la normale... ou presque.")
    time.sleep(1)
    print("Continuez à jouer, et n'oubliez pas, le jeu est peut-être toujours... défectueux.")

def simon_game():
    sequence = []
    score = 0

    print("Bienvenue dans le jeu Simon !")
    time.sleep(1)
    
    while True:
        sequence.append(random.choice(colors))
        
        # Déclenchement de l'easter egg si la séquence contient "Rouge", "Vert", "Bleu", "Jaune"
        if sequence == ["Rouge", "Vert", "Bleu", "Jaune"]:
            trigger_easter_egg()

        print("\033c", end="")  # Clear the screen
        print("Voici la séquence à reproduire :")
        display_sequence(sequence)

        print("Reproduisez la séquence dans le même ordre.")
        if not check_user_input(sequence):
            print(f"Vous avez fait une erreur. Votre score est {score}.")
            break
        
        score += 1
        print(f"Bravo ! Votre score actuel est {score}.")
        time.sleep(1)

if __name__ == "__main__":
    simon_game()
