API urls:

register new user: 
    local: POST 'http://127.0.0.1:8000/api/auth/users/'
    heroku:

get user token:
    local: POST 'http://127.0.0.1:8000/api/auth/token/login/'
    heroku:

get users:
    local: GET 'http://127.0.0.1:8000/api/users/'
    heroku: