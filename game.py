class Hero:
    def __init__(self, name: str, hp: int, mana: int, damage: int):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.damage = damage
        print("Hi, I am", self.name)
    def attack(self)->int:
        return self.damage
    def attacked(self, damage: int):
        self.hp = self.hp - damage
a = Hero("Alucard",100,100,50)
b = Hero("Thor",80,120,100)
b.attacked(a.attack())
print(a.hp)
print(b.hp)