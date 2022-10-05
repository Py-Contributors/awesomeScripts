# pip install geocoder
import geocoder

print("------------------ locate addresses ------------------")

print("1. Get co-ordinates of an address")
print("2. Get address (in words) of co-ordinates")
print("-------------------------------------------------------")

user_choice = int(input("Select (1/2): "))

print("-------------------------------------------------------")

if user_choice == 1:
    user_address = input("Enter the address (in words): ")
    coordinates = geocoder.arcgis(user_address)
    geo = geocoder.arcgis(user_address)
    print("-------------------------------------------------------")
    print(f"[Latitude, Longitude]: {geo.latlng}")

elif user_choice == 2:
    user_latitude = float(input("Enter the latitude: "))
    user_longitude = float(input("Enter the longitude: "))

    output_address = geocoder.arcgis([user_latitude, user_longitude], method="reverse")
    output_address = output_address.raw['address']['LongLabel']

    print("-------------------------------------------------------")
    print(f"The address is '{output_address}'")


# Made with ♥ by https://github.com/NishantPacharne