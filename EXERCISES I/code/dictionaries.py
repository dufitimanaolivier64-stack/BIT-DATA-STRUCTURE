fare_records = [
    {"id": 1, "name": "Bus", "value": 120},
    {"id": 2, "name": "Taxi", "value": 150},
    {"id": 3, "name": "Train", "value": 200}
]


fare_records[1]["value"] = 170


fare_records.append({"id": 4, "name": "Metro", "value": 130})


fare_records = [rec for rec in fare_records if rec["name"] != "Train"]


total_value = sum(rec["value"] for rec in fare_records)

print("Final Records:", fare_records)
print("Total Value of All Records:", total_value)