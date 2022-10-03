from myClasses import Die
from myClasses import Player
from myClasses import DiceGame


# 各プレイヤーのサイコロを準備
player_die = Die()
computer_die = Die()

# プレイヤーを準備
my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

# ゲームの準備
game = DiceGame(my_player, computer_player)

# ゲームの開始
game.play()
