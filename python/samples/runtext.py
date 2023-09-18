#!/usr/bin/env python
# Display a runtext with double-buffering.
import os
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import random

fontdir = "/home/edinel/source/led-matrix/fonts/"
        

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")



    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        red_val = 128
        green_val = 128
        blue_val = 128 
        textColor = graphics.Color(red_val, green_val, blue_val)

        fontpath = fontdir+self.args.font
        print (fontpath)
        font.LoadFont(fontpath)
        print (font.height)
        x_pos = offscreen_canvas.width
        y_pos = font.height
        my_text = self.args.text
        x_move = -1
        y_move = -1
        height_correction = 3
    
        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, x_pos, y_pos, textColor, my_text,)
            x_pos += x_move
            y_pos +=y_move
            
            if ((x_pos + len >= offscreen_canvas.width) and (x_move>0)):
                print ("right") 
                x_move = -x_move
                textColor = reset_color(self)   
            elif ((x_pos + x_move <= 0) and (x_move < 0)):
                print ("left")
                x_move = -x_move
                textColor = reset_color(self)                   
            if ((y_pos - font.height + height_correction <= 0) and (y_move < 0)):
                print ("top")
                y_move = -y_move
                textColor = reset_color(self)   

            elif ((y_pos + y_move >= offscreen_canvas.height) and (y_move > 0)):
                print ("bottom")
                y_move = -y_move
                textColor = reset_color(self)
            textColor = graphics.Color(red_val, green_val, blue_val)
            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)



def reset_color(self):
    random.seed ()
    new_red_val = random.randrange(0,255,1)
    new_green_val = random.randrange(0,255,1)
    new_blue_val = random.randrange(0,255,1)
    l_textColor = graphics.Color(new_red_val, new_green_val, new_blue_val)
    return l_textColor


# Main function
if __name__ == "__main__":
    path = "Path is"
    path += os.getcwd()
    print (path)
    run_text = RunText()
    if (not run_text.process()):
        print ("WTAF")
        run_text.print_help()
