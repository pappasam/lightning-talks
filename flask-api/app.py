'''Flask REST api in 79 lines of Python 3.6'''

from flask import Flask, request, jsonify

APP = Flask(__name__)

IN_MEMORY_DATABASE = {
    0: 'my first value',
    1: 'my second value',
    2: 'my third value',
}


@APP.route('/api/resource', methods=['GET'])
def get_resources():
    '''Return all resources in JSON'''
    return jsonify({
        'data': IN_MEMORY_DATABASE,
    })


@APP.route('/api/resource', methods=['POST'])
def create_resource():
    '''Expects JSON body with following schema:
        {
            data: "your new value here"
        }
    '''
    global IN_MEMORY_DATABASE
    json_body = request.get_json()
    if json_body is None or 'data' not in json_body:
        return jsonify({
            'data': 'error: bad request',
        }), 400  # Bad Request
    value = json_body['data']
    new_db_id = max(IN_MEMORY_DATABASE.keys()) + 1
    IN_MEMORY_DATABASE[new_db_id] = value
    return jsonify({
        'data': 'ok',
    })


@APP.route('/api/resource/<int:resource_id>', methods=['PUT'])
def create_or_update_resource(resource_id):
    '''Expects JSON body with following schema:
        {
            data: "your new value here"
        }
    '''
    global IN_MEMORY_DATABASE
    json_body = request.get_json()
    if json_body is None or 'data' not in json_body:
        return jsonify({
            'data': 'error: bad request',
        }), 400  # Bad Request
    value = json_body['data']
    success_message = (
        'ok: resource modified'
        if resource_id in IN_MEMORY_DATABASE else
        'ok: resource created'
    )
    IN_MEMORY_DATABASE[resource_id] = value
    return jsonify({
        'data': success_message,
    })


@APP.route('/api/resource', methods=['DELETE'])
def delete_resources():
    '''Performs the simple action of deleting the entire database'''
    global IN_MEMORY_DATABASE
    IN_MEMORY_DATABASE = {}
    return jsonify({
        'data': 'ok'
    })


if __name__ == '__main__':
    APP.run(debug=True)
