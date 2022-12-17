def access_user(request, environ):
    if environ['LOGNAME'] == 'alexeysvatov':
        request['access_user'] = 'Framework owner'
    else:
        request['access_user'] = 'Unknown user'
    return request


middlewares = [access_user]
