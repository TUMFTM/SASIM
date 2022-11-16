from flask import Flask, request
from flask_cors import CORS

from AA_new.controllers.trip.TripController import TripController
from AA_new.entities_new.location.Location import Location
from AA_new.helpers.ApiHelper import ApiHelper

app = Flask(__name__)
CORS(app)


@app.route('/plattform', methods=['GET'])
def return_trip():
    api_helper = ApiHelper()

    input_start_lat = str(request.args['inputStartLat'])
    input_start_lon = str(request.args['inputStartLon'])
    start_location = Location(lat=float(input_start_lat), lon=float(input_start_lon))

    input_end_lat = str(request.args['inputEndLat'])
    input_end_lon = str(request.args['inputEndLon'])
    end_location = Location(lat=float(input_end_lat), lon=float(input_end_lon))

    input_mode = str(request.args['mode'])
    mode = api_helper.get_mode_from_input(input_mode)
    print(mode)

    input_trip_type = str(request.args['tripType'])
    trip_type = api_helper.get_trip_type_from_input(input_trip_type)

    trip_controller = TripController()
    trip = trip_controller.get_trip(
        start_location=start_location,
        end_location=end_location,
        mode=mode,
        trip_type=trip_type
    )

    list_segments = []

    segments = trip.segments

    # if trip consists of multiple segments, iterate over segments to return a list of segments in the rest-api response
    if (type(segments) == list):
        for j in range(len(trip.segments)):

            new_segment = trip.segments[j]
            segment_waypoints = []
            for k in range(len(new_segment.waypoints)):
                lat = new_segment.waypoints[k].lat
                lon = new_segment.waypoints[k].lon

                dict_waypoint = {
                    'lat': float(lat),
                    'lon': float(lon)
                }

                segment_waypoints.append(dict_waypoint)

            dict_segment = {

                'mode': new_segment.mode.value,
                'distance': new_segment.distance,
                'duration': new_segment.duration,
                'costs': {
                    'externalCosts': {
                        'all': new_segment.costs.external_costs.external_costs,
                        'air': new_segment.costs.external_costs.air,
                        'noise': new_segment.costs.external_costs.noise,
                        'climate': new_segment.costs.external_costs.climate,
                        'accidents': new_segment.costs.external_costs.accidents,
                        'space': new_segment.costs.external_costs.space,
                        'barrier': trip.costs.external_costs.barrier,
                        'congestion': trip.costs.external_costs.congestion
                    },
                    'internalCosts': {'all': new_segment.costs.internal_costs.internal_costs}
                },
                'waypoints': segment_waypoints

            }

            list_segments.append(dict_segment)

    else:
        new_segment = segments

        segment_waypoints = []
        for k in range(len(new_segment.waypoints)):
            lat = new_segment.waypoints[k].lat
            lon = new_segment.waypoints[k].lon

            dict_waypoint = {
                'lat': float(lat),
                'lon': float(lon)
            }

            segment_waypoints.append(dict_waypoint)

        dict_segment = {

            'mode': new_segment.mode.value,
            'distance': new_segment.distance,
            'duration': new_segment.duration,
            'costs': {
                'externalCosts': {
                    'all': new_segment.costs.external_costs.external_costs,
                    'air': new_segment.costs.external_costs.air,
                    'noise': new_segment.costs.external_costs.noise,
                    'climate': new_segment.costs.external_costs.climate,
                    'accidents': new_segment.costs.external_costs.accidents,
                    'space': new_segment.costs.external_costs.space,
                    'barrier': trip.costs.external_costs.barrier,
                    'congestion': trip.costs.external_costs.congestion
                },
                'internalCosts': {'all': new_segment.costs.internal_costs.internal_costs}
            },
            'waypoints': segment_waypoints

        }

        list_segments.append(dict_segment)

    dict_new_result = {
        'tripMode': mode.value,
        'distance': trip.distance,
        'duration': trip.duration,
        'costs': {
            'externalCosts': {
                'all': trip.costs.external_costs.external_costs,
                'air': trip.costs.external_costs.air,
                'noise': trip.costs.external_costs.noise,
                'climate': trip.costs.external_costs.climate,
                'accidents': trip.costs.external_costs.accidents,
                'space': trip.costs.external_costs.space,
                'barrier': trip.costs.external_costs.barrier,
                'congestion': trip.costs.external_costs.congestion
            },
            'internalCosts': {'all': trip.costs.internal_costs.internal_costs}

        },

        'segments': list_segments

    }

    return dict_new_result

if __name__ == "__main__":
    app.run()
