import pygame, sys 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('PNG/Characters/Player male/male_head.png').convert_alpha()
        self.rect = self.image.get_rect()

# BASIC SETTINGS ---------------------------------------------
pygame.init()
clock = pygame.time.Clock()
width = 680
height = 400
scr = pygame.display.set_mode((width,height))
pygame.display.set_caption('Human Farm')
# CLASS---------------------------------------------
inst_player = pygame.sprite.GroupSingle()
inst_player.add(Player())
# VARIABLES---------------------------------------------
is_game_on = True
#main_font = pygame.font.Font()


while(True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if is_game_on :
        inst_player.draw(scr)
        inst_player.update()
    else: 
        pass 
    clock.tick(60)