class User:
  def __init__(self, id, email, username, password):
    self.id = id  # Unique user
    self.email = email
    self.username = username
    self.password = password  # Hashed password
