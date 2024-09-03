import sys
import pygame

class AlienInvasion:
    """Class that manage game source and action"""

    def __init__(self):
        """Initial game and create game source"""
        pygame.init()
        # 设置帧率
        self.clock = pygame.time.Clock()

        # 设置背景色
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start game mainloop"""
        while True:
            # Detect keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)
            # Dispalay screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Create instance and run game
    ai = AlienInvasion()
    ai.run_game()
