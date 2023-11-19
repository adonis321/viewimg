import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# 函数，用于选择文件并更新条目的内容
# 使用方法：
# 当你调用 `open_file` 函数并传入一个 Entry 实例，`file_path` 变量就会存储你选择的文件路径。
def open_file(entry,i,file_paths):
    filepath = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filepath)
    file_paths[i] = filepath  # 存储文件路径
    print(len(file_paths), i, file_paths[i])

# 函数，控制条目和按钮的显示/隐藏
def format_to_planes(format):
    if "N420" in format:
        return 2
    elif "N422" in format:
        return 3
    else:
        return 1

def toggle_entries(format_combox,file_entries,open_buttons,num_planes):
    format = format_combox.get()  # 注意这里改为format_combobox.get()
    planes = format_to_planes(format)
    for i in range(num_planes):
        if i < planes:
            file_entries[i].pack()
            open_buttons[i].pack()
        else:
            file_entries[i].pack_forget()
            open_buttons[i].pack_forget()

#window = tk.Tk()

# 所有的YUV格式
img_formats = ["A2R10G10B10_1P","A2B10G10R10_1P","T_Y8_1P", "T_Y10_1P", "T_Y12_1P", "T_Y14_1P", "T_Y16_1P", "T_Y8___V8U8_N422_2P", "T_Y10___V10U10_N422_2P", 
   "T_Y12___V12U12_N422_2P", "T_Y8___U8V8_N420_2P", "T_Y10___U10V10_N420_2P", "T_Y10___U2V2_N420_2P", "T_Y10___U2V2_V2U2_N420_2P",
   "T_Y10___V2U2_N420_2P", "T_Y10___V2V2_N420_2P", "T_Y12___U2V2_N420_2P", "T_Y13___U2V2_N420_2P", "T_Y14___U2V2_N420_2P", 
   "T_Y8___U4V4_N420_2P", "T_Y10___U4V4_N420_2P", "T_Y10___U6V6_N420_2P", "T_Y10___U8V8_N420_2P", "T_Y10___U10V10_N420_2P", 
   "T_Y10___U12V12_N420_2P", "T_Y12___U12V12_N420_2P", "T_Y14___U14V14_N420_2P", "T_Y8___U8___V8_N420_3P", "T_Y10___U10___V10_N420_3P",
   "T_Y8___U8___V8_N422_3P", "T_Y10___U10___V10_N422_3P", "T_Y8___V8___U8_N420_3P", "T_Y10___V10___U10_N420_3P", "T_Y8___V8___U8_N422_3P", 
   "T_Y10___V10___U10_N422_3P"]

def make_open_file_button(root,format_combobox,file_entries,open_buttons,num_planes,file_paths):
    print(num_planes)
    '''
        # 创建条目和按钮
        for i in range(num_planes):
            filepath_entry = tk.Entry(root)
            filepath_entry.pack_forget()  # 默认隐藏
            filepath_entry.place(x=100, y=170+30*i)
            file_entries.append(filepath_entry)
            print('make_butn')
            #open_button = tk.Button(window, text=f'Open file {i}', command=lambda i=i: open_file(file_entries[i]))
            open_button = tk.Button(root, text=f'Plane{i}', command=lambda i=i: open_file(file_entries[i], i, file_paths))
            open_button.pack_forget()  # 默认隐藏
            open_button.place(x=100, y=170+80*i)
            open_buttons.append(open_button)
    '''


    #print(len(file_paths), file_paths[0])
    #label = tk.Label(root, text="Format:")
    #label.pack()

    # 格式下拉选择框 (Combobox)
    #format_combobox = ttk.Combobox(root, values=yuv_formats)  
    format_combobox.bind("<<ComboboxSelected>>", toggle_entries(format_combobox,file_entries,open_buttons,num_planes))  # 当下拉列表的值被选择，执行toggle_entries函数。
    #format_combobox.pack()
