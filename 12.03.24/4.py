class Weapon:
    def __init__(self,name,damage,range):
        self.name=name
        self.damage=damage
        self.range=range

    def hit(self,actor,target):
        if target.is_alive():
            if 1:
                pass

class BaseCharacter:
    def __init__(self,pos_x,pos_y,hp):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.hp=hp

    def move(self,delta_x,delta_y):
        self.pos_x+=delta_x
        self.pos_y+=delta_y

    def is_alive(self):
        return self.hp>0

    def get_damage(self,amount):
        self.hp-=amount

    def get_coords(self):
        return [self.pos_x,self.pos_y]

class BaseEnemy(BaseCharacter):
    def hit(self,target):
        pass

class MainHero(BaseCharacter):
    def hit(self,target):
        pass

    def add_weapon(self,weapon):
        if type(weapon)=="Weapon":
            print(f"Get <{weapon}>")

    def next_weapon(self):


    def heal(self,amount):
        self.hp+=amount
        if self.hp>200:
            print("More than max, hp now is 200")
            self.hp=200



weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)