#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity """
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity

# Create State, City, and User
state = State(name="California")
state.save()
city = City(state_id=state.id, name="San Francisco")
city.save()
user = User(email="john@snow.com", password="johnpwd")
user.save()

# Create Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# Create Amenities
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# Link places with amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

# Commit changes
storage.save()

print("OK")

