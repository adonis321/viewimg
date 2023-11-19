import os
import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import A2R10G10B10 as a2r10g10b10
import A2B10G10R10 as a2b10g10r10
import Y10_U10V10_N420 as Y10_U10V10_N420
import open_file_paths as fp
#import imageio

img = None
frames = []
current_frame = 0
gif_play = False
global running
running = False
global canvas
global scrollbar
global filename
global ax_x
global ax_y
ax_x = 360 #画布坐标
ax_y = 10
# 创建全局字典来存储文件路径
file_paths = {}
num_planes = 3  # 最大的plane数目
global photo
global bytes_per_pixel#default 2 bytes
global save_img
# 存储像素的列表 for YUV format
Y_pixels = []
UV_pixels = []

file_entries = []
open_buttons = []
# 创建 Canvas 对象
#canvas = tk.Canvas(root, width=500, height=400)
#canvas.place(x=100, y=200)

#open CIF 图像
def play_gif():
    global current_frame
    global gif_timer
    global canvas
    if frames:
        #canvas = tk.Canvas(root, width=750, height=750,scrollregion=(0,0,2920,2080))
        canvas = tk.Canvas(root, width=750, height=750)
        canvas.place(x=ax_x, y=ax_y)
        #scrollbar = tk.Scrollbar(root, command=canvas.yview)
        #canvas.config(yscrollcommand=scrollbar.set)
        #scrollbar.pack(side="right", fill="y")
        frame = frames[current_frame]
        canvas.create_image(0, 0, image=frame, anchor='nw')
        current_frame = (current_frame + 1) % len(frames)
    running = True
    gif_timer = root.after(100, play_gif)

def stop_gif():
    global gif_timer
    global canvas
    if gif_timer is not None:
        # 使用 root.after_cancel 方法来取消定时器
        root.after_cancel(gif_timer)
        gif_timer = None
    canvas.destroy()
    running = False
    #root.destroy()

def on_close():
    root.destroy()

def read_image(imagefile, format=None, width=None, height=None, pitch=None):
    global img, frames, current_frame, bytes_per_pixel
    Y_pixels = []
    UV_pixels = []
    global canvas, photo

    if format is None:
        # 打开图像
        img = Image.open(imagefile)

        # 将图像转换为 numpy 数组
        data = np.array(img)
        img_resized = img.resize((canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img_resized)
        image_id = canvas.create_image(0, 0, image=photo, anchor='nw')
        canvas.image = photo
        #canvas.tag_bind(image_id, "<Button-1>", show_real_size)
        #canvas.bind("<Button-1>", show_real_size)
    elif format == 'A2R10G10B10_1P':
        # 从 bin 文件中读取数据
        with open(imagefile, 'rb') as f:
        #data = np.fromfile(f, dtype=np.uint8 if format == 'RGB888' else np.uint32)
            pixel_data = f.read()
            print(width, height)
            #img = a2r10g10b10.parse_a2r10g10b10(pixel_data,width, height)
            argb8888_data = a2r10g10b10.convert_a2r10g10b10_to_argb8888(pixel_data)
            pixel = a2r10g10b10.parse_a2r10g10b10_pitch_linear(imagefile, pixel_data,
                                                       width,
                                                       height)
            #a2r10g10b10.display_image(pixel, width,height)
            # 将图像转换为 numpy 数组
            # 打开图像
            #data = np.fromfile(f, dtype= np.uint32)
            # 将数据重塑为原始的图像形状
            '''
            argb888 = 'argb8888.bin'
                    # 从 bin 文件中读取数据
            with open(argb888, 'wb') as f:
                f.write(argb8888_data)

            with open(argb888, 'rb') as f:
                data = np.fromfile(f, dtype=np.uint8 if format == 'RGB888' else np.uint32)
                data = data.reshape((height, width))
            '''
            #data = np.fromfile(f, dtype=np.uint32)
            data = np.array(pixel)
            # 用PIL Image创建图像
            image_save_data = Image.fromarray(data)

            #img_resized = image_data.resize((canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS)
            #img_resized = image_data.resize((width, height), Image.LANCZOS)
            #image_data.save('test.bmp')
            photo = ImageTk.PhotoImage(image_save_data)
            image_id = canvas.create_image(0, 0, image=photo, anchor='nw')
            canvas.image = photo

            img = photo
            #img_resized = img.resize((canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS)
            #photo = ImageTk.PhotoImage(img_resized)
            #image_id = canvas.create_image(0, 0, image=img, anchor='nw')
            #canvas.image = img
            #canvas.tag_bind(image_id, "<Button-1>", show_real_size)
            #canvas.bind("<Button-1>", show_real_size)
            data = data.reshape((height, width, 4))
    elif format == 'A2B10G10R10_1P':
        # 从 bin 文件中读取数据
        with open(imagefile, 'rb') as f:
            pixel_data = f.read()
            print(width, height)
            #argb8888_data = a2b10g10r10.convert_a2r10g10b10_to_argb8888(pixel_data)
            pixel = a2b10g10r10.parse_a2b10g10r10_pitch_linear(imagefile, pixel_data,
                                                       width,
                                                       height)

            data = np.array(pixel)
            # 用PIL Image创建图像
            image_save_data = Image.fromarray(data)
            photo = ImageTk.PhotoImage(image_save_data)
            image_id = canvas.create_image(0, 0, image=photo, anchor='nw')
            canvas.image = photo

            img = photo

           # canvas.bind("<Button-1>", show_real_size)
            data = data.reshape((height, width, 4))
    elif format == 'T_Y10___U10V10_N420_2P':
        bytes_per_pixel = 2
        file_paths = get_file_paths()
        # 从 bin 文件中读取数据
        Y_pixels = []
        UV_pixels = []
        Y10_U10V10_N420.open_Y(file_paths[0], Y_pixels)
        Y10_U10V10_N420.open_UV(file_paths[1], UV_pixels)
        # 将Y、UV列表装换为图片的形状
        Y_pixels = np.array(Y_pixels).reshape(height, width)
        UV_pixels = np.array(UV_pixels).reshape(height // 2, width // 2, 2)

        # 将UV扩大到和Y的形状一样
        V = np.repeat(np.repeat(UV_pixels[...,1], 2, axis=0), 2, axis=1)
        U = np.repeat(np.repeat(UV_pixels[...,0], 2, axis=0), 2, axis=1)
        # 装换YUV到RGB
        yuv_image = np.dstack((Y_pixels, U, V)).astype(np.uint8)
        rgb_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

        image_save_data = Image.fromarray(rgb_image) # 使用PIL来将numpy array转化为图像
        #image.save('test_Y10U10V10.bmp')
        # 用PIL Image创建图像
        #photo = ImageTk.PhotoImage(image)
        #image_id = canvas.create_image(0, 0, image=photo, anchor='nw')
        #canvas.image = photo

        #img = photo

        #canvas.bind("<Button-1>", show_real_size)
        data = rgb_image.reshape((height, width, 3))
    else:
        # 从 bin 文件中读取数据
        with open(imagefile, 'rb') as f:
            data = np.fromfile(f, dtype=np.uint8 if format == 'RGB888' else np.uint32)
        try:
            # 将数据重塑为原始的图像形状
            data = data.reshape((height, width))
        except Exception as e:
            # 弹出提示框，显示错误信息
            messagebox.showerror("file size error", str(e))

    return data,image_save_data

#
# 放大缩小
# #

def zoom_fun(event):
    # 获得当前的坐标范围
    xdata, ydata = plt.gca().get_xlim(), plt.gca().get_ylim()
    # 根据事件的滚轮方向进行放大、缩小
    if event.button == 'up':
        scale_factor = 1/1.1
    elif event.button == 'down':
        scale_factor = 1.1
    else:
        return
    # 更新坐标轴范围
    plt.gca().set_xlim([xdata[0]*scale_factor, xdata[1]*scale_factor])
    plt.gca().set_ylim([ydata[0]*scale_factor, ydata[1]*scale_factor])
    canvas_t.draw()  # 重新绘制来更新图像

def display_image(data,image_save_data=None):
    global canvas_t
    # 创建 Figure 对象
    fig = Figure(figsize=(5, 4), dpi=100)

    # 在 Figure 对象中创建一个子图
    ax = fig.add_subplot(121)

    # 在子图中显示图像
    ax.imshow(data, cmap='gray')
    ax.set_axis_off() # 隐藏x轴和y轴
    # 创建 FigureCanvasTkAgg 对象
    canvas_t = FigureCanvasTkAgg(fig, master=root)

    # 显示图像
    canvas_t.draw()
    canvas_t.get_tk_widget().place(x=ax_x, y=ax_y)
    #canvas_t.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # 将 matplotlib 导航工具栏添加到 tkinter 窗口
    #toolbar = NavigationToolbar2Tk(canvas_t, root)
    #toolbar.update()
    # 绑定 button_press_event 事件到 FigureCanvasTkAgg
    #canvas_t.mpl_connect("button_press_event", show_real_size)
    #canvas_t.mpl_connect('scroll_event', zoom_fun)
    return image_save_data

def save_img_file(img):
      # Ask for save file path
        ftypes = [('BMP files', '*.bmp'),('JPG files', '*.jpg'),('JPEG files', '*.jpeg'),('PNG files', '*.png'), ('All files', '*')]
        dlg = filedialog.asksaveasfile(defaultextension=".bmp", filetypes=ftypes)
        if dlg is None:  # User cancelled save dialog
            return
        try:
            img.save(dlg.name, 'BMP')
            messagebox.showinfo("Saved", "Image saved successfully")
        except Exception as e:
            messagebox.showerror("Error", "Failed to save image:\n" + str(e))

def open_image_file():
    global filename
    filename = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp'),  ('All files', '*.*')])
    open_bin_file()

def open_bin_file():
    global img, frames, current_frame, gif_play, canvas,filename,save_img
    # 打开文件对话框

    #print(running)
    #print(frames, len(frames))

    if len(frames) != 0:
        stop_gif()

    # 获取文件的扩展名
    ext = os.path.splitext(filename)[1].lower()
    #img = img.resize((600, 600), Image.LANCZOS)  # Resize the image
    #PLAY GIF
    # If it's a GIF, we read all frames
    gif_play = (ext == '.gif')
    if gif_play:
        img = Image.open(filename)
        try:
            frames = []
            while True:
                frames.append(ImageTk.PhotoImage(img))
                img.seek(len(frames))
        except EOFError:
            pass
        current_frame = 0
        # 开始播放新的GIF动画
        play_gif()
    else:
        print('222\n')
        #canvas = tk.Canvas(root, width=750, height=750,scrollregion=(0,0,2920,2080)) #创建画布
        canvas = tk.Canvas(root, width=750, height=750) #创建画布
        canvas.place(x=ax_x, y=ax_y)
        #scrollbar = tk.Scrollbar(root, command=canvas.yview)
       # canvas.config(yscrollcommand=scrollbar.set)
        #scrollbar.pack(side="right", fill="y")
        #img_resized = img.resize((canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS)
        #photo = ImageTk.PhotoImage(img_resized)
        #image_id = canvas.create_image(0, 0, image=photo, anchor='nw')
        #canvas.image = photo
        #canvas.tag_bind(image_id, "<Button-1>", show_real_size)


    # 根据文件的扩展名来读取文件
    if ext in ['.jpg', '.jpeg', '.png', '.bmp']:
        data,image_save_data = read_image(filename)
        save_img = display_image(data,image_save_data)
    elif ext == '.bin':
        # 获取用户的输入
        width = int(width_entry.get())
        height = int(height_entry.get())
        pitch = int(pitch_entry.get())
        # 获取选中的格式
        format = format_var.get()
        print(format)
        # 读取并显示图像
        data,image_save_data = read_image(filename, format, width, height,pitch)
        save_img = display_image(data,image_save_data)
    return save_img

def show_help():
    messagebox.showinfo("Help", "This is a help message.")

def zoom_in():
    global img
    width, height = img.size
    img = img.resize((width*2, height*2), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=photo, anchor='w')
    canvas.image = photo

def zoom_out():
    global img
    width, height = img.size
    img = img.resize((width//2, height//2), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=photo, anchor='w')
    canvas.image = photo

def del_img(photo):
    del photo

def show_real_size(event=None):
    print("click click")
    #if img is not None:
    #创建新窗口
    new_window = tk.Toplevel(root)
    ## 创建新的 PhotoImage 对象
    photo = ImageTk.PhotoImage(canvas.img)
    # 在新窗口中创建 Label 并显示图像
    label = tk.Label(new_window, image=photo)
    label.image = photo  # 保持对图像的引用
    label.pack()
    #new_window.bind("<Destroy>", del_img(new_window))
    #new_window.protocol("WM_DELETE_WINDOW", del_img(photo))

def update_frame():
    global current_frame
    if frames:  # Check if frames is not empty
        current_frame = (current_frame + 1) % len(frames)
        canvas.itemconfig(canvas.image, image=frames[current_frame])
        #root.after(100, update_frame)
'''
# 创建全局字典来存储文件路径
file_paths = {}

def get_file_paths():
    print(len(file_paths), file_paths[0])
    return file_paths

# 函数，用于选择文件并更新条目的内容
# 使用方法：
# 当你调用 `open_file` 函数并传入一个 Entry 实例，`file_path` 变量就会存储你选择的文件路径。
def open_file(entry,i):
    filepath = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filepath)
    file_paths[i] = filepath  # 存储文件路径
    #print(len(file_paths), i, file_paths[i])
'''

yuv_formats = ["T_Y8", "T_Y10", "T_Y12", "T_Y14", "T_Y16", "T_Y8___V8U8_N422", "T_Y10___V10U10_N422", 
   "T_Y12___V12U12_N422", "T_Y8___U8V8_N420", "T_Y10___U10V10_N420", "T_Y10___U2V2_N420", "T_Y10___U2V2_V2U2_N420",
   "T_Y10___V2U2_N420", "T_Y10___V2V2_N420", "T_Y12___U2V2_N420", "T_Y13___U2V2_N420", "T_Y14___U2V2_N420", 
   "T_Y8___U4V4_N420", "T_Y10___U4V4_N420", "T_Y10___U6V6_N420", "T_Y10___U8V8_N420", "T_Y10___U10V10_N420", 
   "T_Y10___U12V12_N420", "T_Y12___U12V12_N420", "T_Y14___U14V14_N420", "T_Y8___U8___V8_N420", "T_Y10___U10___V10_N420",
   "T_Y8___U8___V8_N422", "T_Y10___U10___V10_N422", "T_Y8___V8___U8_N420", "T_Y10___V10___U10_N420", "T_Y8___V8___U8_N422", 
   "T_Y10___V10___U10_N422"]


def get_file_paths():
    print(len(file_paths), file_paths[0])
    return file_paths

def open_path(file_entry, plane_idx):
        global filename
        filename = tk.filedialog.askopenfilename(filetypes=[('Binary Files', '*.bin'), ('All files', '*.*')])
        if filename: # 检查用户是否选择了文件
            file_entry.delete(0, tk.END) # 清除entry中的内容
            file_entry.insert(0, filename) # 将文件路径插入到entry中
            file_paths[plane_idx] = filename  # 保存文件路径至全局字典


def make_file_entry_and_button(plane_idx):
    # 创建 Entry 对象
    file_entry = tk.Entry(root, width=20)  # width 用于设置 Entry 的宽度
    file_entry.place(x=100, y=plane_idx * 30 + 170)  # 适当位置放置 Entry 对象

    # 创建 Button 对象
    load_button = tk.Button(root, text=f'Load Plane{plane_idx}', command=lambda: open_path(file_entry, plane_idx))
    load_button.place(x=255, y=plane_idx * 30 + 165)  # 在 Entry 对象的旁边放置 Button 对象

    file_entries.append(file_entry)
    open_buttons.append(load_button)


def update_entries_and_buttons():
    global num_planes
    # 销毁旧的条目和按钮
    for entry in file_entries:
        entry.destroy()
    for button in open_buttons:
        button.destroy()

    file_entries.clear()
    open_buttons.clear()

    # 为新的 plane 数目创建条目和按钮
    for i in range(num_planes):
        make_file_entry_and_button(i)

def on_format_selected(event):
    global num_planes
    selected_format = format_var.get()
    # 你可以根据所选格式设置 num_planes
    # 作为示例，我只是随机设置了一个数值
    num_planes = format_to_planes(selected_format)  # 在这里设置你的 plane 取值
    update_entries_and_buttons()

# 函数，控制条目和按钮的显示/隐藏
def format_to_planes(format):
    if "2P" in format:
        return 2
    elif "3P" in format:
        return 3
    else:
        return 1
##################################################################################
def main():
    global root, width_entry, height_entry, pitch_entry, format_var,num_planes
    # 创建 tkinter 窗口
    root = tk.Tk()

    # 设置窗口的大小
    root.geometry('1170x850')

    # 设置窗口的图标
    #root.iconphoto(False, tk.PhotoImage(file="logo.png"))

    # 创建一个白色背景的 Frame 控件
    frame = tk.Frame(root, bg='white', width=750, height=750)
    frame.place(x=ax_x, y=ax_y)
    # 将鼠标左键单击事件绑定到 Frame 上
    #frame.bind("<Button-1>", lambda e: show_real_size())

    # 创建 Label 和 Entry 对象
    width_label = tk.Label(root, text="Width:", anchor="w")
    width_label.place(x=10, y=10)
    width_entry = tk.Entry(root, width=10)
    width_entry.place(x=100, y=10)

    height_label = tk.Label(root, text="Height:", anchor="w")
    height_label.place(x=10, y=40)
    height_entry = tk.Entry(root, width=10)
    height_entry.place(x=100, y=40)

    pitch_label = tk.Label(root, text="Pitch:", anchor="w")
    pitch_label.place(x=10, y=70)
    pitch_entry = tk.Entry(root, width=10)
    pitch_entry.place(x=100, y=70)

    # 创建菜单栏
    menubar = tk.Menu(root)

    # 创建文件菜单
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_image_file)
    menubar.add_cascade(label="File", menu=filemenu)

    # 创建帮助菜单
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=show_help)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # 显示菜单栏
    root.config(menu=menubar)

    # 创建 Label 对象
    format_label = tk.Label(root, text="Format:", anchor="w")
    format_label.place(x=10, y=100)

    # 创建 StringVar 对象
    format_var = tk.StringVar()

    # 创建 Combobox 对象
    #format_combobox = ttk.Combobox(root, textvariable=format_var, values=['ARGB8888', 'YUV', 'RGB888', 'A2Y10U10V10', 'A2R10G10B10', 'A2B10G10R10'])
    format_combobox = ttk.Combobox(root, textvariable=format_var, values=fp.img_formats)
    format_combobox.place(x=100, y=100)
    format_combobox.bind("<<ComboboxSelected>>", on_format_selected)

    # 在画布上创建一个透明的矩形，覆盖整个画布
    #rect = canvas.create_rectangle(0, 0, 500, 400, fill='', outline='')
    #canvas.tag_bind(rect,"<Button-1>", lambda e: show_real_size())

    # 创建 Button 对象
    save_img_button = tk.Button(root, text="save", command=lambda : save_img_file(save_img))
    save_img_button.place(x=10, y=200)

    ori_img_button = tk.Button(root, text="show_bin", command=lambda : open_bin_file())
    ori_img_button.place(x=10, y=170)
    # 运行 tkinter 主循环
    #root.after(100, update_frame)
    # 运行 tkinter 主循环
    #root.after(100, play_gif)
    # 在 main() 函数内部或者其他适当的位置调用 make_file_entry_and_button() 函数
    for i in range(num_planes):
        make_file_entry_and_button(i)
    
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

# 通过判断 __name__ 是否为 "__main__"来确定是否执行 main() 函数
if __name__ == "__main__":
    main()