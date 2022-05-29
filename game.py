from pygame import *

class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
    #отражение по горизонтали
    def flip(self):
        self.image = transform.flip(self.image, True, False)

class Player(GameSprite) :
    # Обработка нажатия клавиш для управления
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


display.set_caption("Пинпонг")

back = (255, 255, 255)
win_width = 900
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

player1 = Player('racket.1.png', 5, (win_height / 2) - 40, 14, 80, 5)
player2 = Player('racket.2.png', win_width - 14 - 5, (win_height / 2) - 40, 14, 80, 5)
ball = GameSprite('football.png', win_width/2 - 20, win_height/2 - 20, 40, 40, 80)

font.init()
defaultfont = font.SysFont('Arial', 24)
lose1 = defaultfont.render('Player 1 lose', 1, (255, 215, 0))
lose2 = defaultfont.render('Player 2 lose', 1, (255, 0, 0))


speed_x = 3
speed_y = 3

run = True
finish = False

while run :
    for e in event.get() :
        if e.type == QUIT:
            run = False

    window.fill(back)
    
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (400, 200))

    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (400, 200))

    if not finish :
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2) :
            speed_x *= -1

        player1.update_l()
        player2.update_r()

        player1.reset()
        player2.reset()
        ball.reset()
        
    display.update()
    time.delay(10)
