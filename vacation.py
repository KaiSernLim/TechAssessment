import sys
from geopy.geocoders import Nominatim
from geopy.distance import vincenty


cities = []
km = True if 'km' in sys.argv else False
units = 'kilometers' if km else 'miles'

if len(sys.argv) > 1 and sys.argv[1] != 'km':
    print('Reading txtfile: ' + sys.argv[1])
    cities = [city.rstrip('\n') for city in open(sys.argv[1])]
else:
    print('Enter one city per line in the form of "City, Country".')
    print('Press "Control + D" to finish.')
    cities = [city.rstrip('\n') for city in sys.stdin.readlines()]
    if len(cities) == 0:
        print('No cities entered.')
        sys.exit(0)
    elif len(cities) == 1:
        print ('Not enough cities entered for a trip.')
        sys.exit(0)

try:
    geolocator = Nominatim()
    locations = map(lambda city: geolocator.geocode(city), cities)
    points = map(lambda loc: (loc.latitude, loc.longitude), locations)
    distances = []
    n_cities = len(cities)

    for i in range(n_cities-1):
        if km:
            distances.append(vincenty(points[i], points[i+1]).km)
        else:
            distances.append(vincenty(points[i], points[i+1]).miles)
except:
    print('Error looking up the locations specified.')
    sys.exit(0)

print('Success! Your vacation itinerary is:')
for i in range(n_cities-1):
    print('\t{} -> {}: {:,.2f} {}'.format(cities[i], cities[i+1],
                                          distances[i], units))
print('Total distance covered in your trip: {:,.2f} {}'.format(sum(distances),
                                                               units))
