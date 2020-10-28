import reverse_geocoder as rg
import pprint


# defined function to fetch and change the location to address
def locationToAddress(location):
    address = rg.search(location)
    # printing the results which is a list of ordered dictionary.
    pprint.pprint(address)


# main function
if __name__ == "__main__":
    # asking users for latitude and longitude
    lat = input("Enter Latitude\t")
    long = input("Enter Longitude\t")
    # combining latitude and longitude in location
    location = (lat, long)
    locationToAddress(location)
