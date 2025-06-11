import pygame
import os

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        # 获取屏幕的rect属性
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        # 这里使用os库中的获取路径的方法，按照书中的代码会提示FileNotFound错误
        image_path = os.path.join(os.path.dirname(__file__), 'images/ship.bmp')
        self.image = pygame.image.load(image_path)

        # 获取飞船的外接矩形
        self.rect = self.image.get_rect()

        # 每艘飞船最初都在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)