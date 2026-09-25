import rondom
import pygame


class button():
    def_int_(self,x,y,pos,width,hight):
       self.x = x
       self.y = y
       self.width = width
       self.hight = hight
       self.pos = Pos

    def clicked(self,pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            i self.pos[1] > selfy.y and self.pos[1] < self.x + self.width:
            return true
        return False


    class Rpsgame():
        def_init_(self):
        pygame.init():

        self.screen = pygame.display.set_mode((960,640))
        pygame.display.set_caption("RPS Smasher")

        self.bg = pygame.image.load("background.jpg")
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()

        self.chose_rock = pygame.image.load(rock.png)convert_alpha()
        self.chose_papper = pygame.image.load(papper.png)convert_alpha()
        self.chose_sissor = pygame.image.load(sissor.png)convert_alpha()


        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.r_btn,(20,500)
        self.screen.blit(self.r_btn,(330,500)
        self.screen.blit(self.r_btn,(640,500)

        self.rock_btn = button(30,520) ,(30,520) ,(300,140)
        self.papper_btn = button(30,520) ,(30,520) ,(300,140)
        self.sissor_btn = button(30,520) ,(30,520) ,(300,140)

        self.font = self.font.font(("splatch.ttf"), 90)
        self.text = self.font.render(f" ",true, (255,255,255))