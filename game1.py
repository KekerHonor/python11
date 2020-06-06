import random
class Hero:
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("Hi, I am", self.name, self.hp, self.damage)
    def attack(self)->int:
        return self.damage
    def attacked(self, damage: int):
        if self.hp - damage <= 0:
            print(self.name," died...")
            return True
        else:
            self.hp = self.hp - damage
            return False
you = Hero("You",100,20)
monster = Hero("Monster",100,10)
too = -1
while True:
    is_died = False
    luck = random.randrange(1,3)
    too = int(input("Ugadai chislo ot 1 do 2 \n"))
    if luck ==too:
        print("Ti atakuesh")
        is_died = monster.attacked(you.attack())
        print("Monster's hp:",monster.hp)
    else:
        print("zashishaisa!!!")
        is_died = you.attacked(monster.attack())
        print("Your hp ",you.hp)
    if is_died :
        break
else:
    ("Game over")