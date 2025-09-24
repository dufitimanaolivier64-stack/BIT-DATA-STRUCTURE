fares = [120, 150, 90, 200, 180]  # Example fares

total_fare = sum(fares)
average_fare = total_fare / len(fares)
min_fare = min(fares)
max_fare = max(fares)

report = f"Total Fare Collected: {total_fare}, Average Fare: {average_fare:.2f}"
summary = f"Minimum Fare: {min_fare}, Maximum Fare: {max_fare}"
print(report)
print(summary)