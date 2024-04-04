class pangakonto:
    def __init__(self, kontoSeis, omanikNimi):
        self.kontoSeis = kontoSeis
        self.omanikNimi = omanikNimi

    def raha_lisamine(self, summa):
        if summa > 0:
            self.kontoSeis += summa
            print(f"{summa} eurot lisati kontole")
        else:
            print("Negatiivset summat ei aa lisada kontole")

    def raha_valjavotmine(self, summa):
        if summa > 0:
            if self.kontoSeis >= summa:
                self.kontoSeis -= summa
                print(f"{summa} eurot voeti kontolt nahui")
            else:
                print("Kontol pole piisavalt raha")
        else:   
                print("negatiivset summat ei saa kontolt valja votta")
konto1=pangakonto(500, "kencarson")
konto2=pangakonto(1000, "destroy")
konto1.raha_lisamine(200)
konto1.raha_valjavotmine(50)
konto2.raha_lisamine(500)
konto2.raha_valjavotmine(350)

