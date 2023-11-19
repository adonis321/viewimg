import struct
import numpy as np
from PIL import Image
import cv2
import tkinter as tk
from PIL import Image, ImageTk
'''
从左往右 高位->低位
Plane0: YYYYYYYYYY000000 
Plane1: UUUUUUUUUU000000VVVVVVVVVV000000
'''
# 图像的宽度和高度
width = 768# 图像的宽度
height = 1280# 图像的高度

bytes_per_pixel = 2

# 存储像素的列表
Y_pixels = []
UV_pixels = []

def open_Y(filename,Y_pixels):
    # 读取 Y 分量数据
    with open(filename, 'rb') as f:
        Y_data = f.read()
        #print(len(Y_data))
        for i in range(0, len(Y_data), bytes_per_pixel):
            pixel_data = Y_data[i:i+bytes_per_pixel]
            pixel = struct.unpack("<H", pixel_data)[0] # 解析16位像素数据（以little-endian格式）
            Y = (pixel >> 6) & 0x03FF # 将像素的Y分量解析为10位无符号整数
            Y = (Y * 255) // 1023 # 将Y转换为8位整数
            Y_pixels.append(Y)

def open_UV(filename,UV_pixels):
    # 读取 VU 分量数据
    with open(filename, 'rb') as f:
        UV_data = f.read()
        print(len(UV_data))
        for i in range(0, len(UV_data), bytes_per_pixel * 2): # 注意每个像素由2个bytes组成，所以步长是2
            pixel_data = UV_data[i:i+bytes_per_pixel * 2]
            pixel = struct.unpack("<I", pixel_data)[0] # 解析32位像素数据
            #if i < 5:
                #print(f'{pixel:b}\n')
            V = (pixel >> 22) & 0x03FF # 将像素的V分量解析为10位无符号整数
            U = (pixel >> 6) & 0x03FF  # 将像素的U分量解析为10位无符号整数
            # 将U和V转换为8位整数
            V = (V * 255) // 1023
            U = (U * 255) // 1023
            UV_pixels.append((U, V))
'''
# 将Y、UV列表装换为图片的形状
Y_pixels = np.array(Y_pixels).reshape(height, width)
UV_pixels = np.array(UV_pixels).reshape(height // 2, width // 2, 2)

# 将UV扩大到和Y的形状一样
V = np.repeat(np.repeat(UV_pixels[...,1], 2, axis=0), 2, axis=1)
U = np.repeat(np.repeat(UV_pixels[...,0], 2, axis=0), 2, axis=1)

# 装换YUV到RGB
yuv_image = np.dstack((Y_pixels, U, V)).astype(np.uint8)
rgb_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

image = Image.fromarray(rgb_image) # 使用PIL来将numpy array转化为图像

# 在Tkinter窗口中显示图片
window = tk.Tk()
canvas = tk.Canvas(window, width=image.width, height=image.height)
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor='nw', image=image_tk)

window.mainloop()
'''

# 显示RGB图像
#cv2.imshow('image', rgb_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()