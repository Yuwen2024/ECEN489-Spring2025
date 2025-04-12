import numpy as np
import matplotlib.pyplot as plt


rms_input_voltage = 0.2  # 200 mV in volts
adc_bits = 12
full_scale_vpp = 1.2  # 1.2 V peak-to-peak

# Full scale peak voltage
full_scale_vp = full_scale_vpp / 2
full_scale_rms = full_scale_vp / np.sqrt(2)

# Ideal SNR formula for an N-bit ADC (in dB)
ideal_snr = 6.02 * adc_bits + 1.76


# SNR_actual = ideal_snr + 20*log10(Vin_rms / Vfs_rms)
snr_actual = ideal_snr + 20 * np.log10(rms_input_voltage / full_scale_rms)

# Plotting
bit_depths = np.arange(1, 17)
ideal_snr_values = 6.02 * bit_depths + 1.76
actual_snr_values = ideal_snr_values + 20 * np.log10(rms_input_voltage / (full_scale_vpp / 2 / np.sqrt(2)))

plt.figure(figsize=(10, 6))
plt.plot(bit_depths, ideal_snr_values, label="Ideal SNR", marker='o')
plt.plot(bit_depths, actual_snr_values, label="Actual SNR (Vin = 0.2V RMS)", marker='x', linestyle='--')
plt.axvline(adc_bits, color='red', linestyle=':', label=f'{adc_bits}-bit ADC')
plt.title("SNR vs ADC Resolution")
plt.xlabel("ADC Bit Depth")
plt.ylabel("SNR (dB)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

snr_actual

signal_vpp = 1.2  # Full range peak-to-peak
signal_vp = signal_vpp / 2
signal_rms = signal_vp / np.sqrt(2)

# Noise standard deviation
noise_std = 0.5  # in volts
noise_power = noise_std ** 2
signal_power = signal_rms ** 2

# Input SNR (before ADC) in dB
input_snr = 10 * np.log10(signal_power / noise_power)

# ADC quantization noise power
# Quantization step size
q = signal_vpp / (2 ** adc_bits)
quantization_noise_power = (q ** 2) / 12

# Total noise at ADC output = Gaussian noise + quantization noise
total_noise_power = noise_power + quantization_noise_power
adc_output_snr = 10 * np.log10(signal_power / total_noise_power)

input_snr, adc_output_snr
