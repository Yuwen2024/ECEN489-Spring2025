import numpy as np
import matplotlib.pyplot as plt

# Parameters
F = 2e6         # Frequency of the signal (2 MHz)
Fs = 5e6        # Sampling frequency (5 MHz)
N = 50          # Number of points for the DFT

# Generate the discrete-time signal
t = np.arange(N) / Fs
x = np.cos(2 * np.pi * F * t)

# Apply a Blackman window
window = np.blackman(N)
y = x * window

# Compute the DFT using FFT
X = np.fft.fft(y)
frequencies = np.fft.fftfreq(N, 1/Fs)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 6))
plt.stem(frequencies, np.abs(X), basefmt=" ")
plt.title("50-Point DFT of x(t) with Blackman Window, F = 2 MHz and Fs = 5 MHz")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.xlim(-Fs/2, Fs/2)
plt.show()