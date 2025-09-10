# SCREEN
SCREEN_WIDTH = 1860 # Default: 1280
SCREEN_HEIGHT = 1000 # Default: 980
# PLAYER
PLAYER_HEALTH = 3 # Default: 3
PLAYER_SPEED = 200 # Default: 200
PLAYER_TURN_SPEED = 300 # Default: 300
PLAYER_RADIUS = 20 # Default 20
PLAYER_SHOOT_SPEED = 500 # Default: 500
PLAYER_SHOOT_COOLDOWN = 0.3 # Default: 0.3
PLAYER_SUPER_SHOT_COOLDOWN = 2  # Default: 2
# BULLETS
SHOT_RADIUS = 5 # Default: 5
SUPER_SHOT_RADIUS = 4 # Default: 4
SUPER_SHOT_PELLETS = 10 # Default: 10
# ASTEROIDS
ASTEROID_MIN_RADIUS = 20 # Default: 20
ASTEROID_KINDS = 4 # Default: 3
ASTEROID_SPAWN_RATE = 0.8 # seconds Default: 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS # Do not change
# IMAGES
SPACE_BACKGROUND = "./images/space_background.jpg"
# Upgrades --- Default:=Kills for unlock
# Unlocks
# Fire rate modifiers
FASTER_FIRE_RATE_UNLOCK = 50 # Default: 50
UPGRADED_PLAYER_SHOOT_COOLDOWN = 0.15
# Player speed modifiers
UPGRADED_PLAYER_SPEED_UNLOCK = 300 # Default: 300
UPGRADED_PLAYER_SPEED = 350 # The modified speed.
PLAYER_DOUBLE_SHOT_UNLOCK = 125 # Default: 125
# Player Abilities
# Blink: Teleports the player forward by about 250-400 pixels.
# Dash: brief movement speed [+300-500]
# Shield: A basic non-regenerating shield, False life in a way.
# Power ups?:
# Shotgun power up (current super shot)