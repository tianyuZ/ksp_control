from pospid import PidPos
import krpc, time
import matplotlib.pyplot as plt

# 设置所绘响应曲线图样式
#plt.title("Althold curve", fontsize = 24)  # 绘制标题。
#plt.xlabel("time(s)", fontsize = 14)  # x轴绘制标签。
#plt.ylabel("surface altitude(m)", fontsize = 14)  # y轴绘制标签
#plt.ylim([0, 1000]) # 设置纵坐标轴范围为 0 到 1000
fig, (ax_altitude, ax_controlvalue) = plt.subplots(2, 1)  # 设置子图样式，两行一列。
fig.suptitle('Althod curve', fontsize = 24)  # 绘制子图标题。
# ax_altitude.set_ylabel('surface altitude(m)')  
# ax_controlvalue.set_ylabel('control vaule(%)')
# ax_controlvalue.set_xlabel('time(s)')
#ax_altitude.set_ylim([0, 2000])
#ax_controlvalue.set_ylim([-100, 200])
x_time = []
y_altitude = []
y_controlvalue = []
y_target_altitude = []

conn = krpc.connect(name = 'vessel_althod')
vessel = conn.space_center.active_vessel

target_altitude = 200
#定义pospid控制器
pospidcontroller = PidPos(0.7, 0.0039, 28, 100.0, 0.0)

# 1.设置火箭姿态 油门 开启自动驾驶
vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.target_roll = 0
vessel.auto_pilot.engage()
#vessel.control.throttle = 1  # throttle 100%
time.sleep(1)

# 2.激活第一分级及发射
print('Launch!')
vessel.control.activate_next_stage()  # 激活下一分级，相当于手操空格键。
start_time = time.time()

while True :
    # 得到当前相对地面高度
    current_altitude = vessel.flight().surface_altitude
    #计算目标高度与当前高度差值。
    error_altitude = target_altitude - current_altitude
    #偏差值通过控制器得到控制量。
    control = error_altitude * pospidcontroller
    #控制量缩放后赋值给节流阀。
    vessel.control.throttle = control / 100.0
#   time.sleep(0.01)
    # 绘制曲线图
    ax_altitude.set_ylabel('surface altitude(m)')  
    ax_controlvalue.set_ylabel('control vaule(%)')
    ax_controlvalue.set_xlabel('time(s)')
    x_time.append(time.time() - start_time)
    y_altitude.append(current_altitude)
    y_target_altitude.append(target_altitude)
    y_controlvalue.append(control)
    ax_altitude.plot(x_time, y_altitude, 'b', lw = 1) # draw line chart
    ax_altitude.plot(x_time, y_target_altitude, 'r', lw = 1)
    ax_controlvalue.plot(x_time, y_controlvalue, 'y', lw =1)
    # ax.bar(y, height=y, width=0.3) # draw bar chart   
    plt.pause(0.01)
    if abs(error_altitude) <= 6 :
        print(current_altitude) 
    ax_altitude.cla() # clear plot
    ax_controlvalue.cla()