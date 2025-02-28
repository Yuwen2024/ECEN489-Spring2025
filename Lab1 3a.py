# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:05:43 2025

@author: 13580
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
F = 2e6  # Frequency of the signal in Hz
Fs = 5e6  # Sampling frequency in Hz
N = 50   # Number of samples

t = np.arange(N) / Fs  # Time vector
x = np.cos(2 * np.pi * F * t)  # Generate the signal

# Compute the DFT using FFT
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(N, 1/Fs)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 6))
plt.stem(frequencies, np.abs(X), basefmt=" ", use_line_collection=True)
plt.title('50-Point DFT of x(t) = cos(2πFt) with F = 2 MHz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
