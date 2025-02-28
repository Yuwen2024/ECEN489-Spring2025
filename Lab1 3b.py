import numpy as np
import matplotlib.pyplot as plt

# Parameters
F1 = 200e6  # Frequency of the first component in Hz
F2 = 400e6  # Frequency of the second component in Hz
Fs = 1e9   # Sampling frequency in Hz
N = 50     # Number of samples

t = np.arange(N) / Fs  # Time vector
y = np.cos(2 * np.pi * F1 * t) + np.cos(2 * np.pi * F2 * t)  # Generate the signal

# Compute the DFT using FFT
Y = np.fft.fft(y)
frequencies = np.fft.fftfreq(N, 1/Fs)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 6))
plt.stem(frequencies, np.abs(Y), basefmt=" ", use_line_collection=True)
plt.title('50-Point DFT of y(t) = cos(2πF1t) + cos(2πF2t) with F1 = 200 MHz and F2 = 400 MHz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()