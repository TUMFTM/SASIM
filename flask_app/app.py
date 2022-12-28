from flask import Flask, request
from flask_cors import CORS
from flask import send_from_directory
from flask import render_template
from flask_caching import Cache

from controllers.geocoding.GeocodingController import GeocodingController
from controllers.trip.TripController import TripController
from helpers.ApiHelper import ApiHelper

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

server = Flask(__name__)

server.config.from_mapping(config)
cache = Cache(server)
CORS(server)

FLUTTER_WEB_APP = 'templates'

@server.route('/web/')
def render_page_web():
    return render_template('index.html')

@server.route('/')
def home_page_web():
    return render_page_web()

@server.route('/web/<path:name>')
def return_flutter_doc(name):
    datalist = str(name).split('/')
    DIR_NAME = FLUTTER_WEB_APP

    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]

    return send_from_directory(DIR_NAME, datalist[-1])

@server.route('/plattform', methods=['GET'])
def return_trip():
    api_helper = ApiHelper()

    input_start_address = str(request.args['inputStartAddress'])
    start_location = get_geolocation(input_start_address)

    input_end_address = str(request.args['inputEndAddress'])
    end_location = get_geolocation(input_end_address)

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

@cache.memoize(300)
def get_geolocation(address: str):
    geocoding_controller = GeocodingController()

    return geocoding_controller.get_location(address)

