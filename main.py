from myClasses import Die
from myClasses import Player
from myClasses import DiceGame


# ------------------------------ ルール ------------------------------
# ・二人のプレイヤーがそれぞれサイコロを振る
# ・大きい目が出た方の勝ち
# ・勝った方は持ち点+1, 負けた方は持ち点-1
# ・持ち点が無くなったらゲーム終了
# -------------------------------------------------------------------

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
