
# ! WAP for polymerphrism for multiple Animal like Dog,Cat etc which produce sounds like Dog "Woof" or "Meaow"



class Animal:
    def speak(self):
        return "Sounding......"
    
class Dog(Animal):
    def speak(self):
        return "Dog Sounds:Woof"

class Cat(Animal):
    def speak(self):
        return "Cat sounds:Meowwww"
    
for i in [Animal() ,Dog(),Cat()]:
    print(i.speak())
