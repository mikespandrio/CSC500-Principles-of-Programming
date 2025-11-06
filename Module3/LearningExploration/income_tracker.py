# Annual salaries for 20 working years since college graduation (fake data)
salaries = [
    30000.00,  # Year 1
    32500.00,  # Year 2 - small raise
    34000.00,  # Year 3
    33000.00,  # Year 4 - dip (job change, economy, etc.)
    35500.00,  # Year 5
    37000.00,  # Year 6
    36000.00,  # Year 7 - another dip
    39500.00,  # Year 8 - solid rebound
    42000.00,  # Year 9
    46500.00,  # Year 10 - promotion
    52000.00,  # Year 11
    59000.00,  # Year 12
    68000.00,  # Year 13
    78000.00,  # Year 14
    88000.00,  # Year 15
    102000.00, # Year 16
    118000.00, # Year 17
    136000.00, # Year 18
    158000.00, # Year 19
    180000.00  # Year 20
]
num_salaries = len(salaries)
total = 0.00
max = None
min = None
i = 0
while i < num_salaries:
	total += salaries[i]
	if min is None or min > salaries[i]:
		min = salaries[i]
	if max is None or max < salaries[i]:
		max = salaries[i]
	i += 1

# Average salary over 20 years (for all data in the array)
print(f"Average salary: ${(total / num_salaries):.2f}")

# Total earned (sum of all salaries)
print(f"Total earned: ${total:.2f}")

# Min and Max
print(f"Minimum salary was: ${min}, and maximum salary was: ${max}")
