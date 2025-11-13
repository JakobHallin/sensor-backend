import models.user as user_model
def create_user(id, email, username, password):
    return user_model.User(id, email, username, password)
def get_user_info(user):
    return {
        "id": user.id,
        "email": user.email,
        "username": user.username
    }
print ( "hello world")
User1 = create_user(1, "test@gmail.com", "testuser", "assword") 
print(get_user_info(User1))