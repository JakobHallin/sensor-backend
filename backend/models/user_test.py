import models.user as user_model
## Test user creation
def test_userCreation():
    User1 = user_model.create_user(1, "test@gmail.com", "testuser",  "password") 
    creatuser = (
        User1.id == 1 and
        User1.email == "test@gmail.com" and
        User1.username == "testuser" and
        User1.password =="password"
    )
    print("User creation test passed:", creatuser)