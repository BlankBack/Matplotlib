
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

"""
                练习
假设大家在30岁的时候,根据自己的实际情况,
统计出来了你和你同桌各自从11岁到30岁每年交的女(男)朋友的数量如列表a和b,
请在一个图中绘制出该数据的折线图,
以便比较自己和同桌20年间的差异,
同时分析每年交女(男)朋友的数量走势
    a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
    b = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]
要求:
    y轴表示个数
    x轴表示岁数,比如11岁,12岁等
"""

# 定义变量
x = range(11,31)
y_a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_b = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

# 设置显示中文

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")   # 添加字体路径


# 对所绘的图进行编辑，设置图片大小
fig = plt.figure(figsize=(20,8),dpi=80)     # dpi 的意思是每英寸


# 绘图;
# 设置标签label;指定折线的颜色 color ;线条风格 line style ;线条粗细 line width
plt.plot(x,y_a,label="自己", color = "red", linestyle = ":", linewidth = 5)
plt.plot(x,y_b,label="同桌",color = "cyan", linestyle = "--", linewidth = 3)

# 绘制 x/y 轴的刻度
# 自己写的
# _xtick_lavles = [i/2 for i in range(22,61)]
# plt.xticks(_xtick_lavles[::2])
# 视频讲授
_xtick_lavles = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_lavles, fontproperties = my_font)

plt.yticks([ i/2 for i in range(0,16)])

# 添加描述信息
plt.xlabel("岁数",fontproperties = my_font)
plt.ylabel("个数",fontproperties = my_font)
plt.title("我和同桌每年交女(男)朋友的数量走势折线图", fontproperties=my_font)

# 绘制及设置网格
plt.grid(alpha = 0.5, color = "green")   # alpha 为透明度（0-1）

# 添加图例
# 需要两步，设置label参数，调用legend
plt.legend(prop=my_font, loc="upper left")    # 就是对折线进行说明

# 保存
# plt.savefig("./t3.png")

# 展示图形

plt.show()












