import array
fares = [120, 150, 90, 200, 180]  

total_fare = sum(fares)
average_fare = total_fare / len(fares)
min_fare = min(fares)
max_fare = max(fares)

fares_list = fares.copy()

fares_list.append(160)

fare_array = array.array('i', [120, 150, 90, 200, 180])
print("Sum using array:", sum(fare_array))
print("Sum using list:", sum(fares_list))