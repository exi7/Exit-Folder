
import unicodedata

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = ''.join(c for c in texte if c.isalpha() or c.isspace())
    texte = ''.join(unicodedata.normalize('NFKD', c).encode('ASCII', 'ignore').decode('utf-8') for c in texte)
    return texte

def compter(lettre, texte):
    return texte.count(lettre)

def frequences(texte):
    texte = nettoyer_texte(texte)
    total_lettres = sum(1 for c in texte if c.isalpha())
    
    if total_lettres == 0:
        print("Aucune lettre trouvée dans le texte.")
        return
    
    print(f"\nNombre total de lettres : {total_lettres}\n")
    
    for lettre in "abcdefghijklmnopqrstuvwxyz":
        nombre = compter(lettre, texte)
        pourcentage = (nombre / total_lettres) * 100 if total_lettres > 0 else 0
        print(f"{lettre.upper()} : {nombre} ({pourcentage:.2f} %)")

if __name__ == "__main__":
    texte = input("Saisissez un texte : ")
    frequences(texte)