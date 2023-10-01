# 这个代码在github开源了  https://github.com/magicobs0z/Random-sampling-GUI
# 作者:magicobs0z (芝)
import tkinter as tk
from tkinter import messagebox
import random

# 创建一个列表
# 在这改
my_list = ['苹果', '香蕉', '橙子', '葡萄', '西瓜', '草莓', '樱桃', '芒果', '柚子', '猕猴桃', '蓝莓', '榴莲', '李子', '柚子', '椰子',
           '桃子', '青梅', '柠檬', '橘子', '菠萝', '蜜瓜', '哈密瓜', '火龙果', '龙眼', '荔枝', '柚子', '柑橘', '柚子', '柚子', '枇杷',
           '柚子', '柚子', '柚子', '柚子', '柚子', '甘蔗']

# 创建窗口
window = tk.Tk()
window.title("随机输出")
window.geometry("400x420")


# 创建文本框
text_box = tk.Text(window, height=1, width=5, font=("Arial", 18))
text_box.pack(pady=10)

# 创建颜色选择标签和下拉菜单
color_label = tk.Label(window, text="选择颜色：", font=("Arial", 14))
color_label.pack()

color_options = ['default_color','white', 'red', 'orange', 'yellow', 'green', 'blue']
color_var = tk.StringVar(window)
color_var.set(color_options[0])  # 默认选择第一个颜色

color_option_menu = tk.OptionMenu(window, color_var, *color_options)
color_option_menu.config(font=("Arial", 12))
color_option_menu.pack()

# 创建字体选择标签和下拉菜单
font_label = tk.Label(window, text="选择字体：", font=("Arial", 14))
font_label.pack()

font_options = ['Arial', 'Times New Roman', 'Courier New']
font_var = tk.StringVar(window)
font_var.set(font_options[0])  # 默认选择第一个字体

font_option_menu = tk.OptionMenu(window, font_var, *font_options)
font_option_menu.config(font=("Arial", 12))
font_option_menu.pack()

# 创建字号选择标签和下拉菜单
size_label = tk.Label(window, text="选择字号：", font=("Arial", 14))
size_label.pack()

size_options = ['12', '14', '16', '18', '20','24','28','32','48','64','128','256']
size_var = tk.StringVar(window)
size_var.set(size_options[0])  # 默认选择第一个字号

size_option_menu = tk.OptionMenu(window, size_var, *size_options)
size_option_menu.config(font=("Arial", 12))
size_option_menu.pack()

# 创建Label用于显示随机结果
label_result = tk.Label(window, text="", font=("Arial", 16))
label_result.pack(pady=10)

# 定义按钮点击事件
def generate_random():
    # 从列表中随机选择一个元素
    random_item = random.choice(my_list)
    # 在文本框中显示随机选择的元素
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, random_item)
    # 设置文本框的字体和字号
    text_box.configure(font=(font_var.get(), int(size_var.get()), "bold"))
    # 设置随机结果的字体和颜色
    label_result.config(text="随机结果: " + random_item, font=("Arial", 16),
                        fg=random.choice(color_options))
    # 设置窗口背景颜色
    window.configure(bg=color_var.get())

# 创建按钮
button = tk.Button(window, text="生成随机数", command=generate_random, font=("Arial", 14))
button.pack()

# 运行窗口主循环
window.mainloop()