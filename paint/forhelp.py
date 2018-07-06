from pygame import * 
size=(800,600)
screen = display.set_mode(size) 
                                 
running = True
while running:
    for evt in event.get():  
        if evt.type == QUIT: 
            running = False

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    draw.rect(screen,(50,50,50),Rect(200,150,200,150),20)
    draw.rect(screen,(100,100,100),Rect(450,350,100,100),1)                        
    
    display.flip() 
quit()