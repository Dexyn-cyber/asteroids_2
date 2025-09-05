import pygame
import argparse
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from stats import *
from super_shot import SuperShot
from hud import *

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Enable Debug mode')
args = parser.parse_args()


def main():
    is_alive = True

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_background = pygame.image.load(SPACE_BACKGROUND).convert() # convert optimizes the image for faster blitting
    pygame.display.set_caption("Little Asteroids")
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

        if args.debug:
            if player_stats.health <= 0: # DEBUG: purposes
                        total_time = pygame.time.get_ticks() // 1000
                        print("Game over!")
                        print(player_stats.get_final_score())
                        death_screen(screen, player_stats, total_time)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Goodbye.")
                return
            
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                asteroid.kill()
                player_stats.health -= 1
                if player_stats.health <= 0:
                    total_time = pygame.time.get_ticks() // 1000
                    print("Game over!")
                    print(player_stats.get_final_score())
                    death_screen(screen, player_stats, total_time)

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

        scaled_image = pygame.transform.scale(screen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_image, (0,0)) # Draw screen first before objects, the objects get painted over.

        for object in drawable:
            object.draw(screen)
        stat_hud.update_stats(player_stats.kills, player_stats.score, player_stats.health)
        stat_hud.draw(screen)

        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


def death_screen(screen, stats, time):
    font = pygame.font.SysFont('Arail', 48)
    small_font = pygame.font.SysFont(None, 32)

    screen.fill((0,0,0))

    def convert_time(time):
        minute = time // 60
        seconds = time % 60
        return f"{minute}min {seconds}sec"

    game_over_text = small_font.render("GAME OVER", True, (255, 0, 0))
    kills_text = font.render(f"You got {stats.kills} total kills!", True, (255,255,255))
    small_kills_text = font.render(f"{stats.sm_kills} of asteroid kills were small.", True, (255,255,255))
    medium_kills_text = font.render(f"{stats.med_kills} of them were medium.", True, (255,255,255))
    big_kills_text = font.render(f"{stats.big_kills} of them were giant asteroids.", True, (255,255,255))
    score_text = font.render(f"Your endgame score was {stats.score}", True, (255,255,255))
    time_active = font.render(f"You lasted {convert_time(time)}", True, ('white'))

    # Center screen
    screen.blit(game_over_text, (screen.get_width()//2 - game_over_text.get_width()//2, 225))
    screen.blit(score_text, (screen.get_width()//2 - score_text.get_width()//2, 250))
    screen.blit(time_active, (screen.get_width()//2 - time_active.get_width()//2, 300))
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
