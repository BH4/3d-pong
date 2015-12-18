import PIL.ImageGrab as ImageGrab
import os
import time
 
xpad=66
ypad=221
xmax=715
ymax=692
xlen=xmax-xpad
ylen=ymax-ypad

def screenGrab():
    box = ()
    im = ImageGrab.grab((xpad,ypad,xlen+xpad,ylen+ypad))
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
