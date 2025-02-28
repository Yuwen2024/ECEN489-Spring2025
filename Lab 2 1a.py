import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Define signal parameters
f_signal = 2e6   # Signal frequency = 2 MHz
A = 1.0          # Amplitude = 1V
Fs = 5e6         # Sampling frequency = 5 MHz
SNR_dB = 50      # Desired Signal-to-Noise Ratio in dB

# Time parameters
T_signal = 1e-6 
t_sampled = np.arange(0, T_signal, 1/Fs)  # Sampled time points

# Generate the clean sinewave
signal_sampled = A * np.sin(2 * np.pi * f_signal * t_sampled)

# Compute Signal Power
P_signal = np.mean(signal_sampled ** 2)

# Compute Gaussian Noise Variance
P_noise = P_signal / (10**(SNR_dB / 10))  # Noise power
sigma_squared = P_noise  # Variance of Gaussian noise
sigma = np.sqrt(sigma_squared)

# Generate Gaussian noise
gaussian_noise = sigma * np.random.randn(len(t_sampled))

# Add noise to the signal
signal_noisy = signal_sampled + gaussian_noise

# Compute FFT and Power Spectral Density (PSD)
N = len(signal_noisy)
fft_result = np.fft.fft(signal_noisy)  # Compute FFT
freqs = np.fft.fftfreq(N, 1/Fs)  # Frequency bins
PSD = (np.abs(fft_result)**2) / N  # Power Spectral Density

# Identify the index of the signal frequency in FFT
signal_bin = np.argmin(np.abs(freqs - f_signal))  # Closest frequency bin
signal_power_fft = np.sum(PSD[signal_bin-1:signal_bin+2])  # Sum around the signal bin

# Compute noise power from remaining spectrum bins
noise_bins = np.ones_like(PSD, dtype=bool)  # Mask for all bins
noise_bins[signal_bin-1:signal_bin+2] = False  # Exclude the signal frequency bins
noise_power_fft = np.mean(PSD[noise_bins])  # Average noise power

# Compute SNR from FFT
SNR_computed_dB = 10 * np.log10(signal_power_fft / noise_power_fft)

# Compute Variance of Uniform Noise
a = np.sqrt(3 * P_noise)  # Find max amplitude of uniform noise
uniform_variance = (a**2) / 3  # Variance of uniform noise

# Plot the Power Spectral Density (PSD)
plt.figure(figsize=(8, 4))
plt.plot(freqs[:N//2] / 1e6, PSD[:N//2], label="PSD of Noisy Signal", color='b')
plt.axvline(x=f_signal / 1e6, color='r', linestyle="--", label="Signal Frequency (2 MHz)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Spectral Density")
plt.title("Power Spectral Density of Noisy Signal")
plt.legend()
plt.grid()
plt.show()

# Print Results
print(f"Computed Gaussian Noise Variance: {sigma_squared:.4e}")
print(f"Computed SNR from FFT: {SNR_computed_dB:.2f} dB (Expected: {SNR_dB} dB)")
print(f"Variance of Equivalent Uniform Noise: {uniform_variance:.4e}")
