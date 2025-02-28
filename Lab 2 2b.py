# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Define signal parameters
f_signal = 200e6   # Signal frequency = 200 MHz
Fs = 450e6         # Incommensurate sampling frequency = 450 MHz
N_bits = 6         # 6-bit quantizer resolution
num_periods = 30   # Number of periods to analyze

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

# Compute Power Spectral Density (PSD)
f, PSD = welch(sinewave_quantized, fs=Fs, nperseg=8192, scaling='density', window='hamming')

# Plot PSD
plt.figure(figsize=(10, 6))
plt.semilogy(f / 1e6, PSD)  # Convert Hz to MHz
plt.axvline(x=f_signal / 1e6, color='r', linestyle="--", label="Signal Frequency (200 MHz)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Spectral Density")
plt.title(f"PSD of 6-bit Quantized Signal (Incommensurate Sampling at 450 MHz)")
plt.legend()
plt.grid()
plt.show()

# Compute SNR from the PSD plot
# Signal power is calculated in a narrow band around the signal frequency (200 MHz)
signal_band = (f >= f_signal - 5e6) & (f <= f_signal + 5e6)  # ±5 MHz around the signal frequency
P_signal = np.sum(PSD[signal_band])  # Signal power in that band

# Total noise power is the remaining part of the PSD
P_noise = np.sum(PSD) - P_signal  # Noise power (total PSD minus signal power)

# Calculate SNR in dB
SNR_computed_dB = 10 * np.log10(P_signal / P_noise)  # Computed SNR

# Print computed SNR
print(f"Computed SNR from PSD: {SNR_computed_dB:.2f} dB")


