# ======================================
#     class pro Hráče, Duchy, body
# ======================================
class Hrac:
    def __init__(self, jmeno, hp, killskore, skore):
        self.jmeno = jmeno
        self.skore = skore
        self.hp    = hp 
        self.killskore = killskore
           
        if self.hp < 0:
                raise ValueError("HP hráče nemůže být záporné.")

    def __str__(self):
        return f"packman {self.jmeno} | HP: {self.hp} | skore: {self.skore} | kill skore: {self.killskore}"

    def bod(self):
        self.skore += 1
        print(f"{self.jmeno} snědl bod! Skóre: {self.skore}")
    def megabod(self):
        self.skore += 50
        print(f"{self.jmeno} snědl mega bod! Skóre: {self.skore}")

    
 #hráč = vygenerovány životy,jmeno, skore, kill skore(počet zabití ducha)

class Duch: 
    def __init__(self, jmeno, hp, demage):
        self.jmeno = jmeno
        self.hp    = hp
        self.demage= demage
    def __str__(self):
        return f"duch {self.jmeno} | HP: {self.hp}"
    def utok(self):
        if hrac.hp > 1 : 
            hrac.hp -= 1
            print(f"nyní máš {hrac.hp}")
        else:
            print(f"hra skončila se skorem {hrac.skore}")
    
#duch = vygenerovány životy, jmeno
class Bod: 
    def __init__(self, hp, jmeno):
        self.jmeno  = jmeno    
        self.hp     = hp 
    def __str__(self):
        return f"bod {self.jmeno} | HP: {self.hp}"
#bod = skore pro hráče 
class Megabod: 
    def __init__(self, hp, jmeno):
        self.jmeno  = jmeno    
        self.hp     = hp 
    def __str__(self):
        return f"megabod {self.jmeno} | HP: {self.hp}"
#mega bod = skore pro hráče 

# ======================================
#             HRÁČ SNÍ BOD
# ======================================

if hrac.hp > 0 and bod.hp > 0:

    # bod je sněden
    bod.hp = 0

    # přidání score
    hrac.skore += 1

    print(f"{hrac.jmeno} snědl bod!")

    print(f"Skóre hráče: {hrac.skore}")
# ======================================
#          HRÁČ SNÍ MEGA BOD
# ======================================

if hrac.hp > 0 and megabod.hp > 0:

    # mega bod je sněden
    megabod.hp = 0

    # přidání score
    hrac.skore += 50

    print(f"{hrac.jmeno} snědl mega bod!")

    print(f"Skóre hráče: {hrac.skore}")
# ======================================
#        DUCH MŮŽE SNÍST HRÁČE
#    jen když hráč nesnědl megabod
# ======================================

if megabod.hp > 0:

    # duch sní hráče
    hrac.hp -= duch.demage

    print(f"{duch.jmeno} snědl hráče {hrac.jmeno}!")

    print(f"HP hráče: {hrac.hp}")

else:

    print(f"{hrac.jmeno} má nesmrtelnost!")
# ======================================
#            HRÁČ SNÍ DUCHA
#          když snědl megabod
#           a dostane score
# ======================================

if megabod.hp <= 0:

    # hráč sní ducha
    duch.hp -= 100

    # kill score
    hrac.killskore += 1

    # přidání score
    hrac.skore += 100

    print(f"{hrac.jmeno} snědl ducha {duch.jmeno}!")

    print(f"Score hráče: {hrac.skore}")

    print(f"Kill score: {hrac.killskore}")
else:

    print(f"{hrac.jmeno} nemá megabod!")


hrac = Hrac("packman", 5)
duch1 = Duch("duch1", 1, 1)
duch2 = Duch("duch1", 1, 1)
duch3 = Duch("duch1", 1, 1)
