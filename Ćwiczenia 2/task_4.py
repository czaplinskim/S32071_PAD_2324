class Pojazd:
    def __init__(self, predkosc_max, przebieg, model):
        self.przebieg = przebieg
        self.predkosc_max = predkosc_max
        self.model = model

    def liczba_miejsc(self, miejsca):
        return f"{self.model} pomieści {miejsca} osób"

    def opłata(self, miejsca):
        return miejsca * 100

class Autobus(Pojazd):
    def liczba_miejsc(self, miejsca=50):
        return super().liczba_miejsc(miejsca)

    def opłata(self, miejsca=50):
        podstawowa_opłata = super().opłata(miejsca)
        return podstawowa_opłata + 0.1 * podstawowa_opłata