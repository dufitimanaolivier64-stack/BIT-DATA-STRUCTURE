fares = [120, 150, 90, 200, 180] 

total_fare = sum(fares)
average_fare = total_fare / len(fares)
min_fare = min(fares)
max_fare = max(fares)
threshold = 120
if average_fare > threshold and max_fare > 150:  
    print("Above Standard")
else:
    print("Below Standard")