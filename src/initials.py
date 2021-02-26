# creates template for all mobjs that exist in the game

class Mobj:
    
    # instantiates class for easy attribute access
    def __init__(self, health, dmg, speed, lvl, xp, *armor, pain, perks, resist, ammo):
        
        # pass an int, ex. 100
        self.health = health
        
        # does not apply to demon mobjs, pass a str, ex. "Mega_Armor"
        self.armor = armor
        
        # pass an int, ex. 4
        self.melee_dmg = dmg
        
        # pass a float, ex. 5.8 or 15.7
        self.pain_chance = pain
        
        # pass an int, ex. 60
        self.speed = speed
        
        # pass an int, ex. 12
        self.lvl = level
        
        # checks how much xp player has, or how much xp demon drops, pass an int, ex. 7000
        self.xp = xp
        
        # pass as a list of strs, ex. [Tank, Light_Footed, Tactician]
        self.perks = perks
        
        # pass as a list of strs, ex. [NO_SPLASH_DMG, NO_INFIGHT, NO_DMG]
        self.resistances = resist
        
        # pass a dict, ex. {"Shells": 21, "Bullets": 211}
        self.ammo = ammo
    
    # the following methods allows for modification to instantiated 
    # classes during gameplay, pass the same type into the param's please,
    # refer to the __init__ method for types
    
    def changeHealth(self):
        
        # verifies the param type is the same as the one instantiated
        if isinstance(health, int):
            
            # changes self.health value to that of health if conditional passes
            self.health = health
        
        # otherwise, throw a hissy fit and raise an error
        else:
            raise AttributeError("The parameter does not match the type of self.health")
    
    def changeArmor(self):
        
        # if the armor value doesn't exist on instantiation, raise error
        if not self.armor:
            raise AttributeError("\"self.armor\" was not instantiated")
        
        # verifies the param type is the same as the one instantiated
        if isinstance(armor, str):
            
            # reassigns the self.armor attribute
            self.armor = armor
        
        # otherwise, throw a hissy fit and raise an error
        else:
            raise AttributeError("The parameter does not match the type of self.armor")
    
    def changeMeleeDmg(self):
        
        # verifies parameter is the same as attribute
        if isinstance(damage, int):
            
            # increases / decreases self.base_damage to dmg param
            self.melee_dmg = damage
        
        else:
            raise AttributeError("The parameter does not match the type of self.melee")
    
    def changeLvl(self, new_lvl):
        
        # you know what this does by now
        if isinstance(new_lvl, int):
            
            # modifies level attribute
            self.lvl = new_lvl
        
        # and this too
        else:
            raise AttributeError("The parameter does not match the type of self.lvl")
    
    def addXP(self, new_xp):
        
        if isinstance(new_xp, int):
            
            # increments self.xp
            self.xp += new_xp
        
        else:
            raise AttributeError("The parameter does not match the type of self.xp")
    
    def changeSpeed(self, speed):
        
        if isinstance(speed, int):
            
            # modifies self.speed
            self.speed = speed
        
        else:
            raise AttributeError("The parameter does not match the type of self.speed")

    def modPerks(self, operation, perk):
        
        # if self.perks wasn't instantiated, raise error
        if not self.perks:
            raise AttributeError("\"self.perks\" was not instantiated")
        
        if isinstance(perk, str):
            
            # checks if the operation is "add", if so, append perk to self.perks
            if operation == "add":
                self.perks.append(perk)
            
            # checks if the operation is "del", if so, remove perk from self.perks
            elif operation == "del":
            self.perks.remove(perk)
            
            # otherwise, raise an Attribute Error
            else:
                raise AttributeError("Invalid operation")
        
        else:
            raise AttributeError("The last parameter does not match the type of the items in self.perks")
    
    def modResistances(self, operation, resist):
        
        # if self.resistances wasn't instantiated, raise error
        if not self.resistances:
            raise AttributeError("\"self.resistances\" was not instantiated")
        
        if isinstance(resist, str):
            
            # checks if the operation is "add", if so, append resist to self.resistances
            if operation == "add":
                self.perks.append(resist)
            
            # checks if the operation is "del", if so, remove resist from self.resistances
            elif operation == "del":
                self.perks.remove(resist)
            
            # otherwise, raise an Attribute Error
            else:
                raise AttributeError("Invalid operation")
        
        else:
            raise AttributeError("The last parameter does not match the type of the items in self.resistances")

    def modAmmo(self, operation, ammo_type, count):
        
        # if self.ammo wasn't instantiated, raise error
        if not self.ammo:
            raise AttributeError("\"self.ammo\" was not instantiated")
        
        # now check if the count parameter is the same type as self.ammo
        if isinstance(count, int):
            
            # check if the operation is "add", if so, do the next thing
            if operation == "add":
            
                # now check if the ammo type exists, if so, add count to ammo_type
                if ammo_type in self.ammo:
                    
                    self.ammo[ammo_type] += count
                
                # otherwise, throw a Key Error
                else:
                    raise KeyError("Ammo type was not found in self.ammo")
            
            # check if the operation is "remove", if so, do the next thing
            elif operation == "remove":
                
                # now check if the ammo type exists, if so, subtract count from ammo_type
                if ammo_type in self.ammo:
                    
                    self.ammo[ammo_type] -= count
                
                # otherwise, throw a Key Error
                else:
                    raise KeyError("Ammo type was not found in self.ammo")
            
            # otherwise, throw an Attribute Error
            else:
                raise AttributeError("Invalid operation")
        
        # otherwise, throw an AttributeError
        else:
            raise AttributeError("The last parameter does not match the type of self.ammo")

# creates a template for all weapons to follow
class Weapon:

    def __init__(self, fired_, associated_mobj, )
