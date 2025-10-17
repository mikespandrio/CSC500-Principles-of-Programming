# Son’s heights from birth to age 10 (fake data)
sons_heights = [
    19.7,   # Birth length (newborn)
    29.8,   # Age 1
    34.5,   # Age 2
    37.8,   # Age 3
    40.2,   # Age 4
    43.0,   # Age 5
    45.4,   # Age 6
    48.0,   # Age 7
    50.6,   # Age 8
    52.9,   # Age 9
    55.1,   # Age 10
]

# Calculate inches grown between first and last entry
inches_grown = sons_heights[len(sons_heights) - 1] - sons_heights[0]
print(f"Jr has grown {inches_grown:.2f} inches so far.")

# Find Jr’s height at 3 and 7 years old
print(f"Jr was {sons_heights[3]} inches tall at 3 years old, and {sons_heights[7]} inches tall at 7 years old")
