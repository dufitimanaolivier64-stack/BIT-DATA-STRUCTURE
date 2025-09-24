import array

# -------------------------------
# Integers: Fares input
# -------------------------------
fares = [120, 150, 90, 200, 180]  # Example fares

total_fare = sum(fares)
average_fare = total_fare / len(fares)
min_fare = min(fares)
max_fare = max(fares)

print("\n---integers---")
print(f"Total fares collected: {total_fare}, Average fare: {average_fare:.2f}")
print(f"The lowest fare is {min_fare}, while the highest fare is {max_fare}")
