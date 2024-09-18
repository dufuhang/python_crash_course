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
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start game mainloop"""
        while True:
            self._check_events()
            self.ship.update()
            # 每次循环时都重绘屏幕
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                _check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                _check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Dispalay screen
        pygame.display.flip()

if __name__ == '__main__':
    # Create instance and run game
    ai = AlienInvasion()
    ai.run_game()
