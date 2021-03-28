import const

class Character:
    def __init__(self, fileList = []):
        # Verify the contents of the file list:
        
        
        # Character progress stats:
        self.level = 0
        self.rank = 0
        
        # Template guides the character's stats and growth:
        self.templateClass = 0
        
        # Determinary stats:
        self.strength = 0
        self.constitution = 0
        self.stamina = 0
        self.agility = 0
        self.dexterity = 0
        self.intelligence = 0
        self.spirit = 0
        self.will = 0
        self.wisdom = 0
        
        # Character vitals:
        self.health = 0
        self.magic = 0
        self.special = 0
        
        # Secondary stats:
        self.baseDamage = 0
        self.Defense = 0
        self.resistance = 0
        self.hitRate = 0
        self.blockRate = 0
        self.parryRate = 0
        self.dodgeRate = 0
        self.spellPower = 0
        
        # Skills
        self.skills = []
