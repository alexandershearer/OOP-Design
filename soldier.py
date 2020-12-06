class Soldier:
    def __init__(self, name, rank="Private", reserve):
        self.name = name
        self.rank = rank
        self.reserve = reserve
        self.loadout = Loadout("Starter")

    def introduce(self):
        print(f"My name is {self.name} and I am a {self.title}.")

    def command(self, command):
        print(command)

    def throw_grenade(self):
        print(f"Throwing {self.loadout.lethal_grenade}!")



class General(Soldier):
    def __init__(self, name, platoon_name):
        super().__init__(name)
        self.rank = "General"
        self.platoon_name = platoon_name


    def introduce(self):
        print(f"My name is {self.name} and I run the platoon as a {self.rank}.")



class Loadout:
    def __init__(self, name, lethal_grenade="Frag", tactical_grenade="Flashbang"):
        self.name = name
        self.weapon = Weapon("Assault Rifle", "M16")
        self.lethal_grenade = lethal_grenade
        self.tactical_grenade = tactical_grenade

    def change_name(self, new_name):
        self.name = new_name

    def change_weapon(self, new_type, new_name):
        self.weapon = Weapon(new_type, new_name)




class Weapon:
    def __init__(self, weapon_type, name, attachment1="", attachment2="", attachment3=""):
        self.weapon_type = weapon_type
        self.name = name
        self.attachment1 = attachment1
        self.attachment2 = attachment2
        self.attachment3 = attachment3
        self.skin = "Default"

    def shoot(self):
        print(f"Shooting my {self.name}")

    def reload(self):
        print(f"Reloading my {self.name}")

    def change_skin(self, skin):
        self.skin = skin





soldier1 = General("John")

soldier1.introduce()











