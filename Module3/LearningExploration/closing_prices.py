# Last 30 days closing prices (fake data)
aapl_closing = [
    247.66, 245.27, 254.04, 258.06, 256.48, 256.69, 258.02,
    257.13, 255.45, 254.63, 254.43, 255.46, 256.87, 252.31,
    254.43, 256.08, 245.50, 237.88, 238.99, 238.15, 236.70,
    234.07, 230.03, 226.79, 234.35, 237.88, 239.69, 239.78,
    238.47, 229.72
]

num_items = len(aapl_closing)
total = 0.00
max = None
min = None
i = 0
while i < num_items:
	total += aapl_closing[i]
	if min is None or min > aapl_closing[i]:
		min = aapl_closing[i]
	if max is None or max < aapl_closing[i]:
		max = aapl_closing[i]
	i += 1

# Avg Stock Closing Price
print(f"Average price: ${(total / num_items):.2f}")

# Diff between first and last
print(f"Difference between last and first day: ${aapl_closing[len(aapl_closing) - 1] - aapl_closing[0]:.2f}")

# Min and Max
print(f"Minimum closing price was ${min}, and maximum closing price was ${max}")
