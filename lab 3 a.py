import numpy as np
import matplotlib.pyplot as plt


f = 1e9  # Input signal frequency in Hz (1 GHz)
fs = 10e9  # Sampling frequency in Hz (10 GHz)
A = 2  # Amplitude of input signal (2V)
Ts = 1/fs  # Sampling period
T = 1e-9  # Total time duration for visualization (1 ns)

# Time vectors
t_cont = np.linspace(0, T, 1000)  # High-resolution time for continuous signal
t_samples = np.arange(0, T, Ts)  # Sampling instants

# Input sinusoidal signal
x_cont = A * np.sin(2 * np.pi * f * t_cont)
x_samples = A * np.sin(2 * np.pi * f * t_samples)  # Sampled values

# Zero-Order Hold output
t_zoh = np.repeat(t_samples, 2)[1:]  # Extend each sample for ZOH effect
x_zoh = np.repeat(x_samples, 2)[:-1]  # Hold each sample until next

# First-Order Hold (FOH) output - Linear interpolation between samples
t_foh = np.repeat(t_samples, 2)[1:-1]  # Extend time values for FOH effect
x_foh = np.interp(t_foh, t_samples, x_samples)  # Linear interpolation

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(t_cont * 1e9, x_cont, 'b', label="Input Signal (Continuous)")
plt.step(t_zoh * 1e9, x_zoh, 'r', where='post', label="ZOH Output")
plt.plot(t_foh * 1e9, x_foh, 'g', linestyle='--', label="FOH Output")
plt.scatter(t_samples * 1e9, x_samples, color='black', marker='o', label="Sampled Points")
plt.xlabel("Time (ns)")
plt.ylabel("Amplitude (V)")
plt.title("ZOH and FOH Outputs for 1 GHz Input Signal with 10 GHz Sampling")
plt.legend()
plt.grid()
plt.show()

