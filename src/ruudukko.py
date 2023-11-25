class Ruudukko:
    def __init__(self):
        self.ruudukko = ["-"] * 20

        for x in range(20):
            self.ruudukko[x] = ["-"] * 20

    def tulosta_ruudukko(self):
        print("   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20")
        rivi = 1
        for i in range(20):
            if rivi <= 9:
                print(f"{rivi}  {'  '.join(self.ruudukko[i])}")
            else:
                print(f"{rivi} {'  '.join(self.ruudukko[i])}")
            rivi += 1
