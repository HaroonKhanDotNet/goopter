# object oriented paradigm
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance vs Composition ('has a' relationship)
# 4. Polymorphism

# class
# __init__()
# self

class Thermostat:

    #initialization
    def __init__(self): self.temperature = None

    #setter
    def setTemp(self, temp): self.temperature = temp 

    #getter
    def getTemp(self): return self.temperature

    #temperature regulation
    def regulate(self, temp):
        if self.temperature < temp: print("Start cooling")
        elif self.temperature > temp: print("Start heating")
        else: print("Stop regulating")


thermo = Thermostat()
print(thermo.getTemp())
thermo.setTemp(21)
print(thermo.getTemp())
thermo.regulate(20)
thermo.regulate(22)
thermo.regulate(21)

thermo2 = Thermostat()
thermo2.setTemp(18)
thermo2.regulate(20)
thermo2.regulate(16)

