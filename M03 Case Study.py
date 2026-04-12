class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

vehicle_type = input("Enter the vehicle's type (car, truck, etc): ")
year = int(input("Enter the vehicle's year: "))
make = input("Enter the vehicle's make: ")
model = input("Enter the vehicle's model: ")
doors = int(input("Enter the number of doors (2 or 4): "))
roof = input("Enter the type of roof (solid or sunroof): ")

def display_vehicle_info(vehicle):
    print(f"Vehicle Type: {vehicle.vehicle_type}")
    print(f"Year: {vehicle.year}")
    print(f"Make: {vehicle.make}")
    print(f"Model: {vehicle.model}")
    print(f"Doors: {vehicle.doors}")
    print(f"Roof: {vehicle.roof}")

automobile = Automobile(vehicle_type, year, make, model, doors, roof)
display_vehicle_info(automobile)