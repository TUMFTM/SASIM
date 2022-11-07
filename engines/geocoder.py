from geopy.geocoders import Nominatim
import time
import csv

def get_location(address):
    """

    :param adress: String as an Input (example: Arcisstraße 21, München)
    :return: location point by address
    """
    start = time.time()

    locator = Nominatim(user_agent="gustav")
    location = locator.geocode(address)

    end = time.time()
    print("geocoder api: " + str(end - start))

    return location

def input_address(locator):
    while True:
        start_location = locator.geocode(str(input("Von wo willst du starten?")))

        if (start_location != None):
            break
        else:
            print("Adresse wurde nicht gefunden. Bitte gib eine andere Adresse ein")

    while True:
        destination_location = locator.geocode(str(input("Wohin willst du?")))

        if (destination_location != None):
            break
        else:
            print("Adresse wurde nicht gefunden. Bitte gib eine andere Adresse ein")

    return start_location, destination_location
