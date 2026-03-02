from player.player_structure import PLAY_GAME, WELCOME_TO_PLAYER
from strings import WHICH_APP


PLAYER = "player"
EDITOR = "editor"
MAIN = "main"
START_PLAYING = [WELCOME_TO_PLAYER, PLAY_GAME]
PROGRAMS = {
    PLAYER: [WHICH_APP, PLAYER.capitalize()],
    EDITOR: [WHICH_APP, EDITOR.capitalize()],
    MAIN: [WHICH_APP],
}
