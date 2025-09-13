from functools import wraps
from flask import abort
from flask_login import current_user

def roles_required(*names):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            user_roles = {r.name for r in getattr(current_user, "roles", [])}
            if not set(names).intersection(user_roles):
                abort(403)
            return fn(*args, **kwargs)
        return wrapper
    return decorator

