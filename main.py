#!/usr/bin/python

import os
import sys
import csv

import pygame
import pymunk
import pymunk.pygame_util
import random
from time import sleep

from gobject import *
from gresource import *

TITLE_STR = "Ping Pong"

INFO_HEIGHT = 40
INFO_OFFSET = 10
INFO_FONT = 14

BAR_WIDTH = 60

def draw_info() :
    font = pygame.font.SysFont('Verdana', INFO_FONT)
    info = font.render('F1/F2 : Load/Save file    space : toggle', True, COLOR_BLACK)

    pygame.draw.rect(gctrl.surface, COLOR_PURPLE, (0, gctrl.height - INFO_HEIGHT, gctrl.width, INFO_HEIGHT))
    gctrl.surface.blit(info, (INFO_OFFSET * 2, gctrl.height - 2 * INFO_FONT - INFO_OFFSET)) 

def draw_message(str) :
    gctrl.draw_string(str, 0, 0, ALIGN_CENTER, 40, COLOR_BLACK)
    
    pygame.display.update()
    sleep(2)

def terminate() :
    pygame.quit()
    sys.exit()

def start_game() :
    draw_options = pymunk.pygame_util.DrawOptions(gctrl.surface)

    centerx = gctrl.width / 2
    centery = gctrl.height / 2

    sx = 5
    sy = 5
    ex = gctrl.width - 5
    ey = gctrl.height - 5
    
    walls = []
    walls.append(wall_object((sx, sy), (sx, ey), VWALL_COLLISION_TYPE))
    walls.append(wall_object((ex, ey), (ex, sy), VWALL_COLLISION_TYPE))    
    walls.append(wall_object((sx, sy), (ex, sy), HWALL_COLLISION_TYPE))
    walls.append(wall_object((sx, ey), (ex, ey), HWALL_COLLISION_TYPE))

    for object in walls :
        gctrl.space.add(object.body, object.shape)
    
    bar_sy = centery - (BAR_WIDTH / 2)
    bar_ey = centery + (BAR_WIDTH / 2)
    bar1_x = 30
    bar2_x = gctrl.width - 30

    bars = []
    bars.append(bar_object((bar1_x, bar_sy), (bar1_x, bar_ey), BAR1_COLLISION_TYPE))
    bars.append(bar_object((bar2_x, bar_sy), (bar2_x, bar_ey), BAR2_COLLISION_TYPE))

    for object in bars :
        gctrl.space.add(object.body, object.shape)

    ball = ball_object((centerx, centery))
    gctrl.space.add(ball.body, ball.shape)

    coll_handler1 = gctrl.space.add_collision_handler(BALL_COLLISION_TYPE, VWALL_COLLISION_TYPE)
    coll_handler1.begin = ball.coll_begin

    coll_handler2 = gctrl.space.add_collision_handler(BAR1_COLLISION_TYPE, HWALL_COLLISION_TYPE)
    coll_handler2.begin = bars[0].coll_begin

    coll_handler3 = gctrl.space.add_collision_handler(BAR2_COLLISION_TYPE, HWALL_COLLISION_TYPE)
    coll_handler3.begin = bars[1].coll_begin

    running = True
    while running:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                continue

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q :
                    (x, y) = bars[0].get_position_a()
                    if y > 10 :
                        bars[0].set_velociy(0, -400)
                elif event.key == pygame.K_a :
                    (x, y) = bars[0].get_position_b()
                    if y < gctrl.height - 10 :
                        bars[0].set_velociy(0, 400)
                elif event.key == pygame.K_UP :
                    (x, y) = bars[1].get_position_a()
                    if y > 10 :
                        bars[1].set_velociy(0, -400)
                elif event.key == pygame.K_DOWN :
                    (x, y) = bars[1].get_position_b()
                    if y < gctrl.height - 10 :
                        bars[1].set_velociy(0, 400)
            elif event.type == pygame.KEYUP :
                if event.key == pygame.K_q :
                    bars[0].set_velociy(0, 0)
                elif event.key == pygame.K_a :
                    bars[0].set_velociy(0, 0)
                elif event.key == pygame.K_UP :
                    bars[1].set_velociy(0, 0)
                elif event.key == pygame.K_DOWN :
                    bars[1].set_velociy(0, 0)

        gctrl.surface.fill(COLOR_BLACK)

        gctrl.space.debug_draw(draw_options)

        pygame.display.flip()
        gctrl.space.step(1.0 / FPS)
        gctrl.clock.tick(FPS)

    pygame.quit()

def init_game() :
    pad_width = 800
    pad_height = 400

    gctrl.set_surface(pygame.display.set_mode((pad_width, pad_height)))
    pygame.display.set_caption(TITLE_STR)    

if __name__ == '__main__' :
    init_game()
    start_game()
