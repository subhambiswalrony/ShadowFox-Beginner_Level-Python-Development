'''

1.Avengers is a Marvel’s American Superheroes team, Now you want to showcase your programming skills by
  representing the Avengers team using classes. Create a class called Avenger and create these six
  superheroes using this class.
2. super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
3. Your Avenger class should have these properties:
    1. Name
    2. Age
    3. Gender
    4. Super Power
    5. Weapon
4. Captain America has Super strength, Iron Man has Technology, Black Widow is superhuman,
   Hulk has Unlimited Strength, Thor has super Energy and Hawkeye has fighting skills as superpowers.
5. Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and Arrows
6. Create methods to get the information about each superhero
7. Create a method is_leader() which will tell if the superhero is a leader or not.

'''


class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return f"{self.name} ({self.age} years old, {self.gender}): {self.super_power}, Weapon: {self.weapon}"

    def is_leader(self):
        return self.name in ["Captain America", "Iron Man", "Black Widow", "Thor"]


captain_america = Avenger("Captain America", 100, "Male", "Super strength", "Shield")
iron_man = Avenger("Iron Man", 45, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 40, "Male", "Fighting skills", "Bow and Arrows")

print(captain_america.get_info())
print(iron_man.get_info())
print(black_widow.get_info())
print(hulk.get_info())
print(thor.get_info())
print(hawkeye.get_info())

print(f"Is {captain_america.name} a leader? {captain_america.is_leader()}")
print(f"Is {iron_man.name} a leader? {iron_man.is_leader()}")
print(f"Is {black_widow.name} a leader? {black_widow.is_leader()}")
print(f"Is {hulk.name} a leader? {hulk.is_leader()}")
print(f"Is {thor.name} a leader? {thor.is_leader()}")
print(f"Is {hawkeye.name} a leader? {hawkeye.is_leader()}")
