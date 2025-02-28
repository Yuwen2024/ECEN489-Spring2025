import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

# Define signal parameters
f_signal = 2e6   # Signal frequency = 2 MHz
A = 1.0          # Amplitude = 1V
Fs = 5e6         # Sampling frequency = 5 MHz
SNR_dB = 50      # Desired Signal-to-Noise Ratio in dB

# Time parameters
T_signal = 1e-6  
t_sampled = np.arange(0, T_signal, 1/Fs)  # Sampled time points
N = len(t_sampled)  # Number of samples

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

# Define window types
windows = {
    "Rectangular (No Window)": np.ones(N),  # Equivalent to no windowing
    "Hanning": get_window("hann", N),
    "Hamming": get_window("hamming", N),
    "Blackman": get_window("blackman", N)
}

# Compute and plot the FFT for each window
plt.figure(figsize=(10, 6))

for name, window in windows.items():
    # Apply window to the noisy signal
    signal_windowed = signal_noisy * window

    # Compute FFT
    fft_result = np.fft.fft(signal_windowed)
    freqs = np.fft.fftfreq(N, 1/Fs)  # Frequency bins
    PSD = (np.abs(fft_result)**2) / N  # Power Spectral Density

    # Correct for window power loss
    window_power_correction = np.mean(window**2)  # Normalization factor
    PSD_corrected = PSD / window_power_correction  # Normalize PSD

    # Identify the signal peak in FFT
    signal_bin = np.argmin(np.abs(freqs - f_signal))  # Find closest frequency bin
    signal_power_fft = np.sum(PSD_corrected[signal_bin-1:signal_bin+2])  # Sum around peak

    # Compute noise power (excluding signal bins)
    noise_bins = np.ones_like(PSD_corrected, dtype=bool)
    noise_bins[signal_bin-1:signal_bin+2] = False  # Exclude signal bins
    noise_power_fft = np.mean(PSD_corrected[noise_bins])  # Average noise power

    # Compute SNR
    SNR_computed_dB = 10 * np.log10(signal_power_fft / noise_power_fft)

    # Plot PSD
    plt.plot(freqs[:N//2] / 1e6, PSD_corrected[:N//2], label=f"{name} (SNR: {SNR_computed_dB:.2f} dB)")

plt.axvline(x=f_signal / 1e6, color='r', linestyle="--", label="Signal Frequency (2 MHz)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Spectral Density")
plt.title("Power Spectral Density of Noisy Signal with Different Windows")
plt.legend()
plt.grid()
plt.show()

# Conclusion to answer Questions
# Hamming Window has more Leakage than Hanning Windwo and
# it has better frequency localization than Blackman window