from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        noested_liste = []
        for i in range(self._ant_rader):
            noested_liste.append(self._lag_tom_rad())
        return noested_liste

    def _lag_tom_rad(self):
        liste = []
        for kolonner in range(self._ant_kolonner):
            liste.append(None)
        
        return liste

    def fyll_med_tilfeldige_celler(self):
        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                self.lag_celle(rad,kol)

                tilfeldig = randint(0,2)
                if tilfeldig == 1:    
                    self._rutenett[rad][kol].sett_levende()
            
    def lag_celle(self, rad, kol):
        celle = Celle()
        self._rutenett[rad][kol] = celle

    def hent_celle(self, rad, kol):
        if rad >= 0 and rad < self._ant_rader:
            if kol >= 0 and kol < self._ant_kolonner:
                return self._rutenett[rad][kol] 

    
    def tegn_rutenett(self):
        for rad in range(len(self._rutenett)):
            print("\n")
            for kol in range(len(self._rutenett[rad])):
                print(self._rutenett[rad][kol].hent_status_tegn(), end="")
                
        

    def _sett_naboer(self, rad, kol):
        cellen = self.hent_celle(rad, kol)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not(i == 0 and j == 0):
                    if self.hent_celle(rad + i, kol + j) is not None:
                        cellen.legg_til_nabo(self.hent_celle(rad + i, kol + j))           
      
    def koble_celler(self):
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
               self._sett_naboer(i, j)

    def hent_alle_celler(self):
        alle_celler = []
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                alle_celler.append(self.hent_celle(i, j))

        
        return alle_celler

    def antall_levende(self):
        antall_levende = 0
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                if self.hent_celle(i, j).er_levende():
                    antall_levende += 1

        return antall_levende