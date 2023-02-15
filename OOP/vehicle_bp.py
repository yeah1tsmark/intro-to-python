class Vehicle():

    def __init__(self, model, price, colour, owner):
        self.model = model
        self.price = price
        self.colour = colour
        self.owner = owner


vehicle_owner_1 = Vehicle("X1", "2.5M", "White", "Elijah")
print(vehicle_owner_1.model)
print(vehicle_owner_1.price)
print(vehicle_owner_1.colour)
print(vehicle_owner_1.owner)

print("--------end of owner 1--------")


vehicle_owner_1 = Vehicle("X4", "4.5M", "Blue", "Elvis")
print(vehicle_owner_1.model)
print(vehicle_owner_1.price)
print(vehicle_owner_1.colour)
print(vehicle_owner_1.owner)

print("--------end of owner 2--------")


vehicle_owner_1 = Vehicle("X6", "8M", "Grey", "Mark")
print(vehicle_owner_1.model)
print(vehicle_owner_1.price)
print(vehicle_owner_1.colour)
print(vehicle_owner_1.owner)