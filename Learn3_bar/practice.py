
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

"""
假设你知道了列表a中电影分别在
2017-09-14(b_14), 
2017-09-15(b_15), 
2017-09-16(b_16)三天的票房,
为了展示列表中电影本身的票房以及同其他电影的数据对比情况,
应该如何更加直观的呈现该数据?

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

注意：本练习为绘制多次条形图
"""


# 设置数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

# 设置汉子显示
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

bar_width = 0.3

# 绘制条形图
x_14 = list(range(len(a)))
x_15 = [i + bar_width for i in x_14]
x_16 = [i + bar_width*2 for i in x_14]

# 设置图形大小
plt.figure(figsize=(15,8),dpi=80)

plt.bar(x_14, b_14, width=bar_width, label = "9月14日")
plt.bar(x_15, b_15, width=bar_width, label = "9月15日")
plt.bar(x_16, b_16, width=bar_width, label = "9月16日")

# 编辑x轴
_xtick_labels = x_14
_xtick_labels += x_15
_xtick_labels += x_16
plt.xticks(x_15, a, fontproperties = my_font)

# 编辑y轴

# 编辑图例
plt.legend(prop = my_font, loc = "center right")

# 显示图形
plt.show()