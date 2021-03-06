
from matplotlib import pyplot as plt
from matplotlib import  font_manager
import matplotlib

"""
在美国2004年人口普查发现有124 million的人在离家相对较远的地方工作。
根据他们从家到上班地点所需要的时间,通过抽样统计(最后一列)出了下表的数据,

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

"""
# 设置显示汉字
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

# 设置图形大小
plt.figure(figsize=(18, 8), dpi=80)

# 设置变量
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

plt.bar(range(len(quantity)),quantity,width=1)

# 设置x轴
_x = [i-0.5 for i in range(13)]
_xtick_labels = interval + [150]
plt.xticks(_x, _xtick_labels)

plt.grid(alpha=0.5)

plt.show()