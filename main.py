import pygame as pg
import os
import time
import random
base_dir = os.path.dirname(os.path.abspath(__file__))

pg.init()

game_caption = 'Bounce Ball'

screen_res = (1280,720)
sky_blue = (70,155,200)
dark_grey_blue = (2,48,71)
# pole color
grey_green_blue= (100,50,143)

FPS = 60
gravity_acc = 2

border_thickness = screen_res[1]*0.05

factor = 22
# middle pole
middle_pole_size = (border_thickness*2,screen_res[1]/2)
middle_pole_posi = ((screen_res[0]-border_thickness*2)/2,screen_res[1] - middle_pole_size[1])

# Ball dim
ball_size = (100,100)
ball_ver_vel = 16
ball_position_r = (screen_res[0]*0.25, screen_res[1]*0.55 - ball_size[1])
ball_position_l = (screen_res[0]*0.75, screen_res[1]*0.55 - ball_size[1])
BALL_IMG_PATH = os.path.join(base_dir,'game_assets','imgs','gold_ball.webp')

# Player dim
player_size = (150,250)
player_hori_vel = 5
player_ver_vel = 14
# P1
player_1_position = (screen_res[0]*0.25, screen_res[1]*0.95 - player_size[1])
PLAYER_1_IMG_PATH_STAND = os.path.join(base_dir,'game_assets','imgs','P1_s.png')
PLAYER_1_IMG_PATH_JUMP = os.path.join(base_dir,'game_assets','imgs','P1_j.png')
p1_border_left_limit = border_thickness - factor
p1_border_right_limit = (screen_res[0]-border_thickness*2)/2 + factor
# P2
player_2_position = (screen_res[0]*0.75, screen_res[1]*0.95 - player_size[1])
PLAYER_2_IMG_PATH_STAND = os.path.join(base_dir,'game_assets','imgs','P2_s.png')
PLAYER_2_IMG_PATH_JUMP = os.path.join(base_dir,'game_assets','imgs','P2_j.png')
p2_border_left_limit = (screen_res[0]+border_thickness*2)/2 - factor
p2_border_right_limit = screen_res[0] - border_thickness + factor



class Game():
    def __init__(self,screen_res,bg_color):
        self.screen_res = screen_res
        self.window = pg.display.set_mode(screen_res)
        self.bg_color = bg_color
    
    def ball_motion(self):
        self.ball_vertical_vel()
        self.ball_horizontal_vel()

        ball.ball_rect.y += ball.y_vel
        ball.ball_rect.x += ball.x_vel

    def ball_vertical_vel(self):
        pos = 0
        if p1_border_left_limit<=ball.ball_rect.x<=p1_border_right_limit-ball.ball_size[0]:
            pos = 1
            height_check = (player_1.player_rect.y-ball.ball_size[1]<=ball.ball_rect.y<=player_1.player_rect.y)
            posi_check = (player_1.player_rect.x-ball.ball_size[0]+factor<=ball.ball_rect.x<=player_1.player_rect.x+player_1.player_size[0]-factor)
            if height_check and posi_check:
                ball.y_time = time.time()
                ball.y_vel = -ball_ver_vel


        elif p2_border_left_limit<=ball.ball_rect.x<=p2_border_right_limit-ball.ball_size[0]:
            pos = 2
            height_check = (player_2.player_rect.y-ball.ball_size[1]<=ball.ball_rect.y<=player_2.player_rect.y)
            posi_check = (player_2.player_rect.x-ball.ball_size[0]+factor<=ball.ball_rect.x<=player_2.player_rect.x+player_2.player_size[0]-factor)
            if height_check and posi_check:
                ball.y_time = time.time()
                ball.y_vel = -ball_ver_vel

        if ball.y_time != 0:
            ball.y_vel = ball.y_vel + 0.5

        p1_hori_pole_check = middle_pole_posi[0]-ball.ball_size[0]+1<=ball.ball_rect.x<=middle_pole_posi[0]+middle_pole_size[0]-1
        p1_verti_pole_check = middle_pole_posi[0]-5<=ball.ball_rect.y + ball.y_vel+ball.ball_size[1]<=middle_pole_posi[0]+5
        if p1_hori_pole_check and p1_verti_pole_check:
            ball.y_vel = - ball.y_vel

        if ball.ball_rect.y+ball.y_vel > screen_res[1]*0.95 - ball.ball_size[1]:
            ball.y_vel = 0
            ball.x_vel = 0
            ball.y_time = 0
            if pos ==2:
                ball.ball_rect.y = ball_position_l[1]
                ball.ball_rect.x = ball_position_l[0]
            elif pos==1:
                ball.ball_rect.y = ball_position_r[1]
                ball.ball_rect.x = ball_position_r[0]

    def ball_horizontal_vel(self):
        if p1_border_left_limit<=ball.ball_rect.x<=p1_border_right_limit-ball.ball_size[0]:
            height_check = (player_1.player_rect.y-ball.ball_size[1]<=ball.ball_rect.y<=player_1.player_rect.y)
            posi_check = (player_1.player_rect.x-ball.ball_size[0]+factor<=ball.ball_rect.x<=player_1.player_rect.x+player_1.player_size[0]-factor)
            if height_check and posi_check:
                if player_1.x_vel!=0:
                    ball.x_vel = player_1.x_vel*2
                    # ball.x_vel = player_1.x_vel
        
        elif p2_border_left_limit<=ball.ball_rect.x<=p2_border_right_limit-ball.ball_size[0]:
            height_check = (player_2.player_rect.y-ball.ball_size[1]<=ball.ball_rect.y<=player_2.player_rect.y)
            posi_check = (player_2.player_rect.x-ball.ball_size[0]+factor<=ball.ball_rect.x<=player_2.player_rect.x+player_2.player_size[0]-factor)
            if height_check and posi_check:
                if player_2.x_vel!=0:
                    ball.x_vel = player_2.x_vel*2
                    # ball.x_vel = player_2.x_vel

        p1_hori_pole_check = middle_pole_posi[0]-ball.ball_size[0]<ball.ball_rect.x + ball.x_vel<middle_pole_posi[0]+middle_pole_size[0]-20
        p1_verti_pole_check = middle_pole_posi[1]-5<=ball.ball_rect.y + ball.y_vel + ball.ball_size[1]<=middle_pole_posi[1]+20

        p1_hori_pole_check_for_side = middle_pole_posi[0]-ball.ball_size[0]<ball.ball_rect.x + ball.x_vel<middle_pole_posi[0]+middle_pole_size[0]-20
        p1_verti_pole_check_for_side = middle_pole_posi[1]<ball.ball_rect.y + ball.y_vel + ball.ball_size[1]

        # print(ball.ball_rect.y - ball.y_vel + ball.ball_size[1])
                
        if p1_hori_pole_check and p1_verti_pole_check:
            # print('top')
            if ball.y_vel>0:
                ball.y_vel = -ball.y_vel
            ball.ball_rect.y = middle_pole_posi[1] - ball.ball_size[1] - 5

        elif p1_hori_pole_check_for_side and p1_verti_pole_check_for_side:
            # print('side')
            ball.x_vel = -ball.x_vel
            if ball.ball_rect.x <=middle_pole_posi[0]:
                ball.ball_rect.x = middle_pole_posi[0] - ball.ball_size[0] - 5
            elif ball.ball_rect.x >=middle_pole_posi[0]:
                ball.ball_rect.x = middle_pole_posi[0] + middle_pole_size[0] + 5
        if ball.ball_rect.x<= border_thickness:
            ball.x_vel = -ball.x_vel
            ball.ball_rect.x = border_thickness
        elif ball.ball_rect.x + ball.x_vel>= screen_res[0] - border_thickness - ball.ball_size[0]:
            ball.x_vel = -ball.x_vel
            ball.ball_rect.x = screen_res[0] - border_thickness - ball.ball_size[0]

    def player_motion(self):
        self.calc_vertical_vel(player_1)
        self.calc_vertical_vel(player_2)

        self.calc_horizontal_vel(player_1)
        self.calc_horizontal_vel(player_2)

        player_1.player_rect.y += player_1.y_vel
        player_1.player_rect.x += player_1.x_vel

        player_2.player_rect.y += player_2.y_vel
        player_2.player_rect.x += player_2.x_vel

    def calc_vertical_vel(self,player):
        keys = pg.key.get_pressed()
        if keys[player.key_up]:
            if player.y_vel == 0:
                player.y_time = time.time()
                player.y_vel = -14

        if keys[player.key_down]:
            if player.y_vel != 0:
                player.y_vel += 1

        if player.y_time != 0:
            player.y_vel = player.y_vel + (gravity_acc*(time.time()-player.y_time))

        if player.player_rect.y>screen_res[1]*0.95 - player.player_size[1] - player.y_vel:
            player.y_vel = 0
            player.y_time = 0
            player.player_rect.y = screen_res[1]*0.95 - player.player_size[1]

    def calc_horizontal_vel(self,player):
        keys = pg.key.get_pressed()
        if keys[player.key_left]:
            player.x_vel = - player_hori_vel
        elif player.x_vel < 0:
            player.x_vel += 0.15
            # player.x_vel += 2.5

        if keys[player.key_right]:
            player.x_vel = player_hori_vel
        elif player.x_vel > 0:
            player.x_vel -= 0.15
            # player.x_vel -= 2.5

        if player.player_rect.x<= player.border_left_limit - player.x_vel:
            player.x_vel = 0
            player.player_rect.x = player.border_left_limit
        elif player.player_rect.x>= player.border_right_limit - player.x_vel:
            player.x_vel = 0
            player.player_rect.x = player.border_right_limit

    def draw_border(self):
        top = pg.Rect(0, 0, self.screen_res[0], border_thickness)
        pg.draw.rect(self.window, dark_grey_blue, top)

        right = pg.Rect(self.screen_res[0] - border_thickness, 0, border_thickness, self.screen_res[1])
        pg.draw.rect(self.window, dark_grey_blue, right)

        bottom = pg.Rect(0, self.screen_res[1]-border_thickness, self.screen_res[0], border_thickness)
        pg.draw.rect(self.window, dark_grey_blue, bottom)

        left = pg.Rect(0, 0, border_thickness, self.screen_res[1])
        pg.draw.rect(self.window, dark_grey_blue, left)


    def draw_level(self):
        middle_bar = pg.Rect(middle_pole_posi[0], middle_pole_posi[1],
                              middle_pole_size[0], middle_pole_size[1])
        pg.draw.rect(self.window, grey_green_blue, middle_bar)

        self.draw_border()
        
    def draw(self):
        self.window.fill(self.bg_color)

        self.draw_level()
        self.player_motion()
        self.ball_motion()

        self.window.blit(ball.BALL, (ball.ball_rect.x,ball.ball_rect.y))

        if player_1.y_vel==0:
            self.window.blit(player_1.PLAYER_STAND, (player_1.player_rect.x,player_1.player_rect.y))
        else:
            self.window.blit(player_1.PLAYER_JUMP, (player_1.player_rect.x,player_1.player_rect.y))

        if player_2.y_vel==0: 
            self.window.blit(player_2.PLAYER_STAND, (player_2.player_rect.x,player_2.player_rect.y))
        else:
            self.window.blit(player_2.PLAYER_JUMP, (player_2.player_rect.x,player_2.player_rect.y))

        pg.display.update()

    def set_game_caption(self,caption):
        pg.display.set_caption(caption)


class Ball():
    def __init__(self,ball_size,BALL_IMG_PATH,ball_position):
        self.ball_size = ball_size
        self.BALL_IMG = pg.image.load(BALL_IMG_PATH)
        self.BALL = pg.transform.scale(self.BALL_IMG, self.ball_size)
        self.ball_rect = pg.Rect(ball_position[0],ball_position[1], self.ball_size[0], self.ball_size[1])

        self.x_vel = 0
        self.y_vel = 0

        self.y_time = 0


class Player():
    def __init__(self,player_size,PLAYER_IMG_PATH_STAND,PLAYER_IMG_PATH_JUMP,player_position,name):
        self.player_size = player_size
        if name == 'P1':
            self.PLAYER_IMG_STAND = pg.transform.flip(pg.image.load(PLAYER_IMG_PATH_STAND), True, False)
            self.PLAYER_IMG_JUMP = pg.transform.flip(pg.image.load(PLAYER_IMG_PATH_JUMP), True, False)
        elif name == 'P2':
            self.PLAYER_IMG_STAND = pg.image.load(PLAYER_IMG_PATH_STAND)
            self.PLAYER_IMG_JUMP = pg.image.load(PLAYER_IMG_PATH_JUMP)

        self.PLAYER_STAND = pg.transform.scale(self.PLAYER_IMG_STAND, self.player_size)
        self.PLAYER_JUMP = pg.transform.scale(self.PLAYER_IMG_JUMP, self.player_size)
        self.player_rect = pg.Rect(player_position[0],player_position[1], self.player_size[0], self.player_size[1])

        self.x_vel = 0
        self.y_vel = 0

        self.y_time = 0

        if name == 'P1':
            self.key_up = pg.K_w
            self.key_down = pg.K_s
            self.key_right = pg.K_d
            self.key_left = pg.K_a
            self.border_left_limit = p1_border_left_limit
            self.border_right_limit = p1_border_right_limit - self.player_size[0] 
        if name == 'P2':
            self.key_up = pg.K_UP
            self.key_down = pg.K_DOWN
            self.key_right = pg.K_RIGHT
            self.key_left = pg.K_LEFT
            self.border_left_limit = p2_border_left_limit
            self.border_right_limit = p2_border_right_limit - self.player_size[0]


player_1 = Player(player_size,PLAYER_1_IMG_PATH_STAND,PLAYER_1_IMG_PATH_JUMP,player_1_position,'P1')
player_2 = Player(player_size,PLAYER_2_IMG_PATH_STAND,PLAYER_2_IMG_PATH_JUMP,player_2_position,'P2')

if random.randint(1, 2)==1:
    ball = Ball(ball_size,BALL_IMG_PATH,ball_position_l)
else:
    ball = Ball(ball_size,BALL_IMG_PATH,ball_position_r)


def main():
    clock = pg.time.Clock()
    game = Game(screen_res,sky_blue)
    game.set_game_caption(game_caption)
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                running = False
        
        game.draw()

    pg.quit()

if __name__ == "__main__":
    main()