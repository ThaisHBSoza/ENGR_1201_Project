from Scripts.player import Player

def main():
    character_type = int(input(
"""
Choose a character:
1. Wizard
2. Knight
3. Archer\n
"""
    ))
    
    player_choice = Player(character_type)
    print(f"You are a {player_choice.character}!")
    print(f"With {player_choice.health} health!")
    print(f"And {player_choice.damage} in attack damage!")

if __name__ == "__main__":
    main()

# don't worry too much about builtin variables like
# __name__ or __init__, but if you would like to
# learn about those, check out this documentation
# link: https://docs.python.org/3/reference/datamodel.html#special-writable-attributes
# use crtl+f to find what you want.

# additionally, if you would like to learn more about
# Object Oriented Programming (OOP), you can check out
# this great YouTube link tutorial: https://www.youtube.com/watch?v=ZDa-Z5JzLYM