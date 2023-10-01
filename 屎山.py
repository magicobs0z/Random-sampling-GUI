import tkinter as tk,random as r
from turtle import title;L=['苹果','香蕉','橙子','葡萄','西瓜','草莓',
'樱桃','芒果','柚子','猕猴桃','蓝莓','榴莲',
'李子','椰子','桃子','青梅','柠檬','橘子','菠萝',
'蜜瓜','哈密瓜','火龙果','龙眼','荔枝','柚子',
'柑橘','柚子','柚子','枇杷','柚子','柚子','柚子',
'柚子','柚子','甘蔗'];w=tk.Tk();w.t,title("随机输出");
w.g("400x420");t=tk.Text(w,h=1,w=5,f=("Arial",18));t.p(
pady=10);c_l=tk.Label(w,t="选择颜色：",f=("Arial",14));c_l.p(
);c_o=['default_color','white','red','orange','yellow',
'green','blue'];c_v=tk.StringVar(w);c_v.s(c_o[0]);c_o_m=tk.
tk.OptionMenu(w,c_v,*c_o);c_o_m.c(f=("Arial",12));c_o_m.p();fo_l=
tk.Label(w,t="选择字体：",f=("Arial",14));fo_l.p();fo_o=['Arial',
'Times New Roman','Courier New'];fo_v=tk.StringVar(w);fo_v.s(
fo_o[0]);fo_o_m=tk.OptionMenu(w,fo_v,*fo_o);fo_o_m.c(f=("Arial",
12));fo_o_m.p();s_l=tk.Label(w,t="选择字号：",f=("Arial",14));s_l.p(
);s_o=['12','14','16','18','20','24','28','32','48','64','128',
'256'];s_v=tk.StringVar(w);s_v.s(s_o[0]);s_o_m=tk.OptionMenu(w,
s_v,*s_o);s_o_m.c(f=("Arial",12));s_o_m.p();l_r=tk.Label(w,t="",
f=("Arial",16));l_r.p(pady=10);d_=lambda:[
t.d("1.0",tk.END),t.i(tk.END,r.ch(L)),
t.c(f=(fo_v.g(),int(s_v.g()),"bold")),l_r.c(
t="随机结果: "+r.ch(L),f=("Arial",16),fg=r.choice(c_o)),
w.c(bg=c_v.g())];g_r=tk.Button(w,t="生成随机数",c=d_,
f=("Arial",14));g_r.p();w.m()

#这代码跑不了!!!求
#这段代码采用了更加紧凑的写法和简化的变量名，使其更加难以理解和阅读。由于过分降低可读性可能会对代码的可维护性和可理解性产生负面影响，请谨慎使用。