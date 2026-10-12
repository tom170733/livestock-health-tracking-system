"""
Livestock Health & Tracking System - Production Ready (DPG Standards)
Domain: Agriculture
"""

import json
import os


class Livestock:
    total_animals = 0

    def __init__(self, tag_id, species, age, breed, origin_info):
        self.tag_id = tag_id  # Unique ID
        self.species = species  # e.g., Cattle, Goat
        self.age = age  # Age string
        self.breed = breed

        self.origin_info = origin_info

        self.health_logs = {}  # Dictionary for health check logs
        Livestock.total_animals += 1

    def update_health_status(self, checkup_date, status):
        self.health_logs[checkup_date] = status
        print(f"[Success] Health log added for Tag ID {self.tag_id}.")

    def display_info(self):
        print(f"\n--- Livestock Profile: {self.tag_id} ---")
        print(f"Species & Breed: {self.species} ({self.breed})")
        print(f"Age: {self.age}")
        farm_loc, reg_date = self.origin_info  # Unpacking the tuple
        print(f"Origin Farm Location: {farm_loc}")
        print(f"Registration Date: {reg_date}")
        print(f"Health Logs: {self.health_logs if self.health_logs else 'No health logs recorded yet'}")

    @classmethod
    def get_total_animals(cls):
        return f"Total livestock monitored system-wide: {cls.total_animals}"

    @staticmethod
    def assess_health_risk(temperature_celsius):
        if temperature_celsius > 39.5:
            return "High Risk: Animal has a fever. Veterinary intervention required."
        elif temperature_celsius < 37.5:
            return "Warning: Body temperature is below normal range."
        else:
            return "Normal: Healthy temperature range."

    def to_dict(self):
        return {
            "tag_id": self.tag_id,
            "species": self.species,
            "age": self.age,
            "breed": self.breed,
            "origin_info": list(self.origin_info),  # Convert tuple to list for JSON serialization
            "health_logs": self.health_logs
        }


class FarmManager:
    def __init__(self, filename="farm_registry.json"):
        # Dictionary Data Structure (Task 2 requirement): Tag ID is the unique key
        self.livestock_dict = {}
        self.filename = filename
        self.load_data()

    def add_animal_record(self, animal):
        if animal.tag_id in self.livestock_dict:
            print(f"Error: Tag ID {animal.tag_id} already exists in the system.")
        else:
            self.livestock_dict[animal.tag_id] = animal
            print(f"Animal {animal.tag_id} successfully added to the registry.")
            self.save_data()

    def display_all_records(self):
        print("\n==========================================")
        print("      FARM LIVESTOCK DIRECTORY (DPG)      ")
        print("==========================================")
        if not self.livestock_dict:
            print("Registry is currently empty.")
            return

        for tag, obj in self.livestock_dict.items():
            loc, date = obj.origin_info
            print(f"ID Key: {tag} | Species: {obj.species} | Breed: {obj.breed} | Farm: {loc}")

    def find_animal(self, tag_id):
        return self.livestock_dict.get(tag_id)

    def save_data(self):
        data = {tag: obj.to_dict() for tag, obj in self.livestock_dict.items()}
        try:
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    for tag, d in data.items():
                        # Convert origin list back to tuple
                        origin_tuple = tuple(d["origin_info"])
                        animal = Livestock(d["tag_id"], d["species"], d["age"], d["breed"], origin_tuple)
                        animal.health_logs = d["health_logs"]
                        self.livestock_dict[tag] = animal
                        Livestock.total_animals += 1
                print(f"[System] Loaded existing records from {self.filename}")
            except Exception as e:
                print(f"Error loading data: {e}")


def main_menu():
    manager = FarmManager()

    while True:
        print("\n=== DIGITAL AGRICULTURE LIVESTOCK PORTAL ===")
        print("1. Register New Livestock")
        print("2. View All Livestock Records")
        print("3. View Specific Livestock Profile & Health Logs")
        print("4. Add Health Log / Vaccination")
        print("5. Assess Animal Temperature (Static Method)")
        print("6. View Total System Statistics (Class Method)")
        print("7. Exit Program")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            tag_id = input("Enter Unique Tag ID (e.g., TAG-301): ").strip()
            species = input("Enter Species (e.g., Cattle, Goat, Sheep): ").strip()
            age = input("Enter Age (e.g., 2 Years): ").strip()
            breed = input("Enter Breed: ").strip()
            farm = input("Enter Origin Farm Location: ").strip()
            date = input("Enter Registration Date (YYYY-MM-DD): ").strip()

            origin_tuple = (farm, date)

            new_animal = Livestock(tag_id, species, age, breed, origin_tuple)
            manager.add_animal_record(new_animal)

        elif choice == "2":
            manager.display_all_records()

        elif choice == "3":
            tag_id = input("Enter Tag ID to search: ").strip()
            animal = manager.find_animal(tag_id)
            if animal:
                animal.display_info()
            else:
                print(f"No record found with Tag ID: {tag_id}")

        elif choice == "4":
            tag_id = input("Enter Tag ID to update: ").strip()
            animal = manager.find_animal(tag_id)
            if animal:
                date = input("Enter Checkup Date (YYYY-MM-DD): ").strip()
                status = input("Enter Health Status / Vaccination Details: ").strip()
                animal.update_health_status(date, status)
                manager.save_data()
            else:
                print(f"No record found with Tag ID: {tag_id}")

        elif choice == "5":
            try:
                temp = float(input("Enter animal's body temperature in Celsius: "))
                assessment = Livestock.assess_health_risk(temp)
                print(f"\n[Assessment Result]: {assessment}")
            except ValueError:
                print("Invalid input. Please enter a valid number for temperature.")

        elif choice == "6":
            print("\n" + Livestock.get_total_animals())

        elif choice == "7":
            print("Exiting portal. Thank you for using the DPG Agricultural System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main_menu()