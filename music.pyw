import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import pandas as pd
import sys
import numpy as np
import os
#import warnings
import pyautogui
width, height = pyautogui.size()
from pygame import mixer

#warnings.filterwarnings("ignore")

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %((73.15*width)/100, (46.6*height)/100)
pygame.init()
i_icon = open(r"C:\Users\nagir\OneDrive\Desktop\r1.png")
pic1 = open(r"C:\Users\nagir\OneDrive\Desktop\rx.png")
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("music")
font = pygame.font.SysFont("Segoe UI ", 25)

theme = os.getcwd() + ".\entry_line.json"
manager = pygame_gui.UIManager((500, 500), theme)


text_input3 = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((250, 100), (200, 30)),
     manager = manager, object_id = ObjectID(class_id = "text_entry_line",
                                             object_id = '#main_text_entry3'))


clock = pygame.time.Clock()
data = pd.read_csv(r"C:\Users\nagir\OneDrive\Desktop\data_information.csv")
li = data["NAME"].tolist()
li1 = data["ID"].tolist()
li2 = data["PICTURE"].tolist()
text1 = ''
text2 = ''
li = li
li1 = li1
li2 = li2
id_ = ''
mixer.init()
pic = ''
SCREEN.fill((255,255,255))
class main():

    def username():
        global X, Y, li, li1, li2, id_, text1, text2, pic, pic1
        
        while True:

            UI_REFRESH_RATE = clock.tick(60) / 1000
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry3'):
                    text1 = str(event.text)

                    if text1 in li:
                        n = li.index(text1)
                        id_ = str(li1[n])
                        pic = str(li2[n])
                        imp = pygame.image.load(pic).convert()
                        SCREEN.fill((255,255,255))
                        SCREEN.blit(imp, (250, 200))
                        mixer.init()
                        mixer.music.load(id_)
                        mixer.music.set_volume(0.3)
                        mixer.music.play()
                        
 

                    else:
                        mixer.music.load(r"C:\Users\nagir\OneDrive\Desktop\music.mp3")
                        imp = pygame.image.load(pic1).convert()
                        SCREEN.fill((255,255,255))
                        SCREEN.blit(imp, (250, 200))
                        mixer.music.set_volume(0.3)
                        mixer.music.play()    

                manager.process_events(event)
             
            manager.update(UI_REFRESH_RATE)
    
            textname = font.render("Enter Song_Name", True, (96, 96, 96))
            SCREEN.blit(textname, (20, 100))
            textname = font.render(text1, True, (96, 96, 96))
            SCREEN.blit(textname, (250, 150))
            manager.draw_ui(SCREEN)
            pygame.display.update()
        
    username()

if name == "main":
    main()
