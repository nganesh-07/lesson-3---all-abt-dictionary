trial = {"Fairlife": 5, "chocolate": 4, "milk": 5, "is": 1, "pretty": 2, "great": 5}

print("Original dictionary:", str(trial))

K = 5

response = 0

for key in trial:
    if trial[key] == K:
        response = response + 1

    
print("The frequency of the variable K is:", str(response))