fares = [120, 150, 90, 200, 180]  

total_fare = sum(fares)
average_fare = total_fare / len(fares)
min_fare = min(fares)
max_fare = max(fares)

fares_list = fares.copy()
print("Before modification:", fares_list)


fares_list.append(160)

fares_list = [fare for fare in fares_list if fare >= 100]

fares_list.sort()

print("After modification:", fares_list)
