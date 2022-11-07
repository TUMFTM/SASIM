from flask import Flask, request
from flask_cors import CORS
import csv

from rest_api_controller import get_single_trip_from_address

app = Flask(__name__)
CORS(app)

# get request to plan a route with one option and a start- and end-location
@app.route('/trip_with_segments', methods=['GET'])
def return_route_segments():
    input_start = str(request.args['inputStart'])
    input_end = str(request.args['inputEnd'])

    # mode is type String
    # find available modes in API Documentation, for example use "CAR", "BICYCLE", "MVG" or "TIER"
    input_mode = str(request.args['mode'])

    trip = get_single_trip_from_address(input_start, input_end, input_mode)

    list_segments = []

    segments = trip.get_segments()

    # if trip consists of multiple segments, iterate over segments to return a list of segments in the rest-api response
    if (type(segments) == list):
        for j in range(len(trip.get_segments())):

            new_segment = trip.get_segments()[j]
            segment_waypoints = []
            for k in range(len(new_segment.get_waypoints())):
                lat = new_segment.get_waypoints()[k].get_latitude()
                lon = new_segment.get_waypoints()[k].get_longitude()

                dict_waypoint = {
                    'lat': float(lat),
                    'lon': float(lon)
                }

                segment_waypoints.append(dict_waypoint)

            dict_segment = {

                'mode': new_segment.get_vehicle().get_vehicle_type().value,
                'distance': new_segment.get_distance(),
                'duration': new_segment.get_duration(),
                'costs': {
                    'externalCosts': {
                        'all': new_segment.get_external_costs().all,
                        'air': new_segment.get_external_costs().air_pollution,
                        'noise': new_segment.get_external_costs().noise_pollution,
                        'climate': new_segment.get_external_costs().climate,
                        'accidents': new_segment.get_external_costs().accidents,
                        'space': new_segment.get_external_costs().space,
                        'barrier': trip.get_external_costs().barrier,
                        'congestion': trip.get_external_costs().congestion
                    },
                    'internalCosts': {'all': new_segment.get_internal_costs().value}
                },
                'waypoints': segment_waypoints

            }

            list_segments.append(dict_segment)

    else:
        new_segment = segments

        segment_waypoints = []
        for k in range(len(new_segment.get_waypoints())):
            lat = new_segment.get_waypoints()[k].get_latitude()
            lon = new_segment.get_waypoints()[k].get_longitude()

            dict_waypoint = {
                'lat': float(lat),
                'lon': float(lon)
            }

            segment_waypoints.append(dict_waypoint)

        dict_segment = {

            'mode': new_segment.get_vehicle().get_vehicle_type().value,
            'distance': new_segment.get_distance(),
            'duration': new_segment.get_duration(),
            'costs': {
                'externalCosts': {
                    'all': new_segment.get_external_costs().all,
                    'air': new_segment.get_external_costs().air_pollution,
                    'noise': new_segment.get_external_costs().noise_pollution,
                    'climate': new_segment.get_external_costs().climate,
                    'accidents': new_segment.get_external_costs().accidents,
                    'space': new_segment.get_external_costs().space,
                    'barrier': trip.get_external_costs().barrier,
                    'congestion': trip.get_external_costs().congestion
                },
                'internalCosts': {'all': new_segment.get_internal_costs().value}
            },
            'waypoints': segment_waypoints

        }

        list_segments.append(dict_segment)

    dict_new_result = {
        'tripMode': input_mode,
        'distance': trip.get_distance(),
        'duration': trip.get_duration(),
        'costs': {
            'externalCosts': {
                'all': trip.get_external_costs().all,
                'air': trip.get_external_costs().air_pollution,
                'noise': trip.get_external_costs().noise_pollution,
                'climate': trip.get_external_costs().climate,
                'accidents': trip.get_external_costs().accidents,
                'space': trip.get_external_costs().space,
                'barrier': trip.get_external_costs().barrier,
                'congestion': trip.get_external_costs().congestion
            },
            'internalCosts': {'all': trip.get_internal_costs().value}

        },

        'segments': list_segments

    }

    return dict_new_result


if __name__ == "__main__":
    app.run()
