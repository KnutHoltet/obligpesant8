from verden import Verden

def hovedprogram():
    rader = int(input("rader: "))
    kol = int(input("kol: "))
    verden = Verden(rader, kol)
    while True:
        verden.oppdatering()
        verden.tegn()
        valg = input("Gaa videre... ")
        if valg == "q":
            break




# starte hovedprogrammet
hovedprogram()
