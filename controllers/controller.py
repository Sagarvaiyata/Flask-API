from flask import Blueprint, jsonify, request
from models.heart import heart

bp = Blueprint('routes', __name__)
obj = heart()

@bp.route('/home', methods=['GET'])
def get_home():
    return jsonify(obj.home())

@bp.route('/heart', methods=['GET'])
def get_heart():
    return jsonify(obj.heart())

@bp.route('/heart', methods=['POST'])
def post_heart():
    return jsonify(obj.heart())

@bp.route('/update', methods=['PUT'])
def put_heart():
    return jsonify(obj.put())

@bp.route('/delete', methods=['DELETE'])
def delete_heart():
    return jsonify(obj.delete())