class User:
  def __init__(self, id, email, username, password):
    self.id = id  # Unique user
    self.email = email
    self.username = username
    self.password = password  # Hashed password

def create_user(id, email, username, password):
    return User(id, email, username, password)
def get_user_info(user):
    return {
        "id": user.id,
        "email": user.email,
        "username": user.username
    }