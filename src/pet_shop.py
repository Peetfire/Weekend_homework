# WRITE YOUR FUNCTIONS HERE

# Ex 1
# Returns the value of 'name' from the pet_shop from data structure
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Ex 2
# Returns the value of 'total_cash' from the pet_shop from data structure
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Ex 3
# Adds or subtracts the amount passed in to/from the value of 'total_cash' in the pet_shop from data structure
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

# ex 4
# Returns the value of 'pets_sold" from the pet_shop from data structure
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Ex 5
# Adds the amount passed in to 'pets_sold' in pet_shop data structure
def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount

# Ex 6
# Counts and returns the number of pets stored in pet_shop data structure
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# Ex 7
# Returns a list of pets from the pet_shop data structure with a 'breed' 
# value matching the passed breed string
def get_pets_by_breed(pet_shop, breed):
    matching_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            matching_pets.append(pet)
    return matching_pets