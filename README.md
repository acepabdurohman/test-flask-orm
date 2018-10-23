# Testing CRUD Python Application with Flask and SQLAlchemy

Additional config for deployment to openshift

# add user data

type:POST

endpoint: /users

request: {
    "username": "acep",
    "email": "acep@xxx.com"
}

# get all users data

type:GET

endpoint: /users/<id>





