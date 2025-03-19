def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nombres_premiers(limite):
    return [n for n in range(2, limite + 1) if est_premier(n)]

if __name__ == "__main__":
    limite = int(input("Saisissez une limite : "))
    premiers = nombres_premiers(limite)
    print(f"Les nombres premiers de 2 à {limite} sont : {', '.join(map(str, premiers))}")