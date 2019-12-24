# implementation of a maximum power point tracking algorithm 
# to experiment

import math
import matplotlib.pyplot as plt
import numpy as np

# Global variables
V_START = 0.1
DELTA_V = 0.05
G= 1

class MPPT:

    def __init__(self):
        return

    def calculate_current_function(self, voltage):
        current = 1000*G-math.exp((voltage/0.1))*0.01
        return current

    # power calculation with model of single CV sell 
    def calculate_power_function(self, voltage):
        current = self.calculate_current_function(voltage)
        power = current*voltage
        return power

    def plot_power_function(self, idle_voltage, step):
        current_voltage = 0
        voltage_list = [current_voltage]
        current_list = [self.calculate_current_function(current_voltage)]
        power_list = [self.calculate_power_function(current_voltage)]
        while (current_voltage<=idle_voltage):
            current_voltage = current_voltage + step
            power_list = power_list + [self.calculate_power_function(current_voltage)]
            voltage_list = voltage_list + [current_voltage]
        
        plt.plot(voltage_list, power_list)
        plt.show()       


    # max power point tracking algorithm
    def max_power_point_tracking(self, v_start, delta_v):

        v_old = v_start
        v_current = v_start + delta_v

        v_collector = [v_start]
        p_collector = [self.calculate_power_function(v_start)]
        print(type(v_collector))

        for i in range(100):
            #power calculations
            p_old = self.calculate_power_function(v_old)
            p_current= self.calculate_power_function(v_current)
            output = [v_current, p_current]
            #print(output)
            v_collector =  v_collector + [v_current]
            p_collector = p_collector + [p_current]

            if (p_current>p_old):
                if(v_current > v_old):
                    v_old = v_current
                    v_current = v_current + delta_v
                else:
                    v_old = v_current
                    v_current = v_current - delta_v
                
            else:
                if(v_current > v_old):
                    v_old = v_current
                    v_current = v_current - delta_v
                else:
                    v_old = v_current
                    v_current = v_current + delta_v    



def main():
    mppt = MPPT()
    mppt.plot_power_function(1.15, 0.01)
    mppt.max_power_point_tracking(V_START, DELTA_V)

if __name__ == "__main__":
    main()