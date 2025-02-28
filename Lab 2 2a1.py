import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Define signal parameters
f_signal = 200e6   # Signal frequency = 200 MHz
Fs = 400e6         # Sampling frequency = 400 MHz
N_bits = 6         # 6-bit quantizer resolution
num_periods = 30   # Number of periods to analyze

# Compute time vector
T_signal = num_periods / f_signal  # Total signal duration
t = np.arange(0, T_signal, 1/Fs)  # Time samples

# Generate full-scale sinewave (amplitude from -1V to +1V)
A = 1.0  # Full-scale amplitude
sinewave = A * np.sin(2 * np.pi * f_signal * t)

# Quantization step size
Q_levels = 2 ** N_bits  # Number of quantization levels
Q_step = (2 * A) / Q_levels  # Step size for quantization

# Apply quantization
sinewave_quantized = np.round(sinewave / Q_step) * Q_step

# Compute theoretical SNR (from quantization noise formula)
SNR_theoretical_dB = 6.02 * N_bits + 1.76

# Compute quantization noise
quantization_noise = sinewave - sinewave_quantized
P_signal = np.mean(sinewave ** 2)  # Signal power
P_noise = np.mean(quantization_noise ** 2)  # Noise power
SNR_computed_dB = 10 * np.log10(P_signal / P_noise)  # Computed SNR

# Compute Power Spectral Density (PSD)
f, PSD = welch(sinewave_quantized, fs=Fs, nperseg=4096, scaling='density')

# Plot PSD
plt.figure(figsize=(10, 6))
plt.semilogy(f / 1e6, PSD)  # Convert Hz to MHz for x-axis
plt.axvline(x=f_signal / 1e6, color='r', linestyle="--", label="Signal Frequency (200 MHz)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Spectral Density")
plt.title(f"PSD of 6-bit Quantized Signal (SNR: {SNR_computed_dB:.2f} dB)")
plt.legend()
plt.grid()
plt.show()

# Print results
print(f"Theoretical SNR for 6-bit quantization: {SNR_theoretical_dB:.2f} dB")
print(f"Computed SNR from quantization noise: {SNR_computed_dB:.2f} dB")
