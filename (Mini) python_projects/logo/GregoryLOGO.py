import png
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "LOGO.png"
abs_file_path = os.path.join(script_dir, rel_path)


new_png = []
for y in range(16):
    row = ()
    for x in range(16):
        if (x==0 or x==1) and (y==y):
            row += (0+x*16, 0+y*16, 255-x*16)
        elif (x==14 or x==15) and (y==y):
            row += (0+x*16, 0+y*16, 255-x*16)
        elif (x>=2 and x<=13) and (y<=1 or y>=14):
            row += (0+x*16, 0+y*16, 255-x*16)
            """ Inside \|/ """
        elif (x>=5 and x<=7) and y==5:
            row += (0+y*16, 0+x*16, 255-x*16)
        elif (x>=5 and x<=7) and y==6:
            row += (0+y*16, 0+x*16, 255-x*16)
        elif (x == 6) and (y==7 or y==8):
            row += (0+y*16, 0+x*16, 255-x*16)
        elif (x == 9) and (y==7 or y==8):
            row += (0+y*16, 0+x*16, 255-x*16)
        elif (x == 7 or x == 8) and (y == 9):
            row += (0+y*16, 0+x*16, 255-x*16)
        else:
            row += (0,0,0)
    new_png.append(row)

with open(abs_file_path, 'wb') as file:
    w = png.Writer(16, 16, greyscale=False)
    w.write(file, new_png)