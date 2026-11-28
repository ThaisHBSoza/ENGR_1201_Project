class BladeVillager:
    '''
    Villager who gives the player a blade.
    '''
    def __init__(self):
        self.dialogue = ""
        self.give_item = None #TODO add blade class

class PotionVillager:
    '''
    Villager who gives the player a potion.
    '''
    def __init__(self):
        self.dialogue = ""
        self.give_item = None #TODO add potion class
        
class WizardTeammate:
    '''
    A wizard teammate for our player during their battles.
    '''
    def __init__(self):
        self.character = "wizard"
        self.health = 100
        self.damage = 50
        self.healing_amount = 50
        self.healing_cooldown = 3
        
class ArcherTeammate:
    '''
    A archer teammate for our player during their battles.
    '''
    def __init__(self):
        self.character = "archer"
        self.health = 75
        self.damage = 75