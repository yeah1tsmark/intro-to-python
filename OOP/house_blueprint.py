class House:

    def __init__(self, location, owner, price, roof):
        self.location = location
        self.owner = owner
        self.price = price
        self.roof = roof


house_owner_1 = House("Westlands", "Precious", "6.5M", "98")
print(house_owner_1.location)
print(house_owner_1.owner)
print(house_owner_1.price)
print(house_owner_1.roof)

print("---------End of owner 1----------")

house_owner_2 = House("Ngara", "Kadish", "7M", "40")
print(house_owner_2.location)
print(house_owner_2.owner)
print(house_owner_2.price)
print(house_owner_2.roof)
