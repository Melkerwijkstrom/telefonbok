import json


class Telefonbok:
    def __init__(self, fil="telefonbok.json"):
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
        nummer = input("skriv nummer: ")

        if namn in self.kontakter:
            print("den personen finns redan")
        else:
            self.kontakter[namn] = nummer
            self.spara()
            print("kontakt sparad")

