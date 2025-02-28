import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Define signal parameters
f_signal = 200e6   # Signal frequency = 200 MHz
Fs = 400e6         # Sampling frequency = 400 MHz (Nyquist rate)
N_bits = 12        # 12-bit quantizer resolution
num_periods = 30   # Number of periods to analyze

# Compute time vector: T_signal = num_periods / f_signal
T_signal = num_periods / f_signal  # Total signal duration in seconds
t = np.arange(0, T_signal, 1/Fs)  # Time samples based on sampling rate

# Generate full-scale sinewave (amplitude ±1V)
A = 1.0  # Full scale amplitude
sinewave = A * np.sin(2 * np.pi * f_signal * t)

# Quantization step size: 12-bit resolution gives 4096 levels
Q_levels = 2 ** N_bits  # 4096 levels
Q_step = (2 * A) / Q_levels  # Step size for quantization

# Apply 12-bit quantization to the sinewave
sinewave_quantized = np.round(sinewave / Q_step) * Q_step

# Compute Power Spectral Density (PSD) using Hanning window
f, PSD = welch(sinewave_quantized, fs=Fs, nperseg=8192, scaling='density', window='hann')

# Plot PSD
plt.figure(figsize=(10, 6))
plt.semilogy(f / 1e6, PSD)  # Convert Hz to MHz for better readability
plt.axvline(x=f_signal / 1e6, color='r', linestyle="--", label="Signal Frequency (200 MHz)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Spectral Density")
plt.title(f"PSD of 12-bit Quantized Signal (Sampled at 400 MHz) with Hanning Window")
plt.legend()
plt.grid(True)
plt.show()


