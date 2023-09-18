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
        pos = offscreen_canvas.width
        my_text = self.args.text
        move = -1

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, font.height, textColor, my_text,)
            pos += move
            if ((pos + len + move = offscreen_canvas.width) || (pos + move = 0)){
                move = -move
            }
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
