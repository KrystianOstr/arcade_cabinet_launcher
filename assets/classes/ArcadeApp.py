import pygame as py, sys, subprocess
from assets.classes.Menu import Menu

class ArcadeApp():
    def __init__(self):
        py.init()
        self.display_surface = py.display.set_mode((600,400))
        # self.display_surface = py.display.set_mode((0,0), py.FULLSCREEN)
        py.display.set_caption("Arcade Cabinet Manager")
        self.running = True
        self.menu = Menu()
        self.program_map = {
            "Notepad++": r"C:\Program Files\Notepad++\notepad++.exe",
            "CMD": "start cmd",
            "VSC": r"C:\Users\MLGCS\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        }

    def run(self):
        while self.running:
            self.handle_events()
            self.display_surface.fill((0,0,0))
            self.menu.draw_menu(self.display_surface)
            py.display.update()


    def handle_events(self):
        for event in py.event.get():
                if event.type == py.QUIT:
                    self.quit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        self.quit()
                    if event.key == py.K_DOWN:
                        self.menu.selected_index+=1
                        if self.menu.selected_index == 3:
                            self.menu.selected_index = 0

                    if event.key == py.K_UP:
                        self.menu.selected_index -=1
                        if self.menu.selected_index == -1:
                            self.menu.selected_index = 2
                    if event.key == py.K_RETURN:
                        selected_console = self.menu.menu_options[self.menu.selected_index]
                        command = self.program_map.get(selected_console)
                        if command:
                            subprocess.Popen(command, shell=True)
                            self.quit()

    def quit(self):
        self.running = False
        py.quit()
        sys.exit()