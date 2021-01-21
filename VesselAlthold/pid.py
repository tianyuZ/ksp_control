"""[summary]
    pid 基类
"""
#from pid_controller.pid
import math

class Pid :
    """ pid控制器基类 """
    def __init__(self, kp, ki, kd, upper, lower) :
        self.kp_ = kp
        self.ki_ = ki
        self.kd_ = kd
        self.__saturation_value_upper_ = upper  # 执行器饱和值上界。
        self.__saturation_value_lower_ = lower  # 执行器饱和值下界。
        self.saturation_flag_ = False  # 是否需要抗积分饱和标志

    def SetP(self, kp) :
        self.kp_ = kp

    def SetI(self, ki) :
        self.ki_ = ki

    def SetD(self, kd) :
        self.kd_ = kd

    def Set_SaturationValue(self, upper, lower) :
        self.__saturation_value_upper_ = upper
        self.__saturation_value_lower_ = lower

    def anti_windup(self, u, error) :
        """ 抗积分饱和。
            积分上限为正值。
            积分下限非正。

        Args:
            u : pid控制器原始输出量。
            error: 目标值与实际值之差。
        Returns:
            经抗积分饱和处理后的pid控制器输出量。
            积分项是否需要继续累加误差值。
        """
        if u >= self.__saturation_value_upper_ :
            u = self.__saturation_value_upper_
            if error > 0.0 :
                flag = True
            else :
                flag = False
        else :
            flag =  False
        
        if u <= self.__saturation_value_lower_ :
            u = self.__saturation_value_lower_
            if error < 0.0 :  
                flag = True
            else :
                flag = False
        elif flag != True :
            flag =False

        return u, flag
    