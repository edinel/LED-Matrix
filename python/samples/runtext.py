#!/usr/bin/env python
# Display a runtext with double-buffering.
import os
from samplebase import SampleBase
from rgbmatrix import graphics
import time

fontdir = "/home/edinel/source/led-matrix/fonts/"
        

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")



    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        #print (self.args.font)
        fontpath = fontdir+self.args.font
        print (fontpath)
        font.LoadFont(fontpath)
        print (font.height)
        textColor = graphics.Color(128, 255, 128)
        x_pos = offscreen_canvas.width
        y_pos = font.height
        my_text = self.args.text
        x_move = -1
        y_move = -1

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, x_pos, y_pos, textColor, my_text,)
            x_pos += x_move
            y_pos +=y_move

            if ((x_pos + len == offscreen_canvas.width) and (x_move>0)):
                print ("right") 
                x_move = -x_move
            elif ((x_pos + x_move == 0) and (x_move < 0)):
                print ("left")
                x_move = -x_move
            if ((y_pos - font.height == offscreen_canvas.height) and (y_move < 0)):
                print ("bottom")
                y_move = -y_move
            elif ((y_pos + y_move == 0) and (y_move > 0)):
                print ("top")
                y_move = -y_move


            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)



# Main function
if __name__ == "__main__":
    path = "Path is"
    path += os.getcwd()
    print (path)
    run_text = RunText()
    if (not run_text.process()):
        print ("WTAF")
        run_text.print_help()
