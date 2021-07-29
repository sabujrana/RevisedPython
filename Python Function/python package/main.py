# import game.character.player#(access all definition inside player module)

# game.character.player.get_player_info()#(calling get_player_info() function)


### from import statement

# from game.character import player #importing only player module from packages
# from game.character import boss # importing boss module from packages

# player.get_player_info()
# boss.get_boss_info()

### only certain definition from inside the module
from game.character.boss import get_boss_info
from game.character.player import get_player_info
from game.weapon.gun import gun_description 
from game.weapon.knife import knife_description

get_boss_info() 
get_player_info()
