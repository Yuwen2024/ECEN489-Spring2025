import numpy as np
import matplotlib.pyplot as plt

# Given real DAC output voltages
real_outputs = np.array([-0.01, 0.105, 0.195, 0.28, 0.37, 0.48, 0.6, 0.75])

# Ideal LSB and ideal outputs
ideal_lsb = 0.1  # 100 mV
codes = np.arange(8)
ideal_outputs = codes * ideal_lsb

# Calculate DNL
dnl = (np.diff(real_outputs) / ideal_lsb) - 1

# Calculate INL
inl = (real_outputs - ideal_outputs) / ideal_lsb

# Calculate Offset Error
offset_error = (real_outputs[0] - ideal_outputs[0]) / ideal_lsb

# Calculate Full-Scale Error
full_scale_error = (real_outputs[-1] - ideal_outputs[-1]) / ideal_lsb

# Calculate End-Point Gain
actual_gain_v_per_code = (real_outputs[-1] - real_outputs[0]) / 7  # 7 steps
actual_gain_lsb_per_code = actual_gain_v_per_code / ideal_lsb      # Normalize to LSB/code

# Ideal gain is 1 LSB/code
ideal_gain_lsb_per_code = 1.0

# Gain Error
gain_error = actual_gain_lsb_per_code - ideal_gain_lsb_per_code

# Display results
print("Code | Real Output (V) | Ideal Output (V) | INL (LSB)")
print("--------------------------------------------------------")
for code in range(8):
    print(f" {code:3d} | {real_outputs[code]:14.3f} | {ideal_outputs[code]:14.3f} | {inl[code]:8.3f}")

print("\nCode | DNL (LSB)")
print("-----------------")
for code in range(7):
    print(f" {code:3d} | {dnl[code]:8.3f}")

print("\nOffset Error (in LSBs): {:.3f}".format(offset_error))
print("Full-Scale Error (in LSBs): {:.3f}".format(full_scale_error))
print("\nActual Gain (V/code): {:.6f}".format(actual_gain_v_per_code))
print("Actual Gain (LSB/code): {:.6f}".format(actual_gain_lsb_per_code))
print("Gain Error (LSB/code): {:.6f}".format(gain_error))

# Plot DNL and INL
fig, axs = plt.subplots(2, 1, figsize=(8, 8))

# Plot DNL
axs[0].bar(codes[:-1], dnl)
axs[0].set_title('Differential Nonlinearity (DNL)')
axs[0].set_xlabel('Code')
axs[0].set_ylabel('DNL (LSB)')
axs[0].grid(True, linestyle='--', alpha=0.7)

# Plot INL
axs[1].bar(codes, inl)
axs[1].set_title('Integral Nonlinearity (INL)')
axs[1].set_xlabel('Code')
axs[1].set_ylabel('INL (LSB)')
axs[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Find maximum DNL and INL
max_dnl = np.max(np.abs(dnl))
max_inl = np.max(np.abs(inl))

print("\nMaximum DNL (in LSBs): {:.3f}".format(max_dnl))
print("Maximum INL (in LSBs): {:.3f}".format(max_inl))

