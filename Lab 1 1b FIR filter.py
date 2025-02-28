import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Define custom FIR filter coefficients
# coefficients for a FIR filter (low-pass)
filter_coeffs = np.array([1, 1, 1, 1, 1])  # Simple average filter (box filter)

# Compute the frequency response of the filter
w, h = freqz(filter_coeffs, worN=8000)

# Plot the frequency response
plt.figure(figsize=(8, 6))

# Plot magnitude response
plt.subplot(2, 1, 1)
plt.plot(w / np.pi, np.abs(h), 'b')
plt.title('Frequency Response of the FIR Filter')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude')

# Plot phase response
plt.subplot(2, 1, 2)
plt.plot(w / np.pi, np.angle(h), 'g')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Phase (radians)')

plt.tight_layout()
plt.show()
