# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:44:55 2019

@author: Marlom_Bey
"""

import nltk
import pygame

"""
    implementing nlp and diagram generator
"""


def drawRect(display_surface, black, class_name, x_start, y_start, x_next, y_next):
    
    rect_width = 200
    rect_height = 170
    
    pygame.draw.rect(display_surface, black, (x_start + x_next, y_start + y_next, rect_width, rect_height), 1)
    pygame.draw.line(display_surface, black, (x_start + x_next, y_start + y_next + 20), (x_start + x_next + rect_width - 1, y_start + y_next + 20), 1)
    
    font = pygame.font.SysFont('freesansbold.ttf', 20)
    textsurface = font.render(class_name, False, (0,0,0))
    display_surface.blit(textsurface, (x_start + x_next + 70, y_start + y_next + 5))
    
    textsurface = font.render('- Name: String', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + x_next + 30, y_start + y_next + 30))
    
    textsurface = font.render('- Phone: int', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + x_next + 30, y_start + y_next + 50))
    
    textsurface = font.render('- Email: String', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + x_next + 30, y_start + y_next + 70))
    
    pygame.draw.line(display_surface, black, (x_start + x_next, y_start + 90), (x_start + x_next + rect_width - 1, y_start + 90), 1)
    
    textsurface = font.render('+ AddCustomer()', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + x_next + 30, y_start + y_next + 100))
    
    textsurface = font.render('+ EditCustomer()', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + x_next + 30, y_start + y_next + 120))
    
    textsurface = font.render('+ DeleteCustomer()', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + x_next + 30, y_start + y_next + 140))



def begin_diagram(class_list):
    
    pygame.init()
    pygame.font.init()
    
    win_x = 1280    
    win_y = 720  
    x_start = 100
    y_start = 100
    x_next = 0
    y_next = 0
    x_count = 0
    y_count = 0
    
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    display_surface = pygame.display.set_mode((win_x,win_y))
    pygame.display.set_caption('Test')
    display_surface.fill(white)
    
    for c in class_list:
        
        if x_count == 4:
            x_count = 0
            x_next = 0
            y_next = y_next + 300
        
        if "NN" in c:
            temp = ''.join(c)
            drawRect(display_surface, black, temp, x_start, y_start, x_next, y_next)
            x_next = x_next + 300
            x_count = x_count + 1
            
    

    while True:
    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            pygame.display.update()


def begin_nlp():
    
    text = "A system shall allow the users to register by entering their username and password, In order to get an access to the system"
    print(text)
    
    tokens = nltk.word_tokenize(text)
    print(tokens)
    
    pos = nltk.pos_tag(tokens)
    n_list = []
    
    for p in pos:
        print(p)
        #q = ''.join(p)
    
        if "VB" in p:
            #verb = q.replace("VB","")
            n_list.append(p)
        elif "NN" in p:
            #noun = q.replace("NN","")
            n_list.append(p)
        elif "NNP" in p:
            #nounp = q.replace("NNP","")
            n_list.append(p)
        elif "NNS" in p:
            n_list.append(p)
            
    print(n_list)
    
    begin_diagram(n_list)



"""--------------------MAIN--------------------"""

if __name__ == "__main__":
    
    begin_nlp()
    