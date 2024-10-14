import random

class Tablica:
    def __init__(self, n):
        self.n = n
        self.tablica = [0] * n

    def wypelnij(self, a, b):
        self.tablica = [random.randint(a, b) for _ in range(self.n)]

    def maksimum(self):
        return max(self.tablica)

    def minimum(self):
        return min(self.tablica)

    def maksimum2(self):
        max1, max2 = (self.tablica[0], self.tablica[1]) if self.tablica[0] > self.tablica[1] else (
        self.tablica[1], self.tablica[0])

        for i in range(2, self.n):
            if self.tablica[i] > max1:
                max2 = max1
                max1 = self.tablica[i]
            elif self.tablica[i] > max2 and self.tablica[i] != max1:
                max2 = self.tablica[i]
        return max2

    def znajdz(self, a):
        return self.tablica.index(a) if a in self.tablica else -1

    def __str__(self):
        return ' '.join(map(str, self.tablica))

def main():
    n = 10
    tablica = Tablica(n)

    tablica.wypelnij(1, 100)
    print("Tablica:", tablica)

    print("Maksimum:", tablica.maksimum())
    print("Minimum:", tablica.minimum())

    print("Drugie maksimum:", tablica.maksimum2())

    szukana_wartosc = 50
    indeks = tablica.znajdz(szukana_wartosc)
    if indeks != -1:
        print(f"Wartość {szukana_wartosc} znaleziona na indeksie {indeks}")
    else:
        print(f"Wartość {szukana_wartosc} nie została znaleziona w tablicy")

if __name__ == "__main__":
    main()