
from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

# 对所绘的图进行编辑
# 设置图片大小
fig = plt.figure(figsize=(20,8),dpi=80)     # dpi 的意思是每英寸

# 绘图
plt.plot(x,y)

# 绘制 x 轴的刻度
# # 1、绘制太稀疏，变得密集的方法
# _xtick_lavles = [i/2 for i in range(4,49)]
# plt.xticks(_xtick_lavles)

# 2、绘制太密集，变得稀疏的方法
# 该操作为列表取步长（间隔取值），即在原来的基础上每隔 4 个 i/2 取一个
_xtick_lavles = [i/2 for i in range(4,49)]
plt.xticks(_xtick_lavles[::2])

# 绘制 y 轴的刻度，方法相同
plt.yticks(range(min(y),max(y)+1))



# 保存
# plt.savefig("./t1.png")

# 展示图形
plt.show()











