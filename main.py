from myClasses import Die
from myClasses import Player
from myClasses import DiceGame


# Create the instances of Die
player_die = Die()
computer_die = Die()

# Create the instances of the players
my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

# Create the game instance
game = DiceGame(my_player, computer_player)

# Start the game logic
game.play()
