# VMRP Web App
### a fullcost based multimodal route planner

The VMRP Web App is a routeplanner for the city of Munich, that enables to plan and compare routes with many different modes (private, sharing and public transport). It is part of the research project SASIM of M-Cube (Munich Cluster for the Future of Mobility in Metropolitan Regions). The goal of this project is, to give users a better understanding of the external effects of their mobility behaviour.

## Features:
- plan multiple routes for a start- and destination address and a mobility mode
- compare different routes in a result list 
- MobiScore: the MobiScore is a score developed by M-Cube, to evaluate the sustainability of a mobility choice for a particular route. The MobiScore calculation is based on the distance and the external costs of a route.
- compare costs, distance and travel time in a bar chart
- (coming soon ...) get further information on the external costs of a particular route 

## Use of Web-App (coming soon ...):
The VMRP Web-App is already deployed and can be accessed at sasim.mcube-cluster.de. It is to note, that the current version 0.2 is a beta-version, and bugs can occur.

## Get started for Developers:

### Run Project
Before the project can be run, make sure following steps are done:
1. clone project to your local repository
2. add your own file api_keys.py to the config folder. Then add your TIER and DB Api keys in the following format:

```
dbkey = '[Own DB API-Key]'
tierkey = '[Own TIER API-Key]'
```

3. change constant ROOT_DIR in config/definitions to variant 2 by commenting VARIANT 1 and uncommenting VARIANT 2. VARIANT 1 is needed if you want to build an .exe file

3. run a local instance of OTP2 (Open Trip Planner) on the local device of the developer (find tutorial here --> https://docs.opentripplanner.org/en/latest/Basic-Tutorial/)

4. The application server can be then deployed locally (--> run app.py). 

### REST-API
The Backend REST-Api can be accessed at localhost:5000/plattform/ with the following params:
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
- "CAB": trip using the closest Call a Bike sharing bicycle and walking to the vehicle
- "FLINKSTER": trip using the closest Flinkster sharing car and walking to the vehicle
- "SHARENOW" : trip using the closest Sharenow sharing car and walking to the vehicle
- "PT" : trip using public transport and walking to the first station
- "INTERMODAL_PT_BIKE" : trip using public transport and using the bicycle to get to the first station

For accessing the Web-App Frontend, use localhost:5000/web/ (ideally in chrome web browser)

### Structure of Backend
The backend uses a MVC Architecture. The Model is specified in the directories model/entities and model/enums. Furthermode multiple controller classes are used for the core functionalities, which are called by the TripController class, to create a new trip. To plan a new route create an object of the class TripController and execute the method get_trip() with the input variables start_location and end_location of the internal class Location, and trip_mode of the internal class TripMode.

an example for creating a trip:
```python
trip_controller = TripController()

start_location = Location(lat=48.1663834, lon=11.5748712)
end_location = Location(lat=48.1377949, lon=48.1377949)
trip_mode = TripMode.BICYCLE

trip = trip_controller.get_trip(start_location, end_location, trip_mode)
```

#### pseudo database
All munich and mode specific variables from research are stored in the directory db in csv files. If the values in current research or pricing plans of the mobility sharing services change, these csv. files must be updated.

## Support:
contact gusztav.ottrubay@tum.de for support

## Licence:
MIT Public Licence
