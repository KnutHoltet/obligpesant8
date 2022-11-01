from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f"\n\nGenerasjonsnummer: {self._generasjonsnummer}\nAntall levende celler: {self._rutenett.antall_levende()}\n")



    def oppdatering(self):
        #Teller levende naboer for hver celle
        alle_celler = self._rutenett.hent_alle_celler()
        for celler in alle_celler:
            celler.tell_levende_naboer()
        
        for celler in alle_celler:
            celler.oppdater_status()

        
               
        self._generasjonsnummer += 1

