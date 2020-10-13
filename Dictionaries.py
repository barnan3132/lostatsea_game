# Class: Computer Science 30
# Quint: 1
# Date created: 20/09/28
# Date last modified: 20/10/01
# Name: Barnan Adhikari
# Description: Nested Dictionary of inventories

# Character Profile

character = {
    "Your name is Babaas smith": {
        "Age": "27",
        "From": "Mississauga, Ontario",
        "Fact": "Your one wish is to see the Blue Jays win the world series",
    },
}

# Printing Profile

for person, data in character.items():
    print(f"\n{person.capitalize()}:")
    for k, v in data.items():
        print(f"- {k}: {v}")

# Healing inventory and header

print(f'\n\033[4mThis is your healing inventory\033[0m')
inventory_1 = {
    "painkillers": {
        "Replenishes": "100 HP",
        "Uses": 1,
        "fact": "Numbs all the pain from your body",
    },
    "bandages": {
        "Replenishes": "20 HP",
        "Uses": 5,
        "fact": "Covers wounds, scratches and scars",
    },
    "cough syrup": {
        "Replenishes": "40 HP",
        "Uses": 2,
        "fact": "Supresses your nasty coughs ",
    }
}

# Printing inventory

for item_1, data in inventory_1.items():
    print(f"\n{item_1.capitalize()}:")
    for k, v in data.items():
        print(f"- {k}: {v}")
print()

# Tools inventory and header

print(f'\n\033[4mThis is your tools inventory\033[0m')
inventory_2 = {
    "knife": {
        "Use": "Cut your paracord or attack friendlies or enemies",
        "Uses": 1,
        "fact": "You found this on the Captains body",
    },
    "paracord": {
        "Use": "Ties objects to your raft or vice versa",
        "Uses": 5,
        "fact": "You found this in the galley",
    },
    "lighter": {
        "Use": "Creates fire",
        "Uses": 2,
        "fact": "You brought this with you",
    },
    "bucket": {
        "Use": "Holds freshwater",
        "Uses": 2,
        "fact": "This was keeping you afloat moments after the crash",
    }
}

# Printing inventory

for tools, data in inventory_2.items():
    print(f"\n{tools.capitalize()}:")
    for k, v in data.items():
        print(f"- {k}: {v}")
print()

# Food inventory and header

print(f'\n\033[4mThis is your food inventory\033[0m')
inventory_3 = {
    "1L of freshwater": {
        "Use": "Thirst gets quenched",
        "Uses": 2,
        "fact": "Taste like Dasani",
    },
    "triscuits": {
        "Use": "replenishes food by 3",
        "Uses": 12,
        "fact": "Sharp edges",
    },
    "8oz steak": {
        "Use": "replenishes food by 75",
        "Uses": 1,
        "fact": "mmmm Tasty!",
    },
    "cheese": {
        "Use": "replenishes food by 40",
        "Uses": 3,
        "fact": "Gouda! ",
    }
}

# Printing inventory

for food, data in inventory_3.items():
    print(f"\n{food.capitalize()}:")
    for k, v in data.items():
        print(f"- {k}: {v}")
print()

# Location profile and header

print(f'\n\033[4mYour Locations\033[0m')
locations = {
    "Island": {
        "Location": "South of raft",
        "Fact": "The island contains a treasure chest!",
    },
     "raft": {
        "From": "The original shipwreck",
        "Fact": "The raft could fit up to five people",
    },
}

# Printing Location profiles

for area, data in locations.items():
    print(f"\n{area.capitalize()}:")
    for k, v in data.items():
        print(f"- {k}: {v}")
