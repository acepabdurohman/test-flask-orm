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

endpoint: /users

# get all users data by id

type:GET

endpoint: /users/{id}

# update user data

type:PUT

endpoint: /users/{id}

request: {
    "username": "acep",
    "email": "acep@xxx.com"
}

# delete user data by id

type:DELETE

endpoint: /users/{id}