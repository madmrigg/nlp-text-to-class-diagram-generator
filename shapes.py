# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:08:25 2019

@author: Marlom_Bey
"""

"""
    generating class diagrams
"""

import pygame


def drawRect(display_surface, black, x_start, y_start):
    
    rect_width = 200
    rect_height = 170
    
    pygame.draw.rect(display_surface, black, (x_start, y_start, rect_width, rect_height), 1)
    pygame.draw.line(display_surface, black, (x_start, y_start + 20), (x_start + rect_width - 1, y_start + 20), 1)
    
    font = pygame.font.SysFont('freesansbold.ttf', 20)
    textsurface = font.render('Customer', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + 70, y_start + 5))
    
    textsurface = font.render('- Name: String', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + 30, y_start + 30))
    
    textsurface = font.render('- Phone: int', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + 30, y_start + 50))
    
    textsurface = font.render('- Email: String', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + 30, y_start + 70))
    
    pygame.draw.line(display_surface, black, (x_start, y_start + 90), (x_start + rect_width - 1, y_start + 90), 1)
    
    textsurface = font.render('+ AddCustomer()', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + 30, y_start + 100))
    
    textsurface = font.render('+ EditCustomer()', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + 30, y_start + 120))
    
    textsurface = font.render('+ DeleteCustomer()', False, (0,0,0))
    display_surface.blit(textsurface, (x_start + 30, y_start + 140))
    
    
        
if __name__ == "__main__":
    
    pygame.init()
    pygame.font.init()
    
    x_win = 1280    
    y_win = 720
    x_start = 100
    y_start = 100    
    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    
    display_surface = pygame.display.set_mode((x_win,y_win))
    pygame.display.set_caption('Test')
    display_surface.fill(white)
    
    drawRect(display_surface, black, x_start, y_start)
    drawRect(display_surface, black, x_start + 300, y_start)
    drawRect(display_surface, black, x_start + 600, y_start)
    #drawRect(display_surface, black, x_start, y_start + 300)
    #drawRect(display_surface, black, x_start + 600, y_start + 300)
    

    while True:
    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            pygame.display.update()


