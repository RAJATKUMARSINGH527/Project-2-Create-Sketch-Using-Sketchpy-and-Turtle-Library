#Drawing Canvas
from sketchpy import canvas
myObject = canvas.sketch_from_image("E:\CAP BATCH 2 2023\Projects-1,2,3\ICCT20s World Cup 2007 Winning Moment.jpg")
# myObject.draw()
myObject.draw(threshold=95)