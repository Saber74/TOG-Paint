#stamps.py (using the mouse to stamp pictures)
from pygame import * 
size=(800,600)
screen = display.set_mode(size) 
myStamp=image.load("Wolhaiksong_crest.png")                              
running = True
while running:
    for evt in event.get():  
        if evt.type == QUIT: 
            running = False
        if evt.type==MOUSEBUTTONDOWN:
            backPic=screen.copy()#screen capture (screenshot)
            print("mouse down")
        if evt.type==MOUSEBUTTONUP:
            print("mouse up")

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if mb[0]==1:
        screen.blit(backPic,(0,0))
        screen.blit(myStamp,(mx,my))
                            
    
    display.flip() 
quit() 