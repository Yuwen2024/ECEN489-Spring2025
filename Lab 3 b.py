# -*- coding: utf-8 -*-


import numpy as np

V_initial = 0.5  # V (NRZ signal amplitude)
V_lsb = 1 / 128  # LSB value in V for 7-bit ADC
T_hold = 50e-12  # 50 ps (Hold time due to 50% duty cycle at 10 Gb/s)

# Calculate required time constant tau
tau_required = T_hold / abs(np.log(V_lsb / V_initial))

# Print result
print(f"Required time constant (tau) to keep error < 1 LSB: {tau_required * 1e12:.2f} ps")
