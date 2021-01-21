
import matplotlib.pyplot as plt
from random import random

input_values = [1, 2, 3, 4, 5, 6]  # x轴数据
squares = [1, 4, 9, 16, 25, 36]  # y轴数据
y_altitude = [1, 4, 9, 16, 25, 36]
y_target_altitude = [6, 6, 6, 6, 6, 6]
y_controlvalue = [1, 2, 3, 4, 5, 6]
#plt.plot(squares)
# plt.plot(input_values, squares, linewidth=5)  # 绘制线条粗细。
# plt.title("Square Numbers", fontsize=24)  # 绘制图表标题。
# plt.xlabel("Value", fontsize=14)  # x轴绘制标签。
# plt.ylabel("Square of Value", fontsize=14)  # y轴绘制标签
# plt.tick_params(axis='both', labelsize=14)  # 设置刻度标记样式
fig, (ax_altitude, ax_controlvalue) = plt.subplots(2, 1)  # 设置子图样式，两行一列。
fig.suptitle('Althod curve', fontsize = 24)  # 绘制子图标题。
ax_altitude.set_ylabel('surface altitude(m)')  
ax_controlvalue.set_ylabel('control vaule(%)')
ax_controlvalue.set_xlabel('time(s)')
#ax_altitude.set_ylim([0, 2000])
#ax_controlvalue.set_ylim([-100, 200])
ax_altitude.plot(input_values, y_altitude, 'b', lw = 1) # draw line chart
ax_altitude.plot(input_values, y_target_altitude, 'r', lw = 1)
ax_controlvalue.plot(input_values, y_controlvalue, 'y', lw =1)
plt.pause(5)
ax_altitude.cla() # clear plot
ax_controlvalue.cla()
ax_altitude.plot(input_values, y_altitude, 'b', lw = 1) # draw line chart
ax_altitude.plot(input_values, y_target_altitude, 'r', lw = 1)
ax_controlvalue.plot(input_values, y_controlvalue, 'y', lw =1)
plt.pause(20)

