from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model.models import db
from model.models import User

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbidentity'
db.init_app(application)
#db = SQLAlchemy(application)
ma = Marshmallow(application)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserSchemaAll(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')

user_schema_full = UserSchemaAll()
users_schema_full = UserSchemaAll(many=True)


@application.route("/users", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@application.route("/users", methods=["GET"])
def get_user():
    users = User.query.all()
    result = users_schema_full.dump(users)
    return jsonify(result.data)

@application.route("/users/<id>", methods=["GET"])
def get_user_by_id(id):
    user = User.query.get(id)
    return user_schema_full.jsonify(user)

@application.route("/users/<id>", methods=["PUT"])
def update_user_by_id(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)

@application.route("/users/<id>", methods=["DELETE"])
def delete_user_by_id(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

if __name__ == '__main__':
    application.run(debug=True, port=8080)
