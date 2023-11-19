import numpy as np
import matplotlib.pyplot as plt
import struct
from PIL import Image,ImageTk
import io
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2

def parse_a2r10g10b10(binary_data, width, height):
    #解析数据
    #一个像素占4个字节
    pixel_format = "i"
    pixel_size = struct.calcsize(pixel_format)
    print(pixel_size, len(binary_data),len(binary_data)//4)
    pixel_count = width * height * 4

    #pixel_count = pixel_count - 1
    #创建空白图像
    image = Image.new("RGBA",(width, height))

    for i in range(pixel_count):
        #从二进制数据中读取一个像素
        if i < 5:
            print(i)
        try:
            pixel_data = struct.unpack_from(pixel_format,binary_data,i * pixel_size)[0]
            #pixel_data = struct.unpack_from(pixel_format * (width * height), binary_data)
        except Exception as e:
            # 弹出提示框，显示错误信息
            #messagebox.showerror("file size error", str(e))
            print(i,pixel_count)
            return None
        #pixel_data = struct.unpack_from(pixel_format,binary_data,i * pixel_size)[0]
       # 解析格式
        # 提取分量
        pixel_data = np.array(pixel_data)
        alpha = ((pixel_data >> 30) & 0b11) * 85
        red = ((pixel_data >> 20) & 0b1111111111) * 4
        green = ((pixel_data >> 10) & 0b1111111111) * 4
        blue = (pixel_data & 0b1111111111) * 4

        # 将分量转换为 8 位整数
        alpha = (alpha * 255) // 1020
        red = (red * 255) // 1020
        green = (green * 255) // 1020
        blue = (blue * 255) // 1020

        # 计算像素在图像中的位置
        x = i % width
        y = i // width

        # 将解析出来的颜色写入图像
       # print(f"Pixel{i} (R:{red} G:{green} B:{blue})")
        #将解析出来的颜色写入图像
        image.putpixel((x, y), (red, green, blue, alpha))
        #photo_image= ImageTk.PhotoImage(image)

    #将PIL图像转换为TK inter PhotoImage
    photo_image = ImageTk.PhotoImage(image)

    #创建canvas用于显示图像
    canvas = tk.Canvas()
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    #更新Canvas 大小
    canvas.config(scrollregion=(0, 0, width, height))
    canvas.config(width=min(width, canvas.winfo_screenwidth() - 100),
                        height=min(height, canvas.winfo_screenheight() - 100))
    
    #在canvas 上显示图片
    canvas.create_image(0, 0, anchor = tk.NW, image=photo_image)
        # 创建图像数组
        #image_data = np.zeros((height, width, 4), dtype=np.uint8)
        #image_data[..., 0] = red.reshape((height, width))
        #image_data[..., 1] = green.reshape((height, width))
        #image_data[..., 2] = blue.reshape((height, width))
        #image_data[..., 3] = alpha.reshape((height, width))

    # 显示图像
    #plt.imshow(image_data)
    #plt.axis('off')
    #plt.show()

    return photo_image

def convert_a2r10g10b10_to_argb8888(binary_data):
    # 解析A2R10G10B10格式的图像数据
    pixel_format = "I"
    pixel_size = struct.calcsize(pixel_format)
    pixel_data = struct.unpack_from(pixel_format * (len(binary_data) // pixel_size), binary_data)

    argb_data = bytearray()

    for pixel in pixel_data:
        # 解析A2R10G10B10格式的像素数据
        alpha = (pixel >> 30) & 0b11
        red = (pixel >> 20) & 0b1111111111
        green = (pixel >> 10) & 0b1111111111
        blue = pixel & 0b1111111111
        '''
        # 将分量转换为8位整数
        alpha = (alpha * 255) // 3
        red = (red * 255) // 1023
        green = (green * 255) // 1023
        blue = (blue * 255) // 1023
        '''
        # 将分量转换为 8 位整数
        alpha = (alpha * 255) // 1020
        red = (red * 255) // 1020
        green = (green * 255) // 1020
        blue = (blue * 255) // 1020
        # 将像素数据转换为ARGB8888格式
        argb_pixel = (alpha << 24) | (red << 16) | (green << 8) | blue

        # 将ARGB8888像素数据打包为二进制数据
        argb_data.extend(struct.pack("I", argb_pixel))

    return bytes(argb_data)


def parse_a2r10g10b10_pitch_linear(imagefile, data, width, height):
    # 计算每个像素的字节数
    bytes_per_pixel = 4
    # 计算每行像素的字节数
    pitch = bytes_per_pixel * width
    '''
    if imagefile is not None:
        data = np.fromfile(imagefile, dtype=np.uint32)

        # 解析ARGB分量
        A = (data >> 30) & 0x03
        R = (data >> 20) & 0x3FF
        G = (data >> 10) & 0x3FF
        B = data & 0x3FF

        # 执行更准确的10-bit到8-bit映射
        R = ((R * 255 + 511) // 1023).astype(np.uint8)
        G = ((G * 255 + 511) // 1023).astype(np.uint8)
        B = ((B * 255 + 511) // 1023).astype(np.uint8)

        # 你可能需要调整 R, G, B 以适配你的数据和需求
        RGB = np.stack([R, G, B], axis=-1)  # 这一行将 R, G, B 通道组合在一个数组中
        RGB = RGB.reshape((1280, 768,3))
        # OpenCV需要BGR格式，所以在显示前需要换位
        BGR = cv2.cvtColor(RGB, cv2.COLOR_RGB2BGR)

# 你可以现在把RGB数据存回一个numpy数组
        RGB = (R << 16) | (G << 8) | B
        # 显示图像
        cv2.imshow('image', BGR)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''
    # 解析像素数据
    pixels = []
    for i in range(height):
        start_index = i * pitch
        end_index = start_index + pitch
        row_data = data[start_index:end_index]
        for j in range(0, len(row_data), bytes_per_pixel):
            pixel_data = row_data[j:j+bytes_per_pixel]
            # 解析32位像素数据（以little-endian格式）
            pixel = struct.unpack("<I", pixel_data)[0]
            # 将像素的每个通道解析为10位无符号整数
            alpha = (pixel >> 30) & 0x03
            red = (pixel >> 20) & 0x3FF
            green = (pixel >> 10) & 0x3FF
            blue = pixel & 0x3FF
            # 将每个通道转换为8位整数
            alpha = (alpha * 255) // 3
            red = (red * 255) // 1023
            green = (green * 255) // 1023
            blue = (blue * 255) // 1023
            # 将解析后的像素添加到像素列表中
            pixels.append((red, green, blue, alpha))

    return pixels

def display_image(pixels, width, height):
    # 创建一个新的图像对象
    image = Image.new("RGBA", (width, height))

    # 在图像上绘制像素数据
    image.putdata(pixels)

    # 显示图像
    image.show()

    

