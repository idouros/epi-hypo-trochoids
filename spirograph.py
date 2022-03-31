import cv2
import numpy as np
import math
import time

img_rows = 800
img_cols = 800
img_channels = 3

spire_length = 500000
spire_step = 0.01

# The next three must be FLOAT
r_fixed = 390.0     # radius of the fixed circle
r_rolling = 310.0   # radius of the rolling circle, >0 for hypotrochoid, >0 for epitrochoid
d = 170.0           # distance of tracing point from the centre of the rolling circle
color = (0, 255, 0)
circle_color_fixed = (0, 0, 255)
circle_color_rolling = (255, 0, 0)
thickness = 2
pace = 0            # Zero does not animate.

def spire(canvas):
    row_shift = img_rows / 2.0
    col_shift = img_cols / 2.0

    d_r = r_fixed - r_rolling
    r_r = r_rolling / r_fixed

    start_point = (0, 0)
    for i in range(spire_length):
        t = i * spire_step
        # https://en.wikipedia.org/wiki/Spirograph#Mathematical_basis
        x = row_shift + (d_r) * math.cos(t) + d * math.cos((d_r / r_rolling) * t)
        y = col_shift + (d_r) * math.sin(t) - d * math.sin((d_r / r_rolling) * t)
        end_point = (int(y), int(x))
        if(i > 0):
            canvas = cv2.line(canvas, start_point, end_point, color, thickness, cv2.LINE_AA)
        start_point = end_point
        if pace > 0:
            cv2.imshow('RGB', canvas)
            cv2.waitKey(pace)

def show_circles(canvas):
    centre_circle_fixed = (int(img_cols/2), int(img_rows/2))
    centre_circle_rolling = (int(img_cols/2 - r_fixed + r_rolling), int(img_rows/2))
    tracing_point = (int(img_cols/2 - r_fixed + r_rolling - d), int(img_rows/2))
    # Fixed circle
    canvas = cv2.circle(canvas, centre_circle_fixed, 2, circle_color_fixed,2)
    canvas = cv2.circle(canvas, centre_circle_fixed, int(r_fixed), circle_color_fixed)
    # Rolling circle
    canvas = cv2.circle(canvas, centre_circle_rolling, 2, circle_color_rolling, 2)
    canvas = cv2.circle(canvas, centre_circle_rolling, int(r_rolling), circle_color_rolling)
    # Tracing point
    canvas = cv2.circle(canvas, tracing_point, 2, circle_color_rolling, 2)
    canvas = cv2.line(canvas, tracing_point, centre_circle_rolling, circle_color_rolling)
    cv2.imshow('RGB', canvas)        

def main():
    canvas = np.full((img_rows, img_cols, img_channels), fill_value = 255, dtype = np.uint8)
    spire(canvas)
    if pace == 0:
        cv2.imshow('RGB', canvas)
    cv2.waitKey(0)
    show_circles(canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()