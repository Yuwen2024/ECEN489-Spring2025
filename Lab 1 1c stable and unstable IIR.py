import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, butter

# Stable Filter: Define coefficients
# Order of the filter is 4, and cutoff frequency is 0.2 (normalized)
b_stable, a_stable = butter(4, 0.2)

# Unstable Filter
b_unstable = [1]
a_unstable = [1, -1.5, 0.7]  # The coefficient -1.5 will make it unstable

# Compute frequency responses of both filters
w_stable, h_stable = freqz(b_stable, a_stable, worN=8000)
w_unstable, h_unstable = freqz(b_unstable, a_unstable, worN=8000)

# Plot the frequency responses
plt.figure(figsize=(10, 8))

# Stable Filter Magnitude and Phase
plt.subplot(2, 2, 1)
plt.plot(w_stable / np.pi, np.abs(h_stable), 'b')
plt.title('Stable Filter - Magnitude Response')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude')


# Unstable Filter Magnitude and Phase
plt.subplot(2, 2, 3)
plt.plot(w_unstable / np.pi, np.abs(h_unstable), 'r')
plt.title('Unstable Filter - Magnitude Response')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude')


plt.tight_layout()
plt.show()
