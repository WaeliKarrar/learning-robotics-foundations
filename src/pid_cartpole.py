import time

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp  # Proportional: How hard to push now
        self.ki = ki  # Integral: Fixes long-term drift
        self.kd = kd  # Derivative: Prevents overshooting
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value, dt):
        error = setpoint - measured_value
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        
        self.prev_error = error
        return output

# --- Main Simulation Loop Placeholder ---
# In a real robotics sim (like Gymnasium), you would apply 
# the 'output' force to the cart here.
print("PID Controller for Cart-Pole initialized.")