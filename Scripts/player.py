class Player:
    '''
    Attributes and global configurations for our player.
    '''
    def __init__(self, name_input):
        self.name = str(name_input)
        self.character = "knight"
        self.health = 100
        self.damage = 50