
# coding=utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windows 和 linux 设置字体的方式
# 1、设置 matplotlib 显示中文字体
# font = {'family': 'Microsoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
#
# matplotlib.rc("font", **font)

# 2、使用 font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")   # 添加字体路径

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

fig = plt.figure(figsize=(25, 8), dpi=80)


# 绘图
plt.plot(x, y)

# 调整x轴
_xtick_lables = ["10点{}分".format(i) for i in range(60)]
_xtick_lables += ["11点{}分".format(i-60) for i in range(60,120)]
# 如果想要使用字符串，那么 x 和 _xtick_lables 必须一一对应,数据的长度一样
plt.xticks(list(x)[::3], _xtick_lables[::3], rotation=45, fontproperties=my_font)   #rotation旋转的度数

# 添加描述信息

plt.xlabel("时间", fontproperties=my_font)    # 横坐标
plt.ylabel("温度 单位（℃）", fontproperties=my_font)      # 纵坐标
plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)      #标题




plt.show()