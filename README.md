# SASIM Web App

### a fullcost based multimodal route planner

The VMRP Web App is a routeplanner for the city of Munich, that enables to plan and compare routes with many different
modes (private, sharing and public transport). It is part of the research project SASIM of M-Cube (Munich Cluster for
the Future of Mobility in Metropolitan Regions). The goal of this project is, to give users a better understanding of
the external effects of their mobility behaviour.

## Features

- plan multiple routes for a start- and destination address and a mobility mode
- compare different routes in a result list
- MobiScore: the MobiScore is a score developed by M-Cube, to evaluate the sustainability of a mobility choice for a
  particular route. The MobiScore calculation is based on the distance and the external costs of a route.
- compare costs, distance and travel time in a bar chart
- get further information on the external costs of a particular route

## Use of Web-App (coming soon ...)

The VMRP Web-App is already deployed and can be accessed at http://www.sasim.mcube-cluster.de. It is to note, that the
current version 0.2 is a beta-version, and bugs can occur.

## Get started for Developers

### Run Project locally

Before the project can be run, make sure following steps are done:

1. clone project to your local repository

2. add your own API keys to the file config/api_keys.py. Currently you'll only need a TIER API key and add it as a
   string by replacing following attribute:

```
    tierkey = '[Own TIER API-Key]'
```

3. Make sure, your have the right root directory selected, by changing constant ROOT_DIR in config/definitions to
   VARIANT 2 by commenting other variants and uncommenting VARIANT 2. VARIANT 1 for e.g. is needed if you want to build
   an .exe
   file

4. The application server can be then deployed locally by runing following command in the root of the flask_app project

``` console
    python wsgi.py 
```

### REST-API

The Backend REST-Api can be accessed at localhost:8000/plattform/ with the following params:

- inputStartAddress:
  a Munich address as type string in format "[Streetname] [#], München"
- inputEndAddress:
  a Munich address as type string in format "[Streetname] [#], München"
- tripMode: a valid tripMode

following modes can be used as the param tripMode:

- "CAR" : trip with a private gasoline car
- "ECAR" : trip with a private electric car
- "MOPED" : trip with a private moped
- "EMOPED" : trip with a private electric moped
- "BICYCLE" : trip with a private bicycle
- "EBICYCLE" : trip with a private electric bicycle
- "EMMY: trip using the closest Emmy sharing electric moped and walking to the vehicle
- "TIER" : trip using the closest TIER sharing e-scooter and walking to the vehicle
- (DB API deprecated - not used in frontend) "CAB": trip using the closest Call a Bike sharing bicycle and walking to
  the vehicle
- (DB API deprecated - not used in frontend) "FLINKSTER": trip using the closest Flinkster sharing car and walking to
  the vehicle
- "SHARENOW" : trip using the closest Sharenow sharing car and walking to the vehicle
- "PT" : trip using public transport and walking to the first station
- "INTERMODAL_PT_BIKE" : trip using public transport and using the bicycle to get to the first station

For accessing the Web-App Frontend, use localhost:5000/web/ (ideally in chrome web browser)

### Structure of Backend

The backend uses an MVC Architecture. The Model is specified in the directories model/entities and model/enums.
Furthermode multiple controller classes are used for the core functionalities, which are called by the TripController
class, to create a new trip. To plan a new route create an object of the class TripController and execute the method
get_trip() with the input variables start_location and end_location of the internal class Location, and trip_mode of the
internal class TripMode.

#### example: creating a trip

```python
trip_controller = TripController()

start_location = Location(lat=48.1663834, lon=11.5748712)
end_location = Location(lat=48.1377949, lon=48.1377949)
trip_mode = TripMode.BICYCLE

trip = trip_controller.get_trip(start_location, end_location, trip_mode)
```

#### pseudo database

All munich and mode specific variables from research are stored in the directory db in csv files. If the values in
current research or pricing plans of the mobility sharing services change, these csv. files must be updated.

### Frontend

The frontend was developed using the Dart and SDK Flutter.

#### integration into flask web app

To integrate the frontend into the flask application server, a Flutter build file has to be created by using the build
command

```console
  flutter build web
```

and then the content of build/web folder has to be added to the flask_app/templates folder. IMPORTANT: in
flask_app/templates/index.html the line

```html
    <base href="/">
```

has to be replaced by

```
  <base href="/web/">
```

#### running flutter web server locally

to run to flutter web server locally use the command

```console
  flutter run
```

by default the remote backend server deployed at the Institute of Automotive Technology TUM is used. To use your own
local backend server change the url property in
flutter_frontend/multimodal_routeplanner/lib/04_infrastructure/datasources/route_remote_datasource.dart

### Deploy using docker container

The Web-App can be easily deployed using a docker-container. For own deployment the server_name attribute in
nginx/project.config has to be replaced by personal url.

## Contributors

### Research

External Costs for Munich:
Schröder, Kirn et al. - Ending the myth of mobility at zero costs: An external cost analysis
https://www.sciencedirect.com/science/article/pii/S0739885922000713?via%3Dihub

### Development

flask backend-server and flutter frontend developed by Gusztáv Ottrubay

(gusztav.ottrubay@proton.me | https://github.com/gusti-ott)

### Open Source Software

#### Maps:

OpenStreetMap
https://www.openstreetmap.org/#map=7/47.714/13.349

#### Geocoding:

Nominatim with OpenStreetMap data
https://nominatim.org/

### Open APIs

#### Muenchen API

routing car, bicycle, walk and public transport paths

#### MVV API

routing public transport paths and fetching price data

#### EMMY API

fetching location of EMMY vehicles

#### TIER API

fetching location of TIER vehicles

#### SHARENOW API

fetching location of SHARENOW vehicles

## Support

contact daniel.schroeder@tum.de for support

## Licence

MIT Public Licence
