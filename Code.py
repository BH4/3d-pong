import PIL.ImageGrab as ImageGrab
import os
import time
#import win32api#to fix this one uninstall all python and install 64 bit
import pyautogui
#import win32con
import numpy as np
from random import randrange



#to kill pyautogui move mouse to top left corner of screen.















#need to take picture of side to determine how far the ball is, then
#only move the mouse right before the ball hits my side

#http://www.freegames.ws/games/free_online_games/pong_game/3d_game.htm

tmax=10*60

xpad=325
ypad=162
xmax=1258
ymax=782
xlen=xmax-xpad
ylen=ymax-ypad


linexmin=0
linexmax=350
line1y=257
line2y=376

def screenGrab():
    box = ()
    im = ImageGrab.grab((xpad,ypad,xlen+xpad,ylen+ypad))
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def screenGrabSave():
    box = ()
    im = ImageGrab.grab((xpad,ypad,xlen+xpad,ylen+ypad))
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def partScreenGrabSave(xmin,ymin,xmax,ymax):
    box = ()
    im = ImageGrab.grab((xpad+xmin,ypad+ymin,xpad+xmax,ypad+ymax))
    im.save(os.getcwd() + '\\part_snap__' + str(int(time.time())) + '.png', 'PNG')


"""
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'
"""
def leftClick():
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(.1)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    pyautogui.click()
    print "Click."


def mousePos(cord):
    #win32api.SetCursorPos((xpad + cord[0], ypad + cord[1]))
    pyautogui.moveTo(xpad + cord[0], ypad + cord[1])

def get_cords():
    #x,y = win32api.GetCursorPos()
    x,y = pyautogui.size()
    x = x - xpad
    y = y - ypad
    print x,y

def firstHit():
    x=randrange(0,xlen)
    y=randrange(0,ylen)
    mousePos((x,y))
    time.sleep(.1)
    mousePos((464,309))
    time.sleep(.05)
    leftClick()

def findBall(im):
    
    c=[255,255,255]
    nim=np.array(im)
    
    indices = np.where(nim[:,:,0] == 255)#just check to first correct spot instead?
    cords = zip(indices[1], indices[0])
    num=len(cords)
    
    done=False
    i=num-1
    ball=None
    #print cords
    #done=True
    while not done and i>=0:
        check=cords[i]
        if nim[check[1],check[0],2]==255:
            done=True
            ball=check
        i-=1
        
    return ball,num

def test():
    leftClick()
    time.sleep(.1)
    
    
    im=screenGrab()
    tt=time.time()
    findBall(im)


    print time.time()-tt

def startgame():
    #click start button
    mousePos((464,280))
    leftClick()
    time.sleep(3)

    #click ball
    firstHit()
    '''
    mousePos((464,309))
    leftClick()
    time.sleep(.1)
    '''
    main()
    
def main():
    t=time.time()
    ballCords=(0,0)
    repeatNum=0

    posList=[]
    currentLevel=0
    while time.time()-t<tmax:
        mult=1+.02*currentLevel
        
        im=screenGrab()

        prevBall=ballCords
        ballCords,num=findBall(im)

        if not(ballCords==None) and num<1000 and num>1:
            posList.append(ballCords)
            predict=ballCords
            if len(posList)>=2:
                moveLenX=posList[-1][0]-posList[-2][0]
                moveLenY=posList[-1][1]-posList[-2][1]
                move=(moveLenX*mult,moveLenY*mult)
                predict=(int(ballCords[0]+move[0]),int(ballCords[1]+move[1]))

            mousePos(predict)

            
        #check for new round
        if prevBall==ballCords:
            
            repeatNum+=1
            if repeatNum==10:
                firstHit()
                repeatNum=0
                if flag:
                    currentLevel+=1
                    print currentLevel
                    flag=False
                
        else:
            flag=True
            repeatNum=0
        


