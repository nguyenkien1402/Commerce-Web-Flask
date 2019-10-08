from functools import wraps
from flask import redirect, request, url_for
from firebase_admin import  auth

def verify_firebase_id_token(token):
    """
    A helper function for verifying ID tokens issued by Firebase
    See https://firebase.google.com/docs/auth/admin/verify-id-tokens for
    more information.
    Paramters:
        token: a token issued by firebase
    Output:
        auth_context: Authentication context
    """
    try:
        full_auth_context = auth.verify_id_token(token)
        print(full_auth_context)
        auth_context = {
            'username': full_auth_context.get('name'),
            'uid': full_auth_context.get('uid'),
            'email': full_auth_context.get('email')
        }
    except:
        return {}

    return auth_context

def auth_required(f):
    """
    A decorator for view function that require authentication
    If signin, pass the request to decorated view function with authentication context
    otherwise, reject the request
    :param f:
        the view function to decorate
    :return:
        decorated function: the decorated function.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        firebase_id_token = request.cookies.get('firebase_id_token')
        if not firebase_id_token:
            print("Not authenticated")
            return redirect('/signin')

        auth_context = verify_firebase_id_token(firebase_id_token)
        if not auth_context:
            print("I think the token is invalid")
            return redirect('/signin')

        return f(auth_context=auth_context, *args, **kwargs)
    return decorated


def auth_optional(f):
    """
    A decorator for view function where the authentication is optional.
    If signed in pass the request to decorated view function with authentication context.
    :param f:
        the view function to decorate.
    :return:
        decorator: the decorator function
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        firebase_id_token = request.cookies.get('firebase_id_token')
        print("token:",firebase_id_token)
        if not firebase_id_token:
            return f(auth_context=None, *args, **kwargs)

        auth_context = verify_firebase_id_token(firebase_id_token)
        if not auth_context:
            return f(auth_context=None, *args, **kwargs)
        return f(auth_context=auth_context, *args, **kwargs)
    return decorated