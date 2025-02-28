import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Define signal parameters
f_signal = 200e6   # 200 MHz sinewave
Fs = 400e6         # Sampling frequency = 400 MHz
N_bits = 6         # 6-bit quantizer
num_periods = 100  # Extend to 100 periods

# Compute time vector
T_signal = num_periods / f_signal  # Total signal duration
t = np.arange(0, T_signal, 1/Fs)  # Time samples

# Generate full-scale sinewave (amplitude ±1V)
A = 1.0  
sinewave = A * np.sin(2 * np.pi * f_signal * t)

# Quantization step size
Q_levels = 2 ** N_bits  # 64 levels
Q_step = (2 * A) / Q_levels  # Step size for quantization

# Apply 6-bit quantization
sinewave_quantized = np.round(sinewave / Q_step) * Q_step

# Compute theoretical SNR for 6-bit quantization
SNR_theoretical_dB = 6.02 * N_bits + 1.76

# Compute quantization noise
quantization_noise = sinewave - sinewave_quantized
P_signal = np.mean(sinewave ** 2)  # Signal power
P_noise = np.mean(quantization_noise ** 2)  # Noise power
SNR_computed_dB = 10 * np.log10(P_signal / P_noise)  # Computed SNR

# Compute Power Spectral Density (PSD)
f, PSD = welch(sinewave_quantized, fs=Fs, nperseg=8192, scaling='density')

# Plot PSD
plt.figure(figsize=(10, 6))
plt.semilogy(f / 1e6, PSD)  # Convert Hz to MHz
plt.axvline(x=f_signal / 1e6, color='r', linestyle="--", label="Signal Frequency (200 MHz)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Spectral Density")
plt.title(f"PSD of 6-bit Quantized Signal (100 Periods, SNR: {SNR_computed_dB:.2f} dB)")
plt.legend()
plt.grid()
plt.show()

# Print results
print(f"Theoretical SNR for 6-bit quantization: {SNR_theoretical_dB:.2f} dB")
print(f"Computed SNR from quantization noise (100 periods): {SNR_computed_dB:.2f} dB")

# Conclusions: 
    # 1. The quantization noise is periodic.
    # 2. For more periods, the SNR is more stable