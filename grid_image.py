import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

I=cv.imread('lena.png',0)

def image_to_grid(image,grid_size_h,grid_size_w,plot=False):
    """
    A function that split an image to a NXM (grid_size_h x grid_size_w) grid
    """
    h, w = np.shape(image)
    grid_h = np.append(np.arange(0, int(h + h / grid_size_h), int(h / grid_size_h)), 0)
    grid_w = np.append(np.arange(0, int(w + w / grid_size_w), int(w / grid_size_w)), 0)
    count = 0
    grid_sub=[]
    for i in range(0, len(grid_h) - 2):
        for j in range(0, len(grid_w) - 2):
            count += 1
            sub_I = I[grid_h[i]:grid_h[i + 1] - 1, grid_w[j]:grid_w[j + 1] - 1]
            grid_sub.append(sub_I)
            if plot == True:
                plt.subplot(len(grid_h) - 2, len(grid_w) - 2, count)
                plt.axis('off')
                plt.imshow(sub_I, cmap='gray')

            else:
                pass
    plt.show()
    return grid_sub
grid= image_to_grid(I,16,16,True)
