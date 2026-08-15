from .person import Person
from .pedigree import Pedigree

Mujtba = Person("Mujtaba Abbas","p1","M",False,"p2","p3")
Raza = Person("Raza Abbas","p3","M",False,)
Shabeeh = Person("Shabeeh Zehra","p2","F",False)
fake = Person("fake","p1","M",True)

ped = Pedigree()
ped.add_person(Mujtba)
ped.add_person(Raza)
ped.add_person(Shabeeh)



print(len(ped))
print(ped.get_person("p3").name)
print(ped.get_person("p2").name)
ped.get_person("p99")

