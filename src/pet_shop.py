# WRITE YOUR FUNCTIONS HERE

# Returns the value of 'name' from the pet shop from data structure
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Returns the value of 'total_cash' from the pet shop from data structure
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Adds or subtracts the amount passed in to/from the value of 'total_cash'
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

# Returns the value of 'pets_sold" from the pet shop from data structure
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]