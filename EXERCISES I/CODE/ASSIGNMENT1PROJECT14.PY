import array

# Integers: Fares
fares = [500, 700, 1000, 1200, 800]

total = sum(fares)
average = total / len(fares)
minimum = min(fares)
maximum = max(fares)

# Strings: Formatted report

print("\n--- String Report ---")
print(f"Total fares collected: {total}, Average fare: {average:.2f}")
print(f"The lowest fare is {minimum}, while the highest fare is {maximum}")


# Booleans: Threshold check
threshold = 900
print("\n--- Boolean Check ---")
if average > threshold and maximum > 1000:   
    print("Status: Above Standard ")
else:
    print("Status: Below Standard ")

# Lists: Add, remove, sort
print("\n--- List Operations ---")
print("Original fares:", fares)

fares.append(1500)    
fares.remove(700)  
fares.sort()         

print("Updated fares:", fares)

# Arrays: Fixed-size subset
print("\n--- Array Operations ---")
fare_array = array.array('i', [500, 800, 1200])  # array of integers
array_sum = sum(fare_array)

print("Array fares:", fare_array.tolist())
print("Sum of array fares:", array_sum)
print("Compare with total from list:", total)

# Dictionaries: Records
print("\n--- Dictionary Operations ---")
transport_data = [
    {"id": 1, "name": "Bus A", "value": 500},
    {"id": 2, "name": "Bus B", "value": 1000},
    {"id": 3, "name": "Bus C", "value": 1200}
]

# Update one record
transport_data[1]["value"] = 1100   # Update Bus B

# Delete one record
transport_data = [record for record in transport_data if record["id"] != 1]

# Compute total values
dict_total = sum(record["value"] for record in transport_data)

print("Transport data after updates:", transport_data)
print("Total value (from dictionaries):", dict_total)
