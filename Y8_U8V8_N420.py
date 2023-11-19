import struct
import numpy as np
from PIL import Image
import cv2
import tkinter as tk
from PIL import Image, ImageTk

'''
Plane0: YYYYYYYY 
Plane1: UUUUUUUUVVVVVVVV
'''
# 图像的宽度和高度
width = 768# 图像的宽度
height = 1280# 图像的高度

bytes_per_pixel = 2

# 存储像素的列表
Y_pixels = []
UV_pixels = []
pixels = []

# 读取 Y 分量数据
with open('OUTPUT_LUMA_00000_0.bin', 'rb') as f:
    Y_data = f.read()
    Y = np.frombuffer(Y_data, dtype=np.uint8)
    Y = Y & 0xFF # 既然Y处于10位数据，我们需要屏蔽掉其他的数据
    #Y = (Y * 255 / 1023).astype(np.uint8) # 缩放到8-bit
    Y = Y.reshape(height, width) # 重塑为图像的形状

# 读取 UV 分量数据
with open('OUTPUT_CHROMA_U_00000_0.bin', 'rb') as f:
    UV_data = f.read()
    UV = np.frombuffer(UV_data, dtype=np.uint16) #读取为32位无符号整数
    U = (UV & 0x0FF) # U在低10位
    V = (UV >> 8) & 0x0FF # V在中间的10位，需要rs向右移16位
    # 缩放到8-bit并重塑形状
    V = V.astype(np.uint8).reshape(height // 2, width // 2)
    U = U.astype(np.uint8).reshape(height // 2, width // 2)

# UV的每个元素对应于Y的四个像素，所以需要将UV的尺寸增大到与Y的尺寸相同
U = np.repeat(np.repeat(U, 2, axis=0), 2, axis=1)
V = np.repeat(np.repeat(V, 2, axis=0), 2, axis=1)

# 转换 YUV 到 RGB
yuv_image = cv2.merge([Y, U, V])
rgb_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

image = Image.fromarray(rgb_image) # 使用PIL来将numpy array转化为图像

# 在Tkinter窗口中显示图片
window = tk.Tk()
canvas = tk.Canvas(window, width=image.width, height=image.height)
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor='nw', image=image_tk)

window.mainloop()