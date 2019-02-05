# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: David Fricke
# NUMBER OF HOURS TO COMPLETE:  5 hours
# YOUR COLLABORATION STATEMENT(s): I worked with 
# microbit SOP - Flash, REPL, Reset (button near jack on the mircobit.
# Remember to be in microbit mode

import math
import microbit
from microbit import *

while True:
    microbit.sleep(150)
    y = microbit.accelerometer.get_y()
    x = microbit.accelerometer.get_x()
    z = microbit.accelerometer.get_z()
    ytilt = ((math.atan2(y, z))/(math.pi))*180
    xtilt = ((math.atan2(x, z))/(math.pi))*180
    print(xtilt , ytilt) #print degreed
    if abs(xtilt + ytilt) > 351: # tests show that this is true
        display.show(Image("00000:00900:09990:00900:00000"))
    elif (xtilt < -177 or xtilt > 177) and ytilt < 0: #strange condition, but true north is between -177 x degrees and 177 x degrees and +y
        display.show(Image.ARROW_N)
    elif (xtilt > 177 or xtilt < -177) and ytilt > 0: # true south is between -177 x degree and 177 degrees and -y
        display.show(Image.ARROW_S)
    elif xtilt < -100:       #left
        if abs(ytilt) > 174: #true left
            display.show(Image.ARROW_W)
        elif ytilt < 0:      #
            display.show(Image.ARROW_NW)
        elif ytilt > 0:      #
            display.show(Image.ARROW_SW)
    elif xtilt > 100:        #right
        if abs(ytilt) > 174: #true right
            display.show(Image.ARROW_E)
        elif ytilt < 0:      #
            display.show(Image.ARROW_NE)
        elif ytilt > 0:      #
            display.show(Image.ARROW_SE)




    #This works well. LOTS of experimental data!
