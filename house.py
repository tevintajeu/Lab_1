import math

import cairo

Images = "Image/"

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,1000,1000)
ctx = cairo.Context(surface)

ctx.set_source_rgb(255,255,255)
ctx.paint()

#House Outline
ctx.set_source_rgb(0,0,1)
ctx.set_line_width(1)
ctx.move_to(250,650)
ctx.line_to(710,650)
ctx.stroke()

ctx.move_to(250,650)
ctx.line_to(250,400)
ctx.stroke()

ctx.move_to(710,650)
ctx.line_to(710,400)
ctx.stroke()

ctx.move_to(250,400)
ctx.line_to(200,400)
ctx.stroke()

ctx.move_to(710,400)
ctx.line_to(760,400)
ctx.stroke()

ctx.move_to(200,400)
ctx.line_to(200,300)
ctx.stroke()

ctx.move_to(760,400)
ctx.line_to(760,300)
ctx.stroke()

ctx.move_to(200,300)
ctx.line_to(760,300)
ctx.stroke()

#Windows
#Left
ctx.set_line_width(3)
ctx.set_source_rgb(0,1,0)
ctx.rectangle(280,450,100,100)
ctx.stroke()

#Right
ctx.set_source_rgb(0,1,0)
ctx.rectangle(580,450,100,100)
ctx.stroke()

#WindowLines
#Left
ctx.set_source_rgb(0,0,1)
ctx.set_line_width(1)
ctx.move_to(330,450)
ctx.line_to(330,550)
ctx.stroke()

ctx.move_to(280,500)
ctx.line_to(380,500)
ctx.stroke()

#Right
ctx.move_to(630,450)
ctx.line_to(630,550)
ctx.stroke()

ctx.move_to(580,500)
ctx.line_to(680,500)
ctx.stroke()

#Door
ctx.set_line_width(3)
ctx.set_source_rgb(0,1,0)
ctx.rectangle(430,450,100,200)
ctx.stroke()

#Roof
ctx.set_line_width(1)
ctx.set_source_rgb(0,0,1)
ctx.arc_negative(480,300,150,0, 1*22/7)
ctx.stroke()

#DoorKnob
ctx.set_line_width(5)
ctx.arc(514,550,8,0,2*math.pi)
ctx.fill()
ctx.stroke()

#Moon
ctx.arc(850, 100, 50, 0, 2 * 3.141592)
ctx.set_source_rgb(0, 1, 0)  # White color for the full moon
ctx.fill()

    # Draw the overlapping circle to create the crescent effect
ctx.arc(890, 70, 50, 0, 2 * 3.141592)
ctx.set_source_rgb(1, 1, 1)  # Black color for the overlapping part
ctx.fill()

surface.write_to_png(f"{Images}2DHouse.png")
