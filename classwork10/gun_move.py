import math
import random
from random import choice

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 60
        self.count = 0

    def move(self):
        """Перемещает мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """   
        if (WIDTH - self.x) <= self.r:
            self.x = WIDTH - self.r
            self.vx = -self.vx/2
        if (HEIGHT - self.y) <= self.r:
            self.y = HEIGHT - self.r
            self.vy = (- self.vy)/1.6
            self.vx = (self.vx)/2
            self.count += 1
        if self.count == 5:
            self.vx = 0
            self.vy = 0
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        

    def draw(self):
        """Рисует мячи."""
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r+1
        )
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def alive(self):
        """Отнимает жизнь мяча каждую единицу времени после его остановки.

        Returns:
            Возвращает False, если жизни заканчиваются."""
        if self.count >= 4:
            self.live -= 1
        if self.live <= 0:
            return False



    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        global bullet
        if (self.y - obj.y)**2 + (self.x - obj.x)**2 < (self.r + obj.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen: pygame.Surface):
        """Конструктор класса Gun"""
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        if event.pos[0] != 40:
            self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 40))
        if event.pos[0] == 0:
            self.an = math.asin(1)

        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. 
        Args:
            event: событие мыши.
        """
        if event.pos[0] != 40:
            self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 40))
        if event.pos[0] == 0:
            self.an = math.asin(1)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self, event):
        """Отрисовка пушки.  
        Args:
            event: событие мыши.
        """
        if event.pos[0] != 40:
            self.an = math.atan((450 - event.pos[1]) / (event.pos[0] - 40))
        if event.pos[0] == 0:
            self.an = math.asin(1)
        l = self.f2_power + 20
        cos = math.cos(self.an)
        sin = math.sin(self.an)
        pygame.draw.polygon(
            self.screen, 
            self.color, 
            [(40 + 5 * sin, 450 + 5 * cos),
            (40 + l * cos + 5 * sin, 450 - l * sin + 5 * cos),
            (40 + l * cos - 5 * sin, 450 - l * sin - 5 * cos),
            (40 - 5 * sin, 450 - 5 * cos)]
        )
        

    def power_up(self):
        """Изменение модуля скорости выстрела в зависимости от длительности нажатия."""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    """Конструктор класса Target"""
    def __init__(self, screen: pygame.surface):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.color = RED
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(5, 50)
        self.death = 50
        self.attempts = 0
        self.vx = random.randint(-2,2)
        self.vy = random.randint(-2,2)
        self.t = 0
    

    def new_target(self):
        """ Инициализация новой цели. """
        self.death = 100
        x = self.x = random.randint(600, 780)
        y = self.y = random.randint(300, 550)
        r = self.r = random.randint(2, 50)
        vx = self.vx = random.randint(-2,2)
        vy = self.vy = random.randint(-2,2)
        color = self.color = RED
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
        self.live = 0

    def move(self):
        """Перемещает цель по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, 
        стен по краям окна (размер окна 800х600).
        """   
        T = 150
        self.t += 1
        if self.t % T == 0:
            self.vx = -self.vx
            self.vy = -self.vy
        if self.r >= (WIDTH - self.x):
            self.x = WIDTH - self.r
            self.vx = - self.vx
        if self.r >= (HEIGHT - self.y):
            self.y = HEIGHT - self.r
            self.vy = -self.vy
        self.y += self.vy
        self.x += self.vx

    def draw(self):
        """Отрисовка мишени."""
        if self.live == 1:
            pygame.draw.circle(
                self.screen,
                BLACK,
                (self.x, self.y),
                self.r+1
            )
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

    def alive(self):
        """Уменьшает счетчик каждую единицу времени после попадания в мишень.
        Returns:
            Возвращает True, если счетчик дошел до нуля.
        """
        if self.live != 1:
            self.death -= 1
        if self.death <= 0:
            return True
    
    def show_points(self):
        """Вывод количества очков (числа попаданий в мишени) на экран."""
        pygame.draw.rect(
            self.screen, 
            (255,255,255), 
            (0, 0, 120, 30)
        )
        points = 'Points: ' + str(self.points)
        sur_points = pygame.font.Font(None, 30)
        points = sur_points.render(points, True, BLACK)
        self.screen.blit(points, (10, 10))
       

    def show_attempts(self, bullet):
        """Вывод количества попыток на экран."""
        if self.death < 100:
            pygame.draw.rect(
            self.screen, 
            (255,255,255),
             (600, 0, 200, 30)
        )
            attempts = bullet
            attempts = 'Attempts: ' + str(attempts)
            sur_attempts = pygame.font.Font(None, 30)
            attempts = sur_attempts.render(attempts, True, BLACK)
            self.screen.blit(attempts, (600, 10))
            
    


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
flag = 0
flag1 = 0

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    target.show_points()
    target.move()
    if flag1 == 1:
        target.show_attempts(bullet)
    target.draw()
    if flag == 1:
        gun.draw(event_motion)
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            event_motion = event
            flag = 1
            


    for b in balls:
        b.move()
        b.alive()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.alive()
            flag1 = 1
        if b.alive() == False:
            balls.remove(b)
    if target.alive() == True:
        target.new_target()
    gun.power_up()

pygame.quit()