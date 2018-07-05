
from flask import jsonify


def success(data=None, message='success'):
    return {
        "status": 200,
        "data": data,
        "message": message
    }, 200


def error(status=500, data=None, message='服务器错误'):
    return jsonify({
        "status": status,
        "data": data,
        "message": message
    }), status
