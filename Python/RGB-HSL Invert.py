print("RGB/HSL Colour Inverter");
print("V1.1\n");
from colorsys import hls_to_rgb, rgb_to_hls
from math import fabs

#Functions that make life easier
def hsl_to_rgb(h:float,s:float,l:float) -> list[float]:
    return hls_to_rgb(h,l,s)

def abs(x:float) -> float:
    return fabs(x)

#Main
def invert(r:int,g:int,b:int) -> str:
    if r > 255 or r < 0:
        r = abs(r) % 255

    if g > 255 or g < 0:
        g = abs(g) % 255

    if b > 255 or b < 0:
        b = abs(b) % 255

    return f"rgb({255-r},{255-g},{255-b})"

counter = 0
while True:
    counter += 1
    if counter == 1:
        col = input("What is your colour? ")
    else:
        col = input("\nWhat is your colour? ")

    if col[0] == "r":
        col = col.replace("rgb(","")
        col = col.replace(")","")
        col = col.split(",")
        print(invert(eval(col[0]),eval(col[1]),eval(col[2])))
    
    elif col[0] == "h":
        col = col.replace("%","")
        col = col.replace("hsl(","")
        col = col.replace(")","")
        col = col.split(",")

        h, s, l = eval(col[0])/360, eval(col[1])/100, eval(col[2])/100
        col = hsl_to_rgb(h,s,l)
        col = invert(int(col[0]*255), int(col[1]*255), int(col[2]*255))

        col = col.replace("rgb(","")
        col = col.replace(")","")
        col = col.split(",")

        r, g, b = eval(col[0])/255, eval(col[1])/255, eval(col[2])/255
        col = rgb_to_hls(r,g,b)
        h, l, s = col[0]*360, col[1]*100, col[2]*100

        print(f"hsl({h:.1f},{s:.1f}%,{l:.1f}%)")


