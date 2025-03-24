import pygame.image

from code.Const import WIN_WIDTH, COLOR_PRIMARY, COLOR_SECUNDARY


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menubg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menusom.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=60, text="OJogo", text_color=(COLOR_PRIMARY), text_center_pos=(WIN_WIDTH / 2, 70))
            self.menu_text(text_size=30, text="New Game", text_color=(COLOR_SECUNDARY),
                           text_center_pos=(WIN_WIDTH / 2, 180))
            self.menu_text(text_size=30, text="Score", text_color=(COLOR_SECUNDARY),
                           text_center_pos=(WIN_WIDTH / 2, 210))
            self.menu_text(text_size=30, text="Exit", text_color=(COLOR_SECUNDARY),
                           text_center_pos=(WIN_WIDTH / 2, 240))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    import pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        pygame.font.init()
        text_font = pygame.font.SysFont("GeovaTrial-SemiBold.ttf", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
