# -*- coding: utf-8 -*-
import numpy as np

fs = 10e9  # Sampling frequency in Hz (10 GHz)
ts = 1 / fs  # Sampling period in seconds

adc_bits = 7  # ADC resolution
lsb_error = 1 / (2 ** adc_bits)  # 1 LSB error threshold

# Solve for tau using the equation: exp(-ts/tau) <= 1/128
ln_threshold = np.log(1 / (2 ** adc_bits))

tau = ts / abs(ln_threshold)  # Compute tau

# Print the result
print(f"Required time constant (tau) to keep sampling error < 1 LSB: {tau:.2e} seconds ({tau * 1e12:.2f} ps)")
