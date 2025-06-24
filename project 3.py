project = {"I": 3, "already": 6, "did": 3, "this": 4}

print("The original dictionary:", project)

K = 3

response = 0

for key in project:
    if project[key] == K:
        response = response + 1

print("The frequency of K in this dictionary is:", response)