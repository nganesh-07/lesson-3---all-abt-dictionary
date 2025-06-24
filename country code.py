countrycodes = {"India": "0091",
                "America": "0001",
                "Canada": "0051"}

print("The country code for India:")
print(countrycodes.get("India", "not found"))

print("The country code for Spain:")
print(countrycodes.get("Spain", "not found"))

