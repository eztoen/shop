from users.schemas import UserSchema

def get_users():
    ...

def create_user(new_user: UserSchema) -> dict:
    return {'success': True, 'hello': new_user.username}