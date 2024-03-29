"""Contains the essential imports, functions and classes for the simulation logic."""

import math
import os
import sys
import time
import random
import copy

import pygame
from pygame.locals import * #Even though these are already imported, we simplify the namespace like this.

from settings import *

pygame.init()
screen = pygame.display.set_mode(size) #Get us that window
pygame.display.set_caption("The Flatland") #Give that window a name


def exit():
    """Exits the simulation"""
    pygame.quit()
    sys.exit()


def remove(l, who):
    """Removes all elements whose indexes appear in the [who] list from the [l] list"""
    offset = 0
    
    for i in who:
        l.pop(i + offset)
        offset -= 1
        
    return l
    

def rand (a, b):
    """Returns a random integer from the [a, b] interval."""
    return a + int(round(random.random()*(b - a)))
    

def collides (pos1, r1, pos2, r2):
    """Returns true if two circles are overlapping."""
    return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 <= (r1 + r2)**2

   
class Flatlander:
    """A creep is the simplest, and the only inhabitant of the Flatland. He is a red cricle on the screen. He likes green circles a lot."""
    def __init__(self, pos, genome, energy):
        self.pos = pos
        self.genome = genome
        self.r = genome["r"]
        self.energy = energy
        self.speed = [random.random()*0.5, random.random()*0.5]
        
        self.drawable = True #Flatlanders can be drawn on the screen, obviously
        
    def draw(self):
        pygame.draw.circle(screen, FLColor, [int(round(self.pos[0])), int(round(self.pos[1]))], int(round(self.r)))
        

class Food:
    def __init__(self, pos, size):
        self.pos = pos
        self.r = size

        self.drawable = True        
    def draw(self):
        pygame.draw.circle(screen, foodColor, self.pos, self.r)
    
