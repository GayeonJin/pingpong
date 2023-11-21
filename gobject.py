#!/usr/bin/python

import pygame
import pymunk
import pymunk.pygame_util

BALL_COLLISION_TYPE = 1
VWALL_COLLISION_TYPE = 2
BAR1_COLLISION_TYPE = 3
BAR2_COLLISION_TYPE = 4
HWALL_COLLISION_TYPE = 5

class ball_object :
    def __init__(self, pos, radius = 10) :
        self.body = pymunk.Body()
        self.body.position = pos

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.collision_type = BALL_COLLISION_TYPE

    def set_position(self, pos) :
        self.body.position = pos

    def set_velociy(self, vel_x, vel_y) :
        self.body.velocity = (vel_x, vel_y)

class wall_object :
    def __init__(self, pos1, pos2, collision_type = None, radius = 2) :
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, pos1, pos2, radius)
        self.shape.elasticity = 1
        if collision_type != None :
            self.shape.collision_type = collision_type

class bar_object :
    def __init__(self, pos1, pos2, collision_type = None, radius = 4) :
        self.body = pymunk.Body(body_type = pymunk.Body.KINEMATIC)
        self.shape = pymunk.Segment(self.body, pos1, pos2, radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        if collision_type != None :
            self.shape.collision_type = collision_type

    def set_velociy(self, vel_x, vel_y) :
        self.body.velocity = (vel_x, vel_y)
        
    def get_position_a(self) :
        return self.body.local_to_world(self.shape.a)

    def get_position_b(self) :
        return self.body.local_to_world(self.shape.b)

if __name__ == '__main__' :
    print('pymunk object')