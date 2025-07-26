#Step 1: Create a list of favourite cities
cities = ["Berlin", "Rome","Paris","London"]
#Step 2: Print the entire list
print("favorite cities:", cities[0])
print("last city:", cities[-1])
#Step 4: Add a new city
cities.append("Cape Town")
print("After adding a city:", cities)
#Step 5: remove a city
cities.remove("London")
print("After removing 'London':",cities)
#step 6: Sort the list alphabetically
cities.sort()
print("sorted cities:", cities)
##Step 7:Print the number of cities in the list
print("Number of cities:", len(cities))