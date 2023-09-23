import uuid
import json

cars = []


def add_car(brand, model, hp, price):
    car = {
        "id": str(uuid.uuid4()),
        "brand": brand,
        "model": model,
        "hp": hp,
        "price": price
    }
    cars.append(car)
    return car


def categorize_by_hp():
    slow_cars = []
    fast_cars = []
    sport_cars = []

    for car in cars:
        if car["hp"] < 120:
            slow_cars.append(car)
        elif car["hp"] < 180:
            fast_cars.append(car)
        else:
            sport_cars.append(car)

    return slow_cars, fast_cars, sport_cars


def categorize_by_price():
    cheap_cars = []
    medium_cars = []
    expensive_cars = []

    for car in cars:
        if car["price"] < 1000:
            cheap_cars.append(car)
        elif car["price"] < 5000:
            medium_cars.append(car)
        else:
            expensive_cars.append(car)

    return cheap_cars, medium_cars, expensive_cars


def save_data_to_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main menu
while True:
    print("\n--- Car Management Menu ---")
    print("1. Add a Car")
    print("2. View All Cars")
    print("3. Categorize Cars by HP")
    print("4. Categorize Cars by Price")
    print("5. Save Data to Files")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        brand = input("Enter the brand: ")
        model = input("Enter the model: ")
        hp = int(input("Enter the horsepower: "))
        price = float(input("Enter the price: "))
        car = add_car(brand, model, hp, price)
        print(f"Car added with ID: {car['id']}")
    elif choice == "2":
        print("\n--- All Cars ---")
        for car in cars:
            print(f"ID: {car['id']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car['model']}")
            print(f"HP: {car['hp']}")
            print(f"Price: {car['price']}")
            print("-" * 30)
    elif choice == "3":
        slow_cars, fast_cars, sport_cars = categorize_by_hp()
        print("\n--- Slow Cars ---")
        for car in slow_cars:
            print(f"ID: {car['id']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car['model']}")
            print(f"HP: {car['hp']}")
            print(f"Price: {car['price']}")
            print("-" * 30)
        print("\n--- Fast Cars ---")
        for car in fast_cars:
            print(f"ID: {car['id']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car['model']}")
            print(f"HP: {car['hp']}")
            print(f"Price: {car['price']}")
            print("-" * 30)
        print("\n--- Sport Cars ---")
        for car in sport_cars:
            print(f"ID: {car['id']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car['model']}")
            print(f"HP: {car['hp']}")
            print(f"Price: {car['price']}")
            print("-" * 30)
    elif choice == "4":
        cheap_cars, medium_cars, expensive_cars = categorize_by_price()
        print("\n--- Cheap Cars ---")
        for car in cheap_cars:
            print(f"ID: {car['id']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car['model']}")
            print(f"HP: {car['hp']}")
            print(f"Price: {car['price']}")
            print("-" * 30)
        print("\n--- Medium Cars ---")
        for car in medium_cars:
            print(f"ID: {car['id']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car['model']}")
            print(f"HP: {car['hp']}")
            print(f"Price: {car['price']}")
            print("-" * 30)
        print("\n--- Expensive Cars ---")
        for car in expensive_cars:
            print(f"ID: {car['id']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car['model']}")
            print(f"HP: {car['hp']}")
            print(f"Price: {car['price']}")
            print("-" * 30)
    elif choice == "5":
        save_data_to_file("slow_cars.json", slow_cars)
        save_data_to_file("fast_cars.json", fast_cars)
        save_data_to_file("sport_cars.json", sport_cars)
        save_data_to_file("cheap_cars.json", cheap_cars)
        save_data_to_file("medium_cars.json", medium_cars)
        save_data_to_file("expensive_cars.json", expensive_cars)
        for brand in brands:
            brand_data = [car for car in cars if car["brand"] == brand]
            save_data_to_file(f"{brand.lower()}.json", brand_data)
        print("Data saved to files successfully.")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")