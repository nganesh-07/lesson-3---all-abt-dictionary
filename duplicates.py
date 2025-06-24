studentdata = {"id1":
    {"name": ["Emma"],
     "class": ["7"],
     "subject": ["english, math, science"]
     },
     "id2":
     {"name": ["Blake"],
      "class": ["8"],
      "subject": ["english, math, sports med"]
      },
      "id3":
      {"name": ["Emma"],
       "class": ["7"],
       "subject": ["english, math, science"]
       },
       "id4":
       {"name": ["Olivia"],
        "class": ["7"],
        "subject": ["english, physics, science"]
        },
}

result = {}

for key,value in studentdata.items():
    if value not in result.values():
        result[key]=value

print(result)