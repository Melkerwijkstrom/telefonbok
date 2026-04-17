import json


class Telefonbok:
    def init(self, fil="telefonbok.json"):
        self.fil = fil
        self.kontakter = self.ladda()

  
    def ladda(self):
        try:
            with open(self.fil, "r") as f:
                return json.load(f)
        except:
          
            return {}

    
    def spara(self):
        with open(self.fil, "w") as f:
            json.dump(self.kontakter, f, indent=4)

    def lägg_till(self):
        namn = input("skriv namn: ")
        nummer = input("skriv nummer ")

        if namn in self.kontakter:
            print("den personen finns redan")
        else:
            self.kontakter[namn] = nummer
            self.spara()
            print("kontakt sparad")
            
        def sök(self):
            namn = input("vem vill du söka efter ")
        if namn in self.kontakter:
            print(self.kontakter[namn])
        else:
            print("hittar inte kontakten")

    def uppdatera(self):
        namn = input("vilken kontakt vill du ändra ")
        if namn in self.kontakter:
            nytt = input("skriv nytt nummer: ")
            self.kontakter[namn] = nytt
            self.spara()
            print("uppdaterat")
        else:
            print("finns inte")

    def ta_bort(self):
        namn = input("vem ska tas bort: ")
        if namn in self.kontakter:
            del self.kontakter[namn]
            self.spara()
            print("borttagen")
        else:
            print("finns inte")

    def meny(self):
        while True:
            print("\n1 lägg till")
            print("2 sök")
            print("3 uppdatera")
            print("4 ta bort")

            val = input("välj: ")
            print("uppdaterat")
        else:
            print("finns inte")

    def ta_bort(self):
        namn = input("vem ska tas bort: ")
        if namn in self.kontakter:
            del self.kontakter[namn]
            self.spara()
            print("borttagen")
        else:
            print("finns inte")

    def meny(self):
        while True:
            print("\n1 lägg till")
            print("2 sök")
            print("3 uppdatera")
            print("4 ta bort")

            val = input("välj: ")


