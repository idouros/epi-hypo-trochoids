import cv2
import numpy as np
import math
import time

img_rows = 800
img_cols = 800
img_channels = 3

spire_length = 50000
spire_step = 0.01

r1 = 250
r2 = 48 # >0 for hypotrochoid, >0 for epitrochoid
r3 = 25
color = (255, 0, 0)
thickness = 1
pace = 1

def spire(canvas):
    row_shift = img_rows / 2.0
    col_shift = img_cols / 2.0

    fr1 = float(r1)
    fr2 = float(r2)
    fr3 = float(r3)

    start_point = (0, 0)
    for i in range(spire_length):
        t = i * spire_step
        x = row_shift + (fr1 - fr2) * math.cos(t) + fr3 * math.cos((fr1-fr2)/fr2 * t) #mistake in my initial formulae, work it out
        y = col_shift + (fr1 - fr2) * math.sin(t) - fr3 * math.sin((fr1-fr2)/fr2 * t)
        end_point = (int(y), int(x))
        if(i > 0):
            canvas = cv2.line(canvas, start_point, end_point, (i%255,128,128), thickness)
        start_point = end_point
        cv2.imshow('RGB', canvas)
        cv2.waitKey(pace)

def main():
    canvas = np.full((img_rows, img_cols, img_channels), fill_value = 255, dtype = np.uint8)
    spire(canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()