# COLORS
BLUE            = (0, 0, 255)
BLACK           = (0, 0, 0)
RED             = (255, 0, 0)
YELLOW          = (255, 255, 0)

# GRID FORMAT
ROW_COUNT       = 6
COLUMN_COUNT    = 7
WINDOW_LENGTH   = 4

# CONFIG IA
AI              = 1

AI1             = 0
AI2             = 1

AI_PIECE        = 2
AI2_PIECE       = 1
AI1_PIECE       = 2

EMPTY           = 0

# PLAYER
PLAYER_PIECE    = 1
PLAYER          = 0

# WINDOW
T_CLOSE_WINDOW  = 1000
T_SPLASHSCREEN  = 5

# CONFIG PYGAME
SQUARESIZE      = 100
width           = COLUMN_COUNT * SQUARESIZE
height          = (ROW_COUNT + 1) * SQUARESIZE
size            = (width, height)
RADIUS          = int(SQUARESIZE / 2 - 5)
game_over       = False
