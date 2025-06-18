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
        self.NES = r"C:\Emu\fceux\fceux64.exe"
        self.program_map = {
            "Super Mario Bros": {"cmd": [self.NES,r"C:\Emu\fceux\roms\Super Mario Bros.nes" ], "shell": False},
            "Kid Icarus": {"cmd": [self.NES,r"C:\Emu\fceux\roms\Kid Icarus.nes" ], "shell": False},
            "Contra": {"cmd": [self.NES,r"C:\Emu\fceux\roms\Contra.nes" ], "shell": False},
            "Duck Tales": {"cmd": [self.NES,r"C:\Emu\fceux\roms\Duck Tales.nes" ], "shell": False},
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
                        if self.menu.selected_index == len(self.menu.menu_options):
                            self.menu.selected_index = 0

                    if event.key == py.K_UP:
                        self.menu.selected_index -=1
                        if self.menu.selected_index == -1:
                            self.menu.selected_index = 2
                    if event.key == py.K_RETURN:
                        selected_console = self.menu.menu_options[self.menu.selected_index]
                        entry = self.program_map.get(selected_console)

                        if entry:
                            try:
                                print(f"[INFO] Uruchamiam: {entry['cmd']} | shell={entry['shell']}")
                                subprocess.Popen(entry["cmd"], shell=entry["shell"])
                            except Exception as e:
                                print(f"[BŁĄD] Nie udało się uruchomić: {e}")


    def quit(self):
        self.running = False
        py.quit()
        sys.exit()