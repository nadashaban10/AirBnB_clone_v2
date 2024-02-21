#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
print("Before save (State):", state.to_dict())
state.save()
print("After save (State):", state.to_dict())

# creation of a City
city = City(state_id=state.id, name="San Francisco")
print("Before save (City):", city.to_dict())
city.save()
print("After save (City):", city.to_dict())

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
print("Before save (User):", user.to_dict())
user.save()
print("After save (User):", user.to_dict())

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
print("Before save (Place 1):", place_1.to_dict())
place_1.save()
print("After save (Place 1):", place_1.to_dict())

place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
print("Before save (Place 2):", place_2.to_dict())
place_2.save()
print("After save (Place 2):", place_2.to_dict())

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
print("Before save (Amenity 1):", amenity_1.to_dict())
amenity_1.save()
print("After save (Amenity 1):", amenity_1.to_dict())

amenity_2 = Amenity(name="Cable")
print("Before save (Amenity 2):", amenity_2.to_dict())
amenity_2.save()
print("After save (Amenity 2):", amenity_2.to_dict())

amenity_3 = Amenity(name="Oven")
print("Before save (Amenity 3):", amenity_3.to_dict())
amenity_3.save()
print("After save (Amenity 3):", amenity_3.to_dict())

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")
