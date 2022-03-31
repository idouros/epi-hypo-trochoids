import cv2
import numpy as np
import math
import time

img_rows = 850
img_cols = 850
img_channels = 3

spire_length = 10000
spire_step = 0.01

# The next three must be FLOAT
r_fixed = 300.0     # radius of the fixed circle
r_rolling = -52.0   # radius of the rolling circle, >0 for hypotrochoid, <0 for epitrochoid
d = 50.0           # distance of tracing point from the centre of the rolling circle
spire_color = (0, 0, 0)
circle_color_fixed = (0, 0, 255)
circle_color_rolling = (255, 0, 0)
thickness = 2
pace = 2            # Zero does not animate.
show_circles = True

def spire():
    spire_canvas = np.full((img_rows, img_cols, img_channels), fill_value = 255, dtype = np.uint8)
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
            spire_canvas = cv2.line(spire_canvas, start_point, end_point, spire_color, thickness, cv2.LINE_AA)
        start_point = end_point
        disp_canvas = spire_canvas.copy()
        if pace > 0:
            if show_circles:
                centre_circle_fixed = (int(col_shift), int(row_shift))
                centre_circle_rolling = (int(col_shift + (d_r) * math.sin(t)), int(row_shift + (d_r) * math.cos(t)))
                tracing_point = end_point
                # Fixed circle
                disp_canvas = cv2.circle(disp_canvas, centre_circle_fixed, thickness*2, circle_color_fixed, thickness)
                disp_canvas = cv2.circle(disp_canvas, centre_circle_fixed, int(r_fixed), circle_color_fixed, thickness)
                # Rolling circle
                disp_canvas = cv2.circle(disp_canvas, centre_circle_rolling, thickness*2, circle_color_rolling, thickness)
                disp_canvas = cv2.circle(disp_canvas, centre_circle_rolling, int(abs(r_rolling)), circle_color_rolling, thickness)
                disp_canvas = cv2.line(disp_canvas, centre_circle_fixed, centre_circle_rolling, circle_color_fixed, thickness)
                # Tracing point
                disp_canvas = cv2.circle(disp_canvas, tracing_point, thickness*2, circle_color_rolling, thickness)
                disp_canvas = cv2.line(disp_canvas, tracing_point, centre_circle_rolling, circle_color_rolling, thickness)                
            cv2.imshow('RGB', disp_canvas)
            cv2.waitKey(pace)
    cv2.waitKey(0)
    cv2.imshow('RGB', spire_canvas)
    cv2.waitKey(0)
    

def main():
    spire()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()