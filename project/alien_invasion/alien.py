import pygame
import os
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置其rect属性
        image_path = os.path.join(os.path.dirname(__file__), 'images/alien.bmp')
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
