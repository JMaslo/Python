class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ukony_do_opravy = 1000
        self.mluveni = "Ahoj"

    def krok_vpred(self):
        print("Robot udělal krok vpřed")
        self.ukony_do_opravy -= 1

    def krok_vzad(self):
        print("Robot udělal krok vzad")
        self.ukony_do_opravy -= 1      

    def speak(self):
        return self.mluveni

pes_pepik = Dog("Pepík", 5)
pes_honzik = Dog("Honzik", 8)
for i in range(2):
    pes_honzik.krok_vpred()
    pes_pepik.krok_vzad()
print(pes_honzik.ukony_do_opravy)
print(pes_honzik.mluveni)