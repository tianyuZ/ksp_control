from pid import Pid
import math

class PidPos(Pid) :
    """ 位置式pid,继承自Pid基类. """

    def __init__(self, kp, ki, kd, upper, lower) :  # 增量重载
        super().__init__(kp, ki, kd, upper, lower)
        self.__integration_ = 0.0  # 位置式误差累加和。
        self.__error_pre_ = 0.0

    def __rmul__(self, error) :
        """ `*` 运算符重载。

        Args:
            error : 目标值与实际值之差

        Retruns:
            位置式pid控制器输出量。            

        """
        proportion = self.kp_ * error  # 比例项
        if self.saturation_flag_ == False :  # 依据抗积分饱和标志判断是否对累加项进行处理
            self.__integration_ += error 
        intergration = self.ki_ * self.__integration_  # 积分项
        differentiation = self.kd_ * (error - self.__error_pre_) # 微分项
        u = proportion + intergration + differentiation
        self.__error_pre_ = error
        u, self.saturation_flag_ = self.anti_windup(u, error)  # 抗积分饱和处理
        return u 

    

               
        