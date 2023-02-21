# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from PIL import Image
from numpy import asarray

imin = Image.open("test.jpg")
imar = asarray(imin)
i = 0
j = 0
x = imin.size[0]
y = imin.size[1]
while i < y:
    while j < x:
        brightness = (imar[i, j, 0] + imar[i, j, 1] + imar[i, j, 2])*-1+254
        str = "ÆOyxÎ%¤×}*•¬|³º²–‹›;ˆ¸…·¨´`"
        asciimap = np.array(list(str))
        print(asciimap[int(brightness / 255 * asciimap.size)]*3, end="")
        j += 1
    j = 0
    print(" ")
    i += 1
teststst = input("press enter to exit")
