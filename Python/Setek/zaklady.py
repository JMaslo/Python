class Person:

    def __init__(self, name: str, age: int, height: int, weight: float):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.amount_of_steps = 1000 #Počet kroků do odpočinutí

    def walk(self):
        print(f"{self.name} udělal krok vpřed")
        self.amount_of_steps -= 1

    def speak(self):
        return "Ahoj, jak se máš?" 

    def write_out_info(self): #Vypíše informace o daném člověku
        print(f"Ahoj, já jsem {self.name}, je mi {self.age} let, měřím {self.height} cm a vážím {self.weight} kilogramů")  

pepik = Person("Pepa", 25, 170, 75,)
honzik = Person("Honza", 23, 185, 87)

for ukony in range(3):
    honzik.walk()
    print(honzik.amount_of_steps)

info_of_person = input("O jakém člověku chcete vypsat informace? Pepik/Honzik - Dodržujte formát!\n")
if info_of_person == "Pepik":
    print(pepik.write_out_info())
elif info_of_person == "Honzik":
    print(honzik.write_out_info())   
else:
    print("Špatná odpověd! Zkuste to znovu. Zvolte mezi: Pepik nebo Honzik")