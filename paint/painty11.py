from pygame import * # all graphics programs we do will need this
from random import randint as a
from tkinter import*
from tkinter.colorchooser import*
from tkinter import filedialog
from math import *

root=Tk()
root.withdraw()
font.init()
info=0 ### rendering the font i picked 
text=""  ### text to be displayed for information
alphaColour=(0,0,10,15) ### colours for the alpha brush
#####preset colours
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(16, 80, 102)
WHITE=(255,255,255)
GREEN=(0,255,0)
#########
size=(1200,800)
screen = display.set_mode(size) # Will create an window. We will
width=5 # variabe used for size and width for tools such as eraser and brush
tool="no tool" ### variable used for selection of tools
col=BLACK ## initial variable for colour 

omx,omy=300,300 #used as an end position of mouse for 
stickerPage=1
toolPage=1
mp = 0 ###index of music list decides what song is on
stickerSize=6 ###variable to manipulate sticker size
shapesWidth=5 ###variable for width of shapes

########triangle tool function

 
def draw_triangle(surf, colour, rect, width): #inouts the user will put that will be used to decide everything regarding the triangle

    topleft=rect[0],rect[1] #point1
    topright=rect[2],rect[3]    #point2
    bottomleft=rect[2]//2+mx,rect[3]//2+my #point 3
    horiz = rect.inflate(5 , 0)#positioning and centering the line
    draw.line(surf, colour, horiz.topleft, horiz.topright, width) # ;line from point 1 to 2 
    vert = rect.inflate(1, -5 ) #positioning and centering the line
    draw.line(surf, colour, vert.topleft, vert.bottomleft, width) # line from point 1 to 3
    diag= rect.inflate(5,0) #positioning and centering the line
    draw.line(surf, colour, diag.topright, vert.bottomleft, width) # line from 2 to 3
 
##########rectangle tool function
def draw_rect(surf, colour, rect, width):
    # topleft=mx,my
    # topright=sx,my
    # bottomleft=mx,sy
    # bottomright=sx,sy
    topleft=rect[0],rect[1] #top left corner of rectangle point
    topright=rect[2],rect[1]    #top right corner of rectangle point
    bottomleft=rect[0],rect[3]#bottom left corner of rectangle point
    bottomright=rect[2],rect[3]#bottom right corner of rectangle point
    horiz = rect.inflate(shapesWidth-1 , -1) #positioning and centering the line
    draw.line(surf, colour, horiz.topleft, horiz.topright, width) #drawing a line from top left to to topright
    draw.line(surf, colour, horiz.bottomleft, horiz.bottomright, width) #line from bot left to bot right
    vert = rect.inflate(0, -shapesWidth ) #positioning and centering the line
    draw.line(surf, colour, vert.topleft, vert.bottomleft, width) #line from top left to bot left
    draw.line(surf, colour, vert.topright, vert.bottomright, width) #line from top right to bot right

################fill function
def fill(oldPos, newCol, updating=False):
    # Get old colour on pixel and make pixel list
    oldCol = screen.get_at(oldPos)
    pixList = [oldPos]
    allPixels = {oldPos}

    # While we have points to set
    while pixList:

            # Get a pixel and remove from list
            px, py = pixList.pop(0)

            # Change colour and update if necessary
            screen.set_at((px, py), newCol)
            if updating: display.update(canvasRect)

            # For each adjacent point, add to pixel list if it's like the old colour
            for ax, ay in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if px + ax in range(1000) and py + ay in range(1000):
                    newPos = (px + ax, py + ay)
                    if screen.get_at(newPos) == oldCol and newPos not in allPixels:
                        pixList.append(newPos)
                        allPixels.add(newPos)
######pictures    
canvasRect=Rect(120,80,700,500)
canvasBackgroundList=["white.png","ToG_(2).jpg","inverted_viole___tower_of_god_by_fullm3t41-d5kuw44.jpg","sticker16.jpg","white.png"]
# screen.blit(transform.scale(image.load(canvasBackgroundList[0]),(700,500)),(120,80))
sticker1=image.load("sticker1.jpg")
sticker2=image.load("sticker2.jpg")
sticker3=image.load("sticker3.jpg")
sticker4=image.load("sticker4.jpg")
sticker5=image.load("sticker5.jpg")
sticker6=image.load("sticker6.jpg")
sticker7=image.load("sticker7.jpg")
sticker8=image.load("sticker8.jpg")
sticker9=image.load("sticker9.jpg")
sticker10=image.load("sticker10.jpg")
sticker11=image.load("sticker11.jpg")
sticker12=image.load("sticker12.jpg")
sticker13=image.load("sticker13.jpg")
sticker14=image.load("sticker14.jpg")
sticker15=image.load("sticker15.jpg")
pencilPic=image.load("f6b3a3d2bd84463131bc8c55e2cd2bb6bf3fd83c_hq.jpg")
sprayPic=image.load("spray.jpg")
fillPic=image.load("fill.png")
colourPickerPic=image.load("colourPickers.png")
background2=image.load("background-dark.jpg")
eraserPic=image.load("c47bfab24b04f05a0f30f7d97729bd0c--bia.png")
brushPic=image.load("brush.jpg")
alphaBrushPic=image.load("alphabrush.png")
savePic=image.load("save.png")
loadPic=image.load("load.png")
toolshapesBackground=image.load("toolshapesPic.png.jpg")
gifnum=10 
######music list and playing the music
mixer.init()
musicList=["Greatest Battle Music Of All Times_ On The Battlefield.mp3","Ars.mp3","Fairy Tail OST IV (Disc.2) #16 - Pride of the Guild.mp3","Departure To The Frontlines [Extended].mp3","next to you.mp3","one piece.mp3","one piece two.mp3","lightning.mp3"]
mixer.music.load(musicList[mp])
mixer.music.play()
############starting animation or gif
##gifs=[]
##myClock = time.Clock()
##for t in range(10):
##    gifs.append(image.load("00"+str(t)+".png"))
##while gifnum<37:
##    gifs.append(image.load("0"+str(gifnum)+".png"))
##    gifnum+=1
##for gif in gifs:
##    screen.fill(0)
##    screen.blit(gif, (0,0))
##    display.flip()
##    myClock.tick(10)
##time.wait(1000)
##
##k=10
##pics = []
##
##for i in range(10):
##    pics.append(image.load("yura\\frame_0"+str(i)+"_delay-0.12s.png"))
##while k<16:
##    pics.append(image.load("yura\\frame_"+str(k)+"_delay-0.12s.png"))
##    k+=1
##for pic in pics:
##    screen.fill(0)
##    screen.blit(pic, (0,0))
##    display.flip()
##    myClock.tick(10)
##time.wait(1000)
##screen.fill(BLACK)
##display.flip()
 #background and entrance to paint
screen.blit(transform.scale(background2, (1200,800)),(0,0))
display.flip()       
##############################defining all RECTS
sticker1Rect=Rect(200,10,110,60)
sticker2Rect=Rect(320,10,110,60)
sticker3Rect=Rect(440,10,110,60)
sticker4Rect=Rect(560,10,110,60)
sticker5Rect=Rect(680,10,110,60)
canvasRect=Rect(120,80,700,500)
pencilRect=Rect(20,80,80,80)
eraserRect=Rect(20,170,80,80)
colourpickerRect=Rect(20,260,80,80)
sprayRect=Rect(20,350,80,80)
brushRect=Rect(20,440,80,80)
openRect=Rect(1050,620,100,100)
saveRect=Rect(1050,500,100,100)
fillRect=Rect(20,530,80,80)
alphaBrushRect=Rect(20,620,80,80) 
infoRect=Rect(220,610,540,70) #to display information
toolsRect=Rect(20,10,80,30) #to select tool shapes
shapesRect=Rect(20,45,80,30) #to select shapes page
detailsRect=(840,10,150,220) #shortcuts rect
widthmxmyRect=(1000,10,180,120) #####rect for the mx my and width
draw.rect(screen,WHITE,canvasRect)#drawing the canvas BEFORE the loop
        
########################surfaces
brushHead = Surface((20,20),SRCALPHA)
############################################

click=False
keyboard=False
running=True
cntrlz=[screen.copy(),screen.copy] #undo list
cntrly=[] #redolist
while running:
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed() ###mb --- mouse button                                     ###if mb[0]==1:
        keys=key.get_pressed()
        draw.circle(brushHead,alphaColour,(10,10),10) #drawing circle on the alpha hidden subsurface
        
        for evt in event.get(): 

                if evt.type == QUIT: 
                        running = False
                if evt.type == KEYDOWN:
                        if evt.key == K_ESCAPE:
                                running = False     
                if evt.type==MOUSEBUTTONUP:
                        copy=screen.copy()
                        cntrlz.append(copy) #when mouse button is released a screenshot is added to undo list
                        if toolPage==1:
                            ##########choosing colour
                            if colourpickerRect.collidepoint(mx,my):
                                tool="colourpicker"
                                c=askcolor(title="Pick Colour")
                                if c[0]!=None:
                                        col=c[0]
                                        alphaColour=(col[0],col[1],col[2],10)
                if evt.type==MOUSEBUTTONDOWN:
                        backPic=screen.copy() ##screenshot
                        click=True
                        sx,sy=mouse.get_pos() #mouse positions
                        ###clearing screen
                if mouse.get_pressed()[2]:
                    draw.rect(screen,WHITE,canvasRect,0)
                    
                if evt.type==KEYUP:
                        keyboard=True
        if evt.type == KEYUP:
            #####undo tool
                if keys[K_LCTRL] and keys[K_z] and keyboard:
                        if len(cntrlz)>1:
                            cntrly.append(cntrlz.pop())
                            screen.blit(cntrlz[-1],(0,0))
            #####redo
                if keys[K_LCTRL] and keys[K_y] and keyboard:
                        if len(cntrly) > 0:
                                screen.blit(cntrly[-1],(0,0))
                                cntrlz.append(cntrly.pop())
            ####increases size for width shapes width and stickers
                if keys[K_UP]:
                        if stickerSize<21:
                                stickerSize+=1
                        if width<30:
                                width+=1
                        if shapesWidth==4:
                            shapesWidth=5
                        if shapesWidth<19:
                            shapesWidth+=2
            ###decreases size for width shapes width and stickers
                if keys[K_DOWN]:
                        if stickerSize>6:
                                stickerSize-=1
                        if width>5 :
                                width-=2
                        if shapesWidth>5:
                                shapesWidth-=1
            ####flipping between sticker pages
                if keys[K_LEFT]:
                        if stickerPage>1:
                                stickerPage-=1
                        else:
                                stickerPage=3
            ####flipping between sticker pages
                if keys[K_RIGHT]:
                        if stickerPage<3:
                                stickerPage+=1
                        else:
                                stickerPage=1
            ####change to next song
                if keys[K_LCTRL] and keys[K_n] and keyboard:
                        if mp<7:
                                mp+=1
                        elif mp==7:
                                mp=0
                        mixer.music.load(musicList[mp])
                        mixer.music.play(-1)
            ####change to previous song
                if  keys[K_LCTRL] and keys[K_p] and keyboard:
                        if mp>0:
                                mp-=1
                        elif mp==0:
                                mp=7
                        mixer.music.load(musicList[mp])
                        mixer.music.play(-1)
            ###puases music
                if  keys[K_s]:
                        mixer.music.pause()
            ###starts the music after being puased
                if  keys[K_p]:
                        mixer.music.unpause()



#######makes sure music is always playing
        if mixer.music.get_busy()==False:
  
                mp+=1
                mixer.music.load(musicList[mp])
                mixer.music.play()
  
        
        ########drawing the tools
        draw.rect(screen,BLUE,pencilRect,2)
        draw.rect(screen,BLUE,eraserRect,2)
        draw.rect(screen,BLUE,colourpickerRect,2)
        draw.rect(screen,BLUE,sprayRect,2)
        draw.rect(screen,BLUE,brushRect,2)
        draw.rect(screen,BLUE,fillRect,2)
        draw.rect(screen,BLUE,saveRect,2)
        draw.rect(screen,BLUE,openRect,2)
        draw.rect(screen,(WHITE),infoRect,0)
        draw.rect(screen,(WHITE),detailsRect,0)
        draw.rect(screen,(WHITE),widthmxmyRect,0)
        if toolPage==1: #only create this rect if the page is 1 since there are not enough functionis in the second page
            draw.rect(screen,BLUE,alphaBrushRect,2)
########drawing stickers rects
        draw.rect(screen,BLUE,sticker1Rect,7)
        draw.rect(screen,BLUE,sticker2Rect,7)
        draw.rect(screen,BLUE,sticker3Rect,7)
        draw.rect(screen,BLUE,sticker4Rect,7)
        draw.rect(screen,BLUE,sticker5Rect,7)
####blitting right image for each sticker page
        if stickerPage==1:
                screen.blit(transform.scale(sticker1, (110,60)),(200,10))
                screen.blit(transform.scale(sticker2, (110,60)),(320,10))
                screen.blit(transform.scale(sticker3, (110,60)),(440,10))
                screen.blit(transform.scale(sticker4, (110,60)),(560,10))
                screen.blit(transform.scale(sticker5, (110,60)),(680,10))
        elif stickerPage==2:
                draw.rect(screen,WHITE,sticker1Rect,0)
                draw.rect(screen,WHITE,sticker2Rect,0)
                draw.rect(screen,WHITE,sticker3Rect,0)
                draw.rect(screen,WHITE,sticker4Rect,0)
                draw.rect(screen,WHITE,sticker5Rect,0)
                screen.blit(transform.scale(sticker6,(110,60)),(200,10))
                screen.blit(transform.scale(sticker7,(110,60)),(320,10))
                screen.blit(transform.scale(sticker8,(110,60)),(440,10))
                screen.blit(transform.scale(sticker9,(110,60)),(560,10))
                screen.blit(transform.scale(sticker10,(110,60)),(680,10))
        elif stickerPage==3:
                draw.rect(screen,WHITE,sticker1Rect,0)
                draw.rect(screen,WHITE,sticker2Rect,0)
                draw.rect(screen,WHITE,sticker3Rect,0)
                draw.rect(screen,WHITE,sticker4Rect,0)
                draw.rect(screen,WHITE,sticker5Rect,0)
                screen.blit(transform.scale(sticker11,(110,60)),(200,10))
                screen.blit(transform.scale(sticker12,(110,60)),(320,10))
                screen.blit(transform.scale(sticker13,(110,60)),(440,10))
                screen.blit(transform.scale(sticker14,(110,60)),(560,10))
                screen.blit(transform.scale(sticker15,(110,60)),(680,10))
########changes layout and images according to tool page
        if toolPage==1: ####drawing the rectangles to cover the images created before from the other page
                draw.rect(screen,BLUE,pencilRect,0)
                draw.rect(screen,BLUE,alphaBrushRect,0)
                draw.rect(screen,BLUE,eraserRect,0)
                draw.rect(screen,BLUE,colourpickerRect,0)
                draw.rect(screen,BLUE,sprayRect,0)
                draw.rect(screen,BLUE,brushRect,0)
                draw.rect(screen,BLUE,fillRect,0)
                draw.rect(screen,RED,toolsRect,2)
                ######blitting in the mages in the appropriate squares so user know which tool is which
                screen.blit(transform.scale(pencilPic, (81,86)),(20,75))
                screen.blit(transform.scale(eraserPic, (78,80)),(22,170))
                screen.blit(transform.scale(colourPickerPic, (78,80)),(22,260))
                screen.blit(transform.scale(alphaBrushPic, (78,80)),(22,620))
                screen.blit(transform.scale(brushPic, (78,80)),(22,440))
                screen.blit(transform.scale(fillPic, (78,80)),(22,530))
                screen.blit(transform.scale(sprayPic,(78,80)),(22,350))
        elif toolPage==2:
            ####drawing the rectangles to cover the images created before from the other page
                draw.rect(screen,BLUE,pencilRect,0)
                draw.rect(screen,BLUE,eraserRect,0)
                draw.rect(screen,BLUE,colourpickerRect,0)
                draw.rect(screen,BLUE,sprayRect,0)
                draw.rect(screen,BLUE,brushRect,0)
                draw.rect(screen,BLUE,fillRect,0)
                draw.rect(screen,RED,shapesRect,2)
                ##########drawing the shapes each in the box to select their function
                draw.rect(screen,BLACK,(20,620,81,81),0)
                draw.rect(screen,col,Rect(35,95,50,50),0)
                draw.ellipse(screen,col,Rect(35,185,50,50),0)
                draw_rect(screen,col,Rect(35,275,50,50),shapesWidth)

                for i in range(4):     # loop for drawing ellipse 
                    ellRect = Rect(35+i,370,50,50)
                    ellRect = Rect(35-i,370,50,50)
                    ellRect = Rect(35,370+i,50,50)
                    ellRect = Rect(35,370-i,50,50)
                    ellRect.normalize()
                    draw.ellipse(screen,col,ellRect,shapesWidth)
                draw.line(screen,col,(35,480),(85,480),shapesWidth)
                draw_triangle(screen,col,Rect(35,540,50,50),5)
###blitting images for golden backgournd for tool+shapes and save+load
        screen.blit(transform.scale(savePic,(100,100)),(1050,500))
        screen.blit(transform.scale(loadPic,(100,100)),(1050,620))
        screen.blit(transform.scale(toolshapesBackground,(81,31)),(20,10))
        screen.blit(transform.scale(toolshapesBackground,(81,31)),(20,45))

                
        #####selecting the tools
                        
        if mb[0]==1:#checking left click
                if toolPage==1:
                    if pencilRect.collidepoint(mx,my):
                            tool="pencil"
                    elif eraserRect.collidepoint(mx,my):
                            tool="eraser"
                    elif sprayRect.collidepoint(mx,my):
                            tool="spray"
                    elif brushRect.collidepoint(mx,my):
                            tool="brush"
                    elif alphaBrushRect.collidepoint(mx,my):
                            tool="alphaBrush"
                    elif fillRect.collidepoint(mx,my):
                            tool="fill"
                if toolPage==2:
                    if pencilRect.collidepoint(mx,my):
                            tool="filled rectangle"
                    elif eraserRect.collidepoint(mx,my):
                            tool="filled ellipse"
                    elif sprayRect.collidepoint(mx,my):
                            tool="ellipse"
                    elif brushRect.collidepoint(mx,my):
                            tool="line"
                    elif alphaBrushRect.collidepoint(mx,my):
                            tool="no tool"
                    elif fillRect.collidepoint(mx,my):
                            tool="triangle"
                    elif colourpickerRect.collidepoint(mx,my):
                            tool="rectangle"
                if shapesRect.collidepoint(mx,my):
                        tool="shapes"
                        toolPage=2
                elif toolsRect.collidepoint(mx,my):
                        tool="tool" 
                        toolPage=1
                elif saveRect.collidepoint(mx,my):
                        try:    
                                fname=filedialog.asksaveasfilename() 
                                image.save(screen.subsurface(canvasRect),fname)
                        except:
                                print("Saving error")
                elif openRect.collidepoint(mx,my):
                        try:
                                fname=filedialog.askopenfilename()
                                loadedImage=image.load(fname)
                                w=loadedImage.get_size()[0]#finds width
                                h=loadedImage.get_size()[1]#finds height
                                if w>450 or h>600:#if image is too big in either direction
                                    loadedImageSmall=transform.scale(loadedImage,(700,500))#image changed to fit screen
                                    screen.blit(loadedImageSmall,canvasRect)
                                else:
                                    screen.blit(loadedImage,canvasRect) #original image

                        except:
                            print("doesn't exist")

                        if sticker1Rect.collidepoint(mx,my):
                                tool="sticker1"
                        elif sticker2Rect.collidepoint(mx,my):
                                tool="sticker2"
                        elif sticker3Rect.collidepoint(mx,my):
                                tool="sticker3"
                        elif sticker4Rect.collidepoint(mx,my):
                                tool="sticker4"
                        elif sticker5Rect.collidepoint(mx,my):
                                tool="sticker5"
                elif stickerPage==1:
                        if sticker1Rect.collidepoint(mx,my):
                                tool="sticker1"
                        elif sticker2Rect.collidepoint(mx,my):
                                tool="sticker2"
                        elif sticker3Rect.collidepoint(mx,my):
                                tool="sticker3"
                        elif sticker4Rect.collidepoint(mx,my):
                                tool="sticker4"
                        elif sticker5Rect.collidepoint(mx,my):
                                tool="sticker5"
                elif stickerPage==2:
                        if sticker1Rect.collidepoint(mx,my):
                                tool="sticker6"
                        elif sticker2Rect.collidepoint(mx,my):
                                tool="sticker7"
                        elif sticker3Rect.collidepoint(mx,my):
                                tool="sticker8"
                        elif sticker4Rect.collidepoint(mx,my):
                                tool="sticker9"
                        elif sticker5Rect.collidepoint(mx,my):
                                tool="sticker10"
                elif stickerPage==3:
                        if sticker1Rect.collidepoint(mx,my):
                                tool="sticker11"
                        elif sticker2Rect.collidepoint(mx,my):
                                tool="sticker12"
                        elif sticker3Rect.collidepoint(mx,my):
                                tool="sticker13"
                        elif sticker4Rect.collidepoint(mx,my):
                                tool="sticker14"
                        elif sticker5Rect.collidepoint(mx,my):
                                tool="sticker15"

        ######using the selected tool
        if mb[0]==1:
                if canvasRect.collidepoint(mx,my):#clicked on canvasa
                        screen.set_clip(canvasRect)#only allows the CANVAS to be modified
                        if tool=="pencil":
                                draw.aaline(screen,col,(omx,omy),(mx,my),100)
                        elif tool=="eraser":  
                                dx=mx-omx
                                dy=my-omy
                                dist=int(sqrt(dx**2+dy**2))
                                for i in range(1,dist+1):
                                        xc=int(omx+i*dx/dist)
                                        yc=int(omy+i*dy/dist)
                                        draw.circle(screen,WHITE,(xc,yc),width,0)
                                draw.circle(screen,WHITE,(mx,my),width,0)

                        elif tool=="spray":
                            for i in range(30):
                                dx = a(-10,10)
                                dy = a(-10,10)
                                if hypot(dx,dy) <=10:
                                    draw.circle(screen,col,(mx+dx,my+dy),0)


                        elif tool=="brush":
                                dx=mx-omx
                                dy=my-omy
                                dist=int(sqrt(dx**2+dy**2))
                                for i in range(1,dist+1):
                                        xc=int(omx+i*dx/dist)
                                        yc=int(omy+i*dy/dist)
                                        draw.circle(screen,col,(xc,yc),width,0)
                                draw.circle(screen,col,(mx,my),width,0)
                        elif tool=="alphaBrush":
                                dx=mx-omx
                                dy=my-omy
                                dist=int(sqrt(dx**2+dy**2))
                                for i in range(1,dist+1):
                                        xc=int(omx+i*dx/dist)
                                        yc=int(omy+i*dy/dist)
                                        screen.blit(brushHead,(xc,yc))
                                screen.blit(brushHead,(mx,my))
                        elif tool=="fill":
                                fill((mx,my),col)
                        elif tool=="line":
                            screen.blit(backPic,(0,0))
                            draw.line(screen,col,(mx,my),(sx,sy),width)
                        elif tool=="rectangle":
                            screen.blit(backPic,(0,0))
                            ellRect=Rect(mx,my,(sx-mx),(sy-my))
                            ellRect.normalize()
                            draw_rect(screen,col,ellRect,shapesWidth) ##using rectangle function where lines are drawn
                        elif tool=="filled rectangle":
                            screen.blit(backPic,(0,0))
                            draw.rect(screen,col,Rect(mx,my,(sx-mx),(sy-my)),0)
                        elif tool=="filled ellipse":
                            screen.blit(backPic,(0,0))
                            ellRect=Rect(mx,my,(sx-mx),(sy-my))
                            ellRect.normalize() #to make an increase in the oppiste direction possible(draging ellipse left after starting on right)
                            draw.ellipse(screen,col,ellRect,0)
                        # elif tool=="ellipse":
                        #   screen.blit(backPic,(0,0))
                        elif tool == "ellipse":             
                            screen.fill((0,0,0))
                            screen.blit(backPic,(0,0))
                            radx = (mx-sx)
                            rady = (my-sy)

                            try:
                                for i in range(4):     ## put it in a loop for better results 
                                    ellRect = Rect(sx+i,sy,radx,rady)
                                    ellRect = Rect(sx-i,sy,radx,rady)
                                    ellRect = Rect(sx,sy+i,radx,rady)
                                    ellRect = Rect(sx,sy-i,radx,rady)
                                    ellRect.normalize()
                                    draw.ellipse(screen,col,ellRect,shapesWidth)

                            except:
                                pass

                        elif tool=="triangle":
                            screen.blit(backPic,(0,0))
                            ellRect=Rect(mx,my,(sx-mx),(sy-my))
                            ellRect.normalize()
                            draw_triangle(screen,col,ellRect,5) ##uses triangle function to draw a triangle

                                


                ### using stickers
                        elif tool=="sticker1":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker1, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker2":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker2, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker3":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker3, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker4":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker4, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker5":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker5, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker6":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker6, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker7":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker7, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker8":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker8, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker9":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker9, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker10":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker10, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker11":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker11, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker12":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker12, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker13":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker13, (40*stickerSize,30*stickerSize)),(mx-0.5*(40*stickerSize),my-0.5*(30*stickerSize)))
                        elif tool=="sticker14":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker14, (33*stickerSize,20*stickerSize)),(mx-0.5*(33*stickerSize),my-0.5*(20*stickerSize)))
                        elif tool=="sticker15":
                                screen.blit(backPic,(0,0))
                                screen.blit(transform.scale(sticker15, (50*stickerSize,35*stickerSize)),(mx-0.5*(50*stickerSize),my-0.5*(35*stickerSize)))




                        screen.set_clip(None)#EVERYTHING can be modoot = Tk
        #####changing squares colour and info on information bar for each tool
        ###text variable changes between diffrent tools and all boxes in use are highlighted
        ####text is blitted after being rendered
        ####multiple lines require the repeating of the whole procedure but blitting under

        if tool=="pencil":
                draw.rect(screen,RED,pencilRect,2)
                text=str("This is the Thorn Of The King it allows its user to create lines")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="eraser":
                draw.rect(screen,RED,eraserRect,2)
                text=str("The Poo Poo Wool grants its user the ability to erase things from existance")
                text2=str("Use it wisely. Press up to get a bigger circle and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        elif tool=="colourpicker":
                draw.rect(screen,RED,colourpickerRect,2)
                text=str("This glorious items grants its user the ability to choose a colour")
                text2=str("of their liking to use in their creations")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        elif tool=="spray":
                draw.rect(screen,RED,sprayRect,2)
                text=str("This tool allows the user to spray multiple points at once allowing more surface")
                text2=str("coverage. Press up to increase the width and down to decrease it")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        elif tool=="fill":
                draw.rect(screen,RED,fillRect,2)
                text=str("This tool allows the user to fill up shapes, and surfaces")
                text2=str("It fills using the current colour")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))                



        elif tool=="brush":
                draw.rect(screen,RED,brushRect,2)           
                text=str("The mighty brush is an enhanced version of the thorn as it allows the user to create")
                text2=str("bigger and thicker lines. Press up to increase the width and down to decrease it")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        elif tool=="alphaBrush":
                draw.rect(screen,RED,alphaBrushRect,2)
                text=str("The alphaBrush is a conceptual weapon based on the brush, it allows its user")
                text2=str("to create lines, similar to those of the brush, yet lighter in colour.")
                text3=str("Press up to get more width and down to reduce width")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                info3=myFont.render(text3,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
                screen.blit(info3,(240,650))
        elif tool=="sticker1":
                draw.rect(screen,RED,sticker1Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker2":
                draw.rect(screen,RED,sticker2Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker3":
                draw.rect(screen,RED,sticker3Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker4":
                draw.rect(screen,RED,sticker4Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker5":
                draw.rect(screen,RED,sticker5Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker6":
                draw.rect(screen,RED,sticker1Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker7":
                draw.rect(screen,RED,sticker2Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker8":
                draw.rect(screen,RED,sticker3Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker9":
                draw.rect(screen,RED,sticker4Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker10":
                draw.rect(screen,RED,sticker5Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker11":
                draw.rect(screen,RED,sticker1Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker12":
                draw.rect(screen,RED,sticker2Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker13":
                draw.rect(screen,RED,sticker3Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker14":
                draw.rect(screen,RED,sticker4Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="sticker15":
                draw.rect(screen,RED,sticker5Rect,7)
                text=str("Press up to get a bigger sticker and down for a smaller one")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="filled rectangle":
                draw.rect(screen,RED,pencilRect,2)
                text=str("Allows itsuser to draw a filled rectangle.")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="filled ellipse":
                draw.rect(screen,RED,eraserRect,2)
                text=str("Allows its user to draw a filled ellipse.")
                info=myFont.render(text,True,(0,0,200))
                screen.blit(info,(240,610))
        elif tool=="rectangle":
                draw.rect(screen,RED,colourpickerRect,2)
                text=str("Allows its user to draw an empty rectangle.")
                text2=str("Press up to get more width and press down to decrease width")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        elif tool=="ellipse":
                draw.rect(screen,RED,sprayRect,2)
                text=str("Allows its user to draw an empty ellipse.")
                text2=str("Press up to get more width and press down to decrease width")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        elif tool=="line":
                draw.rect(screen,RED,brushRect,2)
                text=str("Allows its user to draw a sraight line.")
                text2=str("Press up to get more width and press down to decrease width")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        elif tool=="triangle":
                draw.rect(screen,RED,fillRect,2)
                text=str("Allows its user to draw a triangle.")
                text2=str("Press up for more width and press down to decrease width")
                info=myFont.render(text,True,(0,0,200))
                info2=myFont.render(text2,True,(0,0,200))
                screen.blit(info,(240,610))
                screen.blit(info2,(240,630))
        ###deciding what font to use
        myFont=font.SysFont("Arial",16) #information
        myFont1=font.SysFont('Arial',13) #shortcuts
        myFont2=font.SysFont('Arial',18) #professional infortamyion


        ##############blitting the text for the 2 pages of tools
        toolText=str("tools")
        shapesText=str("shapes")
        context1=myFont.render(toolText,True,(0,0,200))
        context2=myFont.render(shapesText,True,(0,0,200))
        screen.blit(context1,(45,17))
        screen.blit(context2,(40,50))
        ################ the shotcuts help page 
        detailsText=("shortcuts:")
        detailsText5=str("sticker pages:right or left arrow")
        detailsContext=myFont1.render(detailsText,True,(255,0,0))
        detailsContext5=myFont1.render(detailsText5,True,(0,0,200))
        screen.blit(detailsContext,(890,10))
        screen.blit(detailsContext5,(840,110))
        detailsText1=("next song : Press cntrl+n")
        detailsText2=str("previous song: Press cntrl+p")
        detailsContext1=myFont1.render(detailsText1,True,(0,0,200))
        detailsContext2=myFont1.render(detailsText2,True,(0,0,200))
        screen.blit(detailsContext1,(840,30))
        screen.blit(detailsContext2,(840,50))
        detailsText3=("stop the music: Press s")
        detailsText4=str("play the music: Press p ")
        detailsContext3=myFont1.render(detailsText3,True,(0,0,200))
        detailsContext4=myFont1.render(detailsText4,True,(0,0,200))
        screen.blit(detailsContext3,(840,70))
        screen.blit(detailsContext4,(840,90))
        detailsText6=("Up arrow for more width")
        detailsText7=str("Down arrow for less width")
        detailsContext6=myFont1.render(detailsText6,True,(0,0,200))
        detailsContext7=myFont1.render(detailsText7,True,(0,0,200))
        screen.blit(detailsContext6,(840,130))
        screen.blit(detailsContext7,(840,150))
        detailsText8=("Left click to clear screen")
        detailsText9=str("Undo: Press cntrl+z ")
        detailsContext8=myFont1.render(detailsText8,True,(0,0,200))
        detailsContext9=myFont1.render(detailsText9,True,(0,0,200))
        screen.blit(detailsContext8,(840,170))
        screen.blit(detailsContext9,(840,190))
        detailsText10=("Redo: Press cntrl+y")
        detailsContext10=myFont1.render(detailsText10,True,(0,0,200))
        screen.blit(detailsContext10,(840,210))
################width and mx, my and shape width and sticker width

        detailsWidth=myFont2.render("Width" +'    ' + str(width),True,(0,0,200))
        detailsmxmy=myFont2.render("mouse position" + '  ' + str(mx) +'   '+ str(my),True,(0,0,200))
        detailsShapesWidth=myFont2.render("shapes Width" +'    ' + str(shapesWidth),True,(0,0,200))
        detailsStickerSize=myFont2.render("stickerSize" +'    ' + str(stickerSize),True,(0,0,200))
        detailsColour=myFont2.render('colour'+'   '+str(col),True,(0,0,200))
        screen.blit(detailsWidth,(1000,20))
        screen.blit(detailsmxmy,(1000,40))
        screen.blit(detailsShapesWidth,(1000,60))
        screen.blit(detailsStickerSize,(1000,80))
        screen.blit(detailsColour,(1000,100))








        ####getting mouse position
        omx=mx
        omy=my
        
        ###updating display
        display.flip()
quit() #






