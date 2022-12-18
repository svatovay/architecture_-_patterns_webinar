def access_user(request, environ):
    env_logname = environ.get('LOGNAME')
    if env_logname == 'alexeysvatov':
        request['access_user'] = 'Framework owner'
    else:
        request['access_user'] = 'Unknown user'
    return request


middlewares = [access_user]
