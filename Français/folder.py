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
   ├─ [1] Fréquence d'apparition d'une lettre dans un texte
   ├─ [2] Liste des nombres premiers
   ├─ [3] Nombres en spirale
   ├─ [4] Simon Game
   └─ [0] Quittes le programme.                                                                 ░                      """)
        
        choix = input("\nEntrez votre choix : ")
        
        if choix == '1':
            run_script("freq_lettres.py")
        elif choix == '2':
            run_script("nombres_premiers.py")
        elif choix == '3':
            run_script("spirale.py")
        elif choix == '4':
            run_script("simon.py")
        elif choix == '0':
            print("Merci d'avoir utilisé le programme !")
            time.sleep(1)
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()
