import os
import time

def run_script(script_name):
    os.system(f'python {script_name}')

def menu():
    while True:
        print("""
              ▓█████ ▒██   ██▒ ██▓▄▄▄█████▓     █████▒▒█████   ██▓    ▓█████▄ ▓█████  ██▀███  
              ▓█   ▀ ▒▒ █ █ ▒░▓██▒▓  ██▒ ▓▒   ▓██   ▒▒██▒  ██▒▓██▒    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
              ▒███   ░░  █   ░▒██▒▒ ▓██░ ▒░   ▒████ ░▒██░  ██▒▒██░    ░██   █▌▒███   ▓██ ░▄█ ▒
              ▒▓█  ▄  ░ █ █ ▒ ░██░░ ▓██▓ ░    ░▓█▒  ░▒██   ██░▒██░    ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
              ░▒████▒▒██▒ ▒██▒░██░  ▒██▒ ░    ░▒█░   ░ ████▓▒░░██████▒░▒████▓ ░▒████▒░██▓ ▒██▒
              ░░ ▒░ ░▒▒ ░ ░▓ ░░▓    ▒ ░░       ▒ ░   ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
              ░ ░  ░░░   ░▒ ░ ▒ ░    ░        ░       ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
              ░    ░    ░   ▒ ░  ░          ░ ░   ░ ░ ░ ▒    ░ ░    ░ ░  ░    ░     ░░   ░ 
              ░  ░ ░    ░   ░                         ░ ░      ░  ░   ░       ░  ░   ░     
------------------------------------------------------------------------------------------------------------------------https://github.com/exi7 | https://github.com/exi7 | https://github.com/exi7 | https://github.com/exi7 | https://github.c\n------------------------------------------------------------------------------------------------------------------------\n{w}
 ┌                                                                                              
 ├           ┌─────────────────┐       
 └─┬─────────┤      Folder     │
   │         └─────────────────┘         
   ├─ [1] Letter frequency in a text
   ├─ [2] List of prime numbers
   ├─ [3] Spiral numbers
   ├─ [4] Simon Game
   └─ [0] Exit the program.                                                                 ░                      """)
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            run_script("LetterFrequencyAnalyzer.py")
        elif choice == '2':
            run_script("PrimeNumberFinder.py")
        elif choice == '3':
            run_script("SpiralNumberGenerator.py")
        elif choice == '4':
            run_script("SimonMemoryGame.py")
        elif choice == '0':
            print("Thank you for using the program!")
            time.sleep(1)
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu()
