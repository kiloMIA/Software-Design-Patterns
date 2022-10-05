from decorator import *
from component import *
from clothes import *

if __name__ == "__main__":
    person = Person()
    print("Client: I've got a person: ")
    executor(person)
    print("\n")

    kurtka = Kurtka(person)
    print("Client: Now I've got a decorated person:")
    executor(kurtka)