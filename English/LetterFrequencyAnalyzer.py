import unicodedata

def clean_text(text):
    text = text.lower()
    text = ''.join(c for c in text if c.isalpha() or c.isspace())
    text = ''.join(unicodedata.normalize('NFKD', c).encode('ASCII', 'ignore').decode('utf-8') for c in text)
    return text

def count(letter, text):
    return text.count(letter)

def frequencies(text):
    text = clean_text(text)
    total_letters = sum(1 for c in text if c.isalpha())
    
    if total_letters == 0:
        print("No letters found in the text.")
        return
    
    print(f"\nTotal number of letters: {total_letters}\n")
    
    for letter in "abcdefghijklmnopqrstuvwxyz":
        number = count(letter, text)
        percentage = (number / total_letters) * 100 if total_letters > 0 else 0
        print(f"{letter.upper()} : {number} ({percentage:.2f} %)")

if __name__ == "__main__":
    text = input("Enter a text: ")
    frequencies(text)
