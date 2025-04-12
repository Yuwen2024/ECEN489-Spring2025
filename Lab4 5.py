import numpy as np
import matplotlib.pyplot as plt

# Given DNL values for 3-bit ADC
dnl = np.array([0, -0.5, 0, 0.5, -1, 0.5, 0.5, 0])

# Calculate INL as cumulative sum of DNL
inl = np.cumsum(dnl)

# Offset and Full-Scale error in LSBs
offset_error = 0.5  # +0.5 LSB
full_scale_error = 0.5  # +0.5 LSB

# Number of codes
codes = np.arange(8)

# Ideal transfer curve (normalized from 0 to 7 LSBs)
ideal_output = codes

# Real transfer curve: include offset and scale factor
# Full-scale error affects the slope.
# Ideal full-scale step = 7 LSBs. New full-scale step = 7 + 0.5 = 7.5 LSBs
# So scale factor = (7.5 / 7)

scale_factor = (7 + full_scale_error) / 7
real_output = offset_error + (codes * scale_factor) + inl  # add offset and INL effects

# Print INL values
print("Code | DNL (LSB) | INL (LSB)")
print("-----------------------------")
for code in range(8):
    print(f" {code:3d} | {dnl[code]:8.2f} | {inl[code]:8.2f}")

# Plot Transfer Curve
plt.figure(figsize=(8,6))
plt.plot(codes, ideal_output, 'o-', label='Ideal Transfer Curve', markersize=8)
plt.plot(codes, real_output, 's--', label='Real Transfer Curve (with errors)', markersize=8)
plt.title('ADC Transfer Curve')
plt.xlabel('Input Code')
plt.ylabel('Output Level (LSBs)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
