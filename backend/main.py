import models.user as user_model
import models.user_test as user_test


print ( "hello world")
User1 = user_model.create_user(1, "test@gmail.com", "testuser", "assword") 
print(user_model.get_user_info(User1))

user_test.test_userCreation()
