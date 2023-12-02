import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        self.square_footage = square_footage
        self.spot_size = spot_size
        self.rows = self.calculate_rows()
        self.lot = ['empty' for _ in range(self.rows)]
        self.parked_cars = {}

    def calculate_rows(self):
        spot_area = self.spot_size[0] * self.spot_size[1]
        total_spots = self.square_footage / spot_area
        rows = int(total_spots)
        return rows

    def park_car(self, car, spot):
        if self.lot[spot] == 'empty':
            self.lot[spot] = car.license_plate
            self.parked_cars[car.license_plate] = spot
            print(f"Car {car.license_plate} parked successfully in spot {spot}")
            return True
        else:
            print(f"Car {car.license_plate} not parked successfully. Trying to find another spot...")
            return False

    def is_full(self):
        return 'empty' not in self.lot

    def map_parked_cars(self):
        return json.dumps(self.parked_cars, indent=2)

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def park(self, parking_lot):
        if not parking_lot.is_full():
            while True:
                spot = random.randint(0, parking_lot.rows-1)
                if parking_lot.park_car(self, spot):
                    break


def main():
    square_footage = 2000
    car_count = 20
    spot_size = (8, 12)

    parking_lot = ParkingLot(square_footage, spot_size)

    cars = [Car(str(random.randint(1000000, 9999999))) for _ in range(car_count)]

    for car in cars:
        car.park(parking_lot)
        if parking_lot.is_full():
            print("Parking lot is full. Exiting program.")
            break  # Exit the loop if the parking lot is full

    # Save the mapping of parked cars to a JSON file
    mapping_json = parking_lot.map_parked_cars()
    with open("parking_mapping.json", "w") as json_file:
        json_file.write(mapping_json)

if __name__ == "__main__":
    main()
