import sys
from typing import Set
import pygame
from ship import Ship

from settings import Settings

class AlienInvasion:
    """Class that manage game source and action"""

    def __init__(self):
        """Initial game and create game source"""
        pygame.init()
        # 设置帧率
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.displa y.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start game mainloop"""
        while True:
            # Detect keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Dispalay screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Create instance and run game
    ai = AlienInvasion()
    ai.run_game()
