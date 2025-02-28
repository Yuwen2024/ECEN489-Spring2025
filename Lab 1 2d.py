# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 03:26:03 2025

@author: 13580
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

# Parameters
F1 = 300e6           # Signal frequency (Hz)
Fs = 800e6          # Sampling frequency (Hz)
T = 10 / F1         # Duration to cover 10 cycles
Ts = 1 / Fs         # Sampling interval

# Time vectors
t_cont = np.arange(0, T, 1e-10)
t_samples = np.arange(0, T, Ts)   # Sampled time points

# Generate the signal
x_cont = np.cos(2 * np.pi * F1 * t_cont)
x_samples = np.cos(2 * np.pi * F1 * t_samples)

# Reconstruct the signal using sinc interpolation
def sinc_interp(x, t, t_samples, Ts):
    y = np.zeros_like(t)
    for n in range(len(x)):
        y += x[n] * np.sinc((t - t_samples[n]) / Ts)
    return y

# Time vector for reconstruction
t_recon = t_cont
x_recon = sinc_interp(x_samples, t_recon, t_samples, Ts)

# Plot the signals
plt.figure(figsize=(10, 6))
plt.plot(t_cont * 1e6, x_cont, label='Original Signal', color='blue', linewidth=1)
plt.stem(t_samples * 1e6, x_samples, linefmt='green', markerfmt='go', basefmt='k', label='Samples')
plt.plot(t_recon * 1e6, x_recon, color='red', linestyle='--', label='Reconstructed Signal')

plt.xlabel('Time (µs)')
plt.ylabel('Amplitude')
plt.title('Sampling and Reconstruction of x1(t) = cos(2πF1t)')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()
