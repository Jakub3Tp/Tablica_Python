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
        max_value = max(self.tablica)
        temp_tablica = [x for x in self.tablica if x != max_value]
        return max(temp_tablica) if temp_tablica else max_value

    def znajdz(self, a):
        return self.tablica.index(a) if a in self.tablica else -1

# Przykładowe użycie:
tablica = Tablica(10)
tablica.wypelnij(1, 100)
print("Tablica:", tablica.tablica)
print("Maksimum:", tablica.maksimum())
print("Minimum:", tablica.minimum())
print("Drugie maksimum:", tablica.maksimum2())
print("Indeks elementu 50:", tablica.znajdz(50))
