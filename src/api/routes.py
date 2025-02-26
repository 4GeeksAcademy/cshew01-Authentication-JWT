"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import (
    create_access_token, get_jwt_identity, jwt_required
)
# from werkzeug.security import (
#     generate_password_hash,
#     check_password_hash,
# )

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

@api.route("/login", methods=['POST'])
def login():
    body = request.get_json(force=True) 

    user = User.query.filter_by(email=body.get('email')).first()

    if (
        not user or
        not user.check_password(body.get("password"))
    ):
        return jsonify(
            msg="Invalid email or password"
        ), 400

    return jsonify(
        token=create_access_token(
             identity=user
        )
    )

@api.route("/secured", methods=['GET'])
@jwt_required()
def secured():
    return jsonify(
        identity=get_jwt_identity()
    )


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# @api.route('/user', methods=['POST'])
# def create_user():
#     user = User.query.all()
#     return jsonify([user.serialize() for user in users])