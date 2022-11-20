from flask import Flask, request
from flask_cors import CORS

from AA_new.controllers.geocoding.GeocodingController import GeocodingController
from AA_new.controllers.trip.TripController import TripController
from AA_new.helpers.ApiHelper import ApiHelper

app = Flask(__name__)
CORS(app)


@app.route('/plattform', methods=['GET'])
def return_trip():
    api_helper = ApiHelper()
    geocoding_controller = GeocodingController()

    input_start_address = str(request.args['inputStartAddress'])
    start_location = geocoding_controller.get_location(input_start_address)

    input_end_address = str(request.args['inputEndAddress'])
    end_location = geocoding_controller.get_location(input_end_address)

    input_trip_mode = str(request.args['tripMode'])
    trip_mode = api_helper.get_trip_mode_from_input(input_trip_mode)

    trip_controller = TripController()
    trip = trip_controller.get_trip(
        start_location=start_location,
        end_location=end_location,
        trip_mode=trip_mode
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
        'tripMode': trip_mode.value,
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
        'mobiScore': trip.mobi_score.value,
        'segments': list_segments

    }

    return dict_new_result


if __name__ == "__main__":
    app.run()
