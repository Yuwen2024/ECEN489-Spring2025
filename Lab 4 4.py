import numpy as np
import matplotlib.pyplot as plt


histogram = np.array([43, 115, 85, 101, 122, 170, 75, 146, 125, 60, 95, 95, 115, 40, 120, 242])

# Total hits and ideal hits per code
total_hits = np.sum(histogram)
num_codes = 16  # 4-bit ADC
ideal_hits = total_hits / num_codes

# Calculate DNL
dnl = (histogram / ideal_hits) - 1

# Calculate INL
inl = np.cumsum(dnl)

# Peak DNL and INL
peak_dnl = np.max(np.abs(dnl))
peak_inl = np.max(np.abs(inl))

# Monotonicity check
is_monotonic = np.all(dnl > -1)

# Print results
print("Code | Histogram | DNL (LSB) | INL (LSB)")
print("------------------------------------------")
for code in range(num_codes):
    print(f"{code:4d} | {histogram[code]:9d} | {dnl[code]:8.3f} | {inl[code]:8.3f}")

print("\nPeak DNL (LSB): {:.3f}".format(peak_dnl))
print("Peak INL (LSB): {:.3f}".format(peak_inl))

if is_monotonic:
    print("The ADC is monotonic.")
else:
    print("The ADC is NOT monotonic.")

# Plot DNL and INL
fig, axs = plt.subplots(2, 1, figsize=(8, 8))

# DNL plot
axs[0].bar(np.arange(num_codes), dnl)
axs[0].set_title('Differential Nonlinearity (DNL)')
axs[0].set_xlabel('Code')
axs[0].set_ylabel('DNL (LSB)')
axs[0].grid(True, linestyle='--', alpha=0.7)

# INL plot
axs[1].bar(np.arange(num_codes), inl)
axs[1].set_title('Integral Nonlinearity (INL)')
axs[1].set_xlabel('Code')
axs[1].set_ylabel('INL (LSB)')
axs[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

