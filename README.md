# Random-sampling-GUI
这是一个拥有用户界面的随机抽取工具，有许多可调选项
## 介绍
代码的第9行放的就是你想要的文字,把这里替换成你想要的随机字符串，然后编译就可以了
注释写得很清楚了，各种功能都可以加，改，你可以随便使用这个项目，只要不删除第1,2行注释就可以
特别简单的一个项目，希望可以给你的生活带来方便
## 使用方法
*首先你需要有一个python，然后在你的代码编辑器里面打开源文件，按照你的需要，修改下面这一段代码*
```
# 创建一个列表
# 在这改
my_list = ['苹果', '香蕉', '橙子', '葡萄', '西瓜', '草莓', '樱桃', '芒果', '柚子', '猕猴桃', '蓝莓', '榴莲', '李子', '柚子', '椰子',
           '桃子', '青梅', '柠檬', '橘子', '菠萝', '蜜瓜', '哈密瓜', '火龙果', '龙眼', '荔枝', '柚子', '柑橘', '柚子', '柚子', '枇杷',
           '柚子', '柚子', '柚子', '柚子', '柚子', '甘蔗']
```
修改格式为 '香蕉' 把这里面的香蕉换成你想要的字.
当你做完这一切以后，保存即可，运行就可以了.
*有手就行*           
## 细节
这个程序里面有很多的可调节的选项，字体，大小，颜色。这些都是可以调节的，你可以自由添加，这部分代码如下所示awa
```
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
```
好,掰掰
