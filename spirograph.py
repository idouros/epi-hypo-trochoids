import cv2
import numpy as np
import math
import time

img_rows = 800
img_cols = 800
img_channels = 3

spire_length = 5000
spire_step = 0.01

# The next three must be FLOAT
r_fixed = 300.0     # radius of the fixed circle
r_rolling = 25.0   # radius of the rolling circle, >0 for hypotrochoid, >0 for epitrochoid
d = 100.0           # distance of tracing point from the centre of the rolling circle
color = (255, 0, 0)
thickness = 1
pace = 1

def spire(canvas):
    row_shift = img_rows / 2.0
    col_shift = img_cols / 2.0

    d_r = r_fixed - r_rolling
    r_r = r_rolling / r_fixed

    start_point = (0, 0)
    for i in range(spire_length):
        t = i * spire_step
        # Still can't figure out why the denominator in the second terms below is r_rolling
        # and not r_fixed. Doesn't seem to make sense...
        x = row_shift + (d_r) * math.cos(t) + d * math.cos((d_r / r_rolling) * t)
        y = col_shift + (d_r) * math.sin(t) - d * math.sin((d_r / r_rolling) * t)
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