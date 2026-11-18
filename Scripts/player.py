class Player:
    """
    Documentation is great... this class creates a Player object.
    """
    character = None
    health = None
    damage = None
    
    def __init__(self, character_input):
        match character_input:
            case 1:
                self.character = "Wizard"
                self.health = 50
                self.damage = 100
                return
            case 2:
                self.character = "Knight"
                self.health = 100
                self.damage = 50
            case 3:
                self.character = "Archer"
                self.health = 75
                self.damage = 75
                return