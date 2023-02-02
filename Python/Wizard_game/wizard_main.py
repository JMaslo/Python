from Wizard_game.wizard_classes import WizardPlayer, HeadWizard, BadWizard  

harry = WizardPlayer("Harry", 18)
ron = WizardPlayer("Ron", 18)
hermiona = WizardPlayer("Hermiona", 18)
brumbal = HeadWizard("Brumbál", 75)
voldemort = BadWizard("Voldemort", 100)

def vitej(): # Uvítací zpráva
    safe_Hogwarts = '''
    Ahoj kouzelníku!

    Vítám Tě u mé hry, kde si zahraješ jaké to je chránit Bradavice :).

    Níže si vyber postavu, kterou bys chtěl být :).

    Hodně štěstí.
    '''
    return safe_Hogwarts

def vyber_charakteru(): # Výběr charakteru
    charakter = input("Výběr: Harry, Hermiona, Ron, Brumbál nebo Voldemort:\n") 
    if charakter == harry.name:
        print(harry.attack())
        question = input("Chcete zavolat někoho silnějšího? Ano/Ne\n")
        if question == "Ano":
            return brumbal.attack_2()
        else:
            return "Ne? Jak tím pádem chcete tuto bitvu vyhrát?" 
            
    elif charakter == hermiona.name:
        print(hermiona.attack())
        question = input("Chcete zavolat někoho silnějšího? Ano/Ne\n")
        if question == "Ano":
            return brumbal.attack_2() 
        else:
            return "Ne? Jak tím pádem chcete tuto bitvu vyhrát?" 

    elif charakter == ron.name:
        print(ron.attack())
        question = input("Chcete zavolat někoho silnějšího? Ano/Ne\n")
        if question == "Ano":
            return brumbal.attack_2()
        else:
            return "Ne? Jak tím pádem chcete tuto bitvu vyhrát?"    

    elif charakter == brumbal.name:
        return brumbal.attack_2()

    elif charakter == voldemort.name:
        return voldemort.expeliarmus()

    else:
        return "Nesprávný charakter, zkuste to znovu"  

def run_again(): # Spuštění programu znovu
    again = input("Chcete program spustit znovu? Odpovězte v tomto formáte: Ano/Ne\n")
    if again == "Ano":
        print(vitej())
        print(vyber_charakteru())
        print(run_again())
    elif again == "Ne":
        print("Děkujeme za spuštění programu, nashledanou.")
    else:
        print("Špatný formát!")

print(vitej())
print(vyber_charakteru())
run_again()  