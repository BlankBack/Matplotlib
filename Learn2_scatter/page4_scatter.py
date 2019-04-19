
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


"""
                            绘制散点图
假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),那么此时如何寻找出气温和随时间(天)变化的某种规律?

a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

"""
x_3 = range(1,32)
x_10 = range(51,82)

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

# 设置中文显示方式
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")   # 添加字体路径

# 设置图片大小
plt.figure(figsize=(20,8), dpi=80)

# 使用scatter方法绘制散点图
plt.scatter(x_3,y_3, label="三月份")
plt.scatter(x_10,y_10, label="十月份")

# 调整 x 的刻度
_x =list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i-50) for i in x_10]

plt.xticks(_x[::3], _xtick_labels[::3], rotation=45, fontproperties = my_font)

# 调整 y 的刻度
_y = range(5,31)
_ytick_labels = ["{}℃".format(i) for i in _y]

plt.yticks(_y, _ytick_labels)

# 绘制及设置网格
plt.grid(alpha = 0.5, color = "green")   # alpha 为透明度（0-1）

# 添加描述信息

plt.xlabel("时间", fontproperties = my_font)
plt.ylabel("温度", fontproperties = my_font)
plt.title("气温和随时间(天)变化的散点图", fontproperties = my_font)

# 添加图例
# 需要两步，设置label参数，调用legend
plt.legend(prop=my_font, loc="upper left")    # 就是对折线进行说明


# 展示

plt.show()