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
# value matching the breed string passed in.
def get_pets_by_breed(pet_shop, breed):
    matching_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            matching_pets.append(pet)
    return matching_pets

# Ex 8 
# Returns the pet object from pet_shop data structure, that has a 'name' 
# value matching the pet_name string passed in.
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# Ex 9 
# Looks for the pet object with a 'name' value matching the pet_name 
# string passed in and if present removes it.
def remove_pet_by_name(pet_shop, pet_name):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, pet_name))

# Ex 10 
# Adds the pet object passed in to the 'pets' list in the pet_shop
# data structure.
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# Ex 11
# Returns the value stored in 'cash' of the customer object passed in.
def get_customer_cash(customer):
    return customer["cash"]