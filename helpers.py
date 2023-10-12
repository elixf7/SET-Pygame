"""Defines the class of Cards"""

import pygame
import os
import sys


WIDTH, HEIGHT = 1400, 900

class Card:
    image = None
    shape = int
    number_of_shapes = int
    color = int
    shading = int

    def __init__(self, image, shape, number_of_shapes, color, shading):
        self.image = pygame.transform.scale(image, (141, 215))
        self.shape = shape
        self.number_of_shapes = number_of_shapes
        self.color = color
        self.shading = shading


# COLOR: RED = 1, GREEN = 2, PURPLE = 3
# NUMBER OF SHAPES: 1,2,3
# SHAPE: OVAL = 1, DIAMOND = 2, NOODLE = 3
# SHADING: CLEAR = 1, CHECK = 2, SOLID = 3
config_name = 'myapp.cfg'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    this_dir = os.path.dirname(sys.executable)
elif __file__:
    this_dir = os.path.dirname(__file__)


practice_deck = {
    
}

practice_deck[1] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.30.03 PM.png')), 1, 3, 2, 1) 
practice_deck[2] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.30.33 PM.png')), 1, 3, 1, 1) 
practice_deck[3] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.31.03 PM.png')), 1, 3, 3, 1) 

practice_deck[4] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.40.00 PM.png')), 2, 3, 2, 1) 
practice_deck[5] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.40.20 PM.png')), 2, 3, 1, 1)  
practice_deck[6] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.40.36 PM.png')), 2, 3, 3, 1) 

practice_deck[7] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.54.05 PM.png')), 3, 3, 2, 1) 
practice_deck[8] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.54.22 PM.png')), 3, 3, 1, 1) 
practice_deck[9] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.54.39 PM.png')), 3, 3, 3, 1) 

practice_deck[10] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.55.36 PM.png')), 1, 3, 2, 3) 
practice_deck[11] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.55.53 PM.png')), 1, 3, 1, 3) 
practice_deck[12] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.56.12 PM.png')), 1, 3, 3, 3) 

practice_deck[13] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.56.31 PM.png')), 2, 3, 3, 3) 
practice_deck[14] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.56.52 PM.png')), 2, 3, 2, 3) 
practice_deck[15] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.57.11 PM.png')), 2, 3, 1, 3) 

practice_deck[16] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.57.40 PM.png')), 3, 3, 3, 3) 
practice_deck[17] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.57.58 PM.png')), 3, 3, 2, 3) 
practice_deck[18] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 2.58.18 PM.png')), 3, 3, 1, 3) 

practice_deck[19] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.13.59 PM.png')), 1, 3, 1, 2) 
practice_deck[20] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.14.18 PM.png')), 1, 3, 2, 2) 
practice_deck[21] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.14.39 PM.png')), 1, 3, 3, 2) 

practice_deck[22] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.15.06 PM.png')), 2, 3, 1, 2) 
practice_deck[23] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.15.21 PM.png')), 2, 3, 2, 2) 
practice_deck[24] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.15.39 PM.png')), 2, 3, 3, 2) 

practice_deck[25] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.15.56 PM.png')), 3, 3, 1, 2) 
practice_deck[26] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.16.13 PM.png')), 3, 3, 2, 2) 
practice_deck[27] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.16.33 PM.png')), 3, 3, 3, 2) 

practice_deck[28] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.19.03 PM.png')), 1, 2, 3, 2) 
practice_deck[29] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.19.26 PM.png')), 1, 2, 2, 2) 
practice_deck[30] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.19.44 PM.png')), 1, 2, 1, 2) 

practice_deck[31] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.19.58 PM.png')), 2, 2, 3, 2) 
practice_deck[32] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.20.14 PM.png')), 2, 2, 2, 2) 
practice_deck[33] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.20.29 PM.png')), 2, 2, 1, 2) 

practice_deck[34] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.20.42 PM.png')), 3, 2, 3, 2) 
practice_deck[35] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.20.59 PM.png')), 3, 2, 2, 2) 
practice_deck[36] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.21.17 PM.png')), 3, 2, 1, 2) 

practice_deck[37] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.21.35 PM.png')), 1, 2, 1, 1) 
practice_deck[38] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.21.58 PM.png')), 1, 2, 2, 1) 
practice_deck[39] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.22.13 PM.png')), 1, 2, 3, 1) 

practice_deck[40] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.22.25 PM.png')), 2, 2, 1, 1) 
practice_deck[41] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.22.41 PM.png')), 2, 2, 2, 1) 
practice_deck[42] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.22.57 PM.png')), 2, 2, 3, 1) 

practice_deck[43] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.23.12 PM.png')), 3, 2, 1, 1) 
practice_deck[44] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.23.27 PM.png')), 3, 2, 2, 1) 
practice_deck[45] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.23.41 PM.png')), 3, 2, 3, 1) 

practice_deck[46] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.24.02 PM.png')), 1, 2, 3, 3) 
practice_deck[47] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.24.17 PM.png')), 1, 2, 2, 3) 
practice_deck[48] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.24.33 PM.png')), 1, 2, 1, 3) 

practice_deck[49] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.25.00 PM.png')), 2, 2, 3, 3) 
practice_deck[50] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.25.18 PM.png')), 2, 2, 2, 3) 
practice_deck[51] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.25.34 PM.png')), 2, 2, 1, 3) 

practice_deck[52] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.25.55 PM.png')), 3, 2, 3, 3) 
practice_deck[53] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.26.19 PM.png')), 3, 2, 2, 3) 
practice_deck[54] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.26.36 PM.png')), 3, 2, 1, 3) 

practice_deck[55] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.29.36 PM.png')), 1, 1, 1, 3) 
practice_deck[56] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.31.31 PM.png')), 1, 1, 2, 3) 
practice_deck[57] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.31.47 PM.png')), 1, 1, 3, 3) 

practice_deck[58] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.32.51 PM.png')), 2, 1, 1, 3) 
practice_deck[59] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.33.03 PM.png')), 2, 1, 2, 3) 
practice_deck[60] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.33.17 PM.png')), 2, 1, 3, 3) 

practice_deck[61] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.33.37 PM.png')), 3, 1, 1, 3) 
practice_deck[62] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.33.49 PM.png')), 3, 1, 2, 3) 
practice_deck[63] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.34.05 PM.png')), 3, 1, 3, 3) 

practice_deck[64] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.34.43 PM.png')), 1, 1, 3, 1) 
practice_deck[65] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.34.53 PM.png')), 1, 1, 2, 1) 
practice_deck[66] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.35.06 PM.png')), 1, 1, 1, 1) 

practice_deck[67] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.35.20 PM.png')), 2, 1, 3, 1) 
practice_deck[68] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.35.31 PM.png')), 2, 1, 2, 1) 
practice_deck[69] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.35.43 PM.png')), 2, 1, 1, 1) 

practice_deck[70] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.35.58 PM.png')), 3, 1, 3, 1) 
practice_deck[71] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.36.10 PM.png')), 3, 1, 2, 1) 
practice_deck[72] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.36.50 PM.png')), 3, 1, 1, 1) 

practice_deck[73] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.37.10 PM.png')), 1, 1, 1, 2) 
practice_deck[74] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.37.24 PM.png')), 1, 1, 2, 2) 
practice_deck[75] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.37.37 PM.png')), 1, 1, 3, 2) 

practice_deck[76] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.37.50 PM.png')), 2, 1, 1, 2) 
practice_deck[77] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.38.05 PM.png')), 2, 1, 2, 2) 
practice_deck[78] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.38.18 PM.png')), 2, 1, 3, 2) 

practice_deck[79] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.38.32 PM.png')), 3, 1, 1, 2) 
practice_deck[80] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.38.48 PM.png')), 3, 1, 2, 2) 
practice_deck[81] = Card(pygame.image.load(os.path.join(this_dir,   'Set Cards', 'Screen Shot 2022-07-13 at 3.39.01 PM.png')), 3, 1, 3, 2) 

# print(this_dir)

