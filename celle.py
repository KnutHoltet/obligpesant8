class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed" 
        self._naboer = []
        self._ant_levende_naboer = 0
    
    def sett_doed(self):
        self._status = "doed" 

    def sett_levende(self):
        self._status = "levende"

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def er_levende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hent_status(self):
        pass

    def hent_status_tegn(self):
        if self.er_levende():
            return "O"
        else:
            return "."

    def tell_levende_naboer(self):
        levendeCeller = []
        
        for celler in self._naboer:
            if celler.er_levende():
                levendeCeller.append(celler)
        
        self._ant_levende_naboer = len(levendeCeller)
       
    def oppdater_status(self):
        if self.er_levende():
            if self._ant_levende_naboer < 2 or self._ant_levende_naboer > 3:
                self.sett_doed()
        else:
            if self._ant_levende_naboer == 3:
                self.sett_levende()