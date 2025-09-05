import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from stats import *
from super_shot import SuperShot
from hud import *

is_alive = True

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create an object to help track time
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    stat_hud = HUD(10, 10)

    Player.containers = (updatable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    super_shots = pygame.sprite.Group()
    SuperShot.containers = (super_shots, updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # This spawns play in the center of the screen

    while is_alive:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye.")
                return
            
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                print(player_stats.get_final_score())
                death_screen(screen, player_stats)

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    player_stats.got_kill(asteroid)
                    break # Exit the shots loop after first collision
            for super_shot in super_shots:
                if asteroid.collides_with(super_shot):
                    super_shot.kill()
                    asteroid.split()
                    asteroid.kill()
                    player_stats.got_kill(asteroid)
                    break

        screen.fill("black") # Draw screen first before objects, the objects get painted over.

        for object in drawable:
            object.draw(screen)
        stat_hud.update_stats(player_stats.kills, player_stats.score, player_stats.health)
        stat_hud.draw(screen)

        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


def death_screen(screen, stats):
    font = pygame.font.SysFont('Arail', 48)
    small_font = pygame.font.SysFont(None, 32)

    screen.fill((0,0,0))

    game_over_text = small_font.render("GAME OVER", True, (255, 0, 0))
    kills_text = font.render(f"You got {stats.kills} total kills!", True, (255,255,255))
    small_kills_text = font.render(f"{stats.sm_kills} of asteroid kills were small.", True, (255,255,255))
    medium_kills_text = font.render(f"{stats.med_kills} of them were medium.", True, (255,255,255))
    big_kills_text = font.render(f"{stats.big_kills} of them were giant asteroids.", True, (255,255,255))
    score_text = font.render(f"Your endgame score was {stats.score}", True, (255,255,255))

    # Center screen
    screen.blit(game_over_text, (screen.get_width()//2 - game_over_text.get_width()//2, 225))
    screen.blit(score_text, (screen.get_width()//2 - score_text.get_width()//2, 250))
    screen.blit(kills_text, (screen.get_width()//2 - kills_text.get_width()//2, 350))
    screen.blit(small_kills_text, (screen.get_width()//2 - small_kills_text.get_width()//2, 400))
    screen.blit(medium_kills_text, (screen.get_width()//2 - medium_kills_text.get_width()//2, 450))
    screen.blit(big_kills_text, (screen.get_width()//2 - big_kills_text.get_width()//2, 500))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                waiting = False
    exit(0)


if __name__ == "__main__":
    main()
