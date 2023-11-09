class Ruudukko:
    def __init__(self):
        self.ruudukko = ["-"] * 20

        for x in range(20):
            self.ruudukko[x] = ["-"] * 20

    def tulosta_ruudukko(self):
        print("   A B C D E F G H I J K L M N O P Q R S T")
        rivi = 1
        for i in range(20):
            if rivi <= 9:
                print(f"{rivi}  {' '.join(self.ruudukko[i])}")
            else:
                print(f"{rivi} {' '.join(self.ruudukko[i])}")
            rivi += 1
