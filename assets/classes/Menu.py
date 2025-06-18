import pygame as py

class Menu():
    def __init__(self):
        # self.menu_options = (["NES", "SNES", "NEOGEO"])
        self.menu_options = (["Super Mario Bros","Kid Icarus", "Contra","Duck Tales" ])
        self.selected_index = 0
        self.font = py.font.Font('assets/graphics/subatomic.ttf', 48)

    def draw_menu(self, display_surface):
        pos_x = display_surface.get_width() //2
        for i, option in enumerate(self.menu_options):
            pos_y = (display_surface.get_height() // 2) + (i*60) - 100
            color = (0,255,0) if i == self.selected_index else (255,255,255)

            option_text = self.font.render(f'{option}', True,color)
            option_rect = option_text.get_rect(center=(pos_x, pos_y))
            display_surface.blit(option_text, option_rect)