class Duck:
    def talk (self):
        print("duck is talking")
    def walk(self):
        print("duck is walking")
class Dog:
    def talk(self):
        print("dog is talking")
class PetLover:
    def __init__(self,pet:Dog):
        self.pet =pet
    def play(self):
        self.pet.talk()
        self.pet.walk()

duck =Duck()
dog=Dog()
pet_lover = PetLover(dog)
pet_lover.play()