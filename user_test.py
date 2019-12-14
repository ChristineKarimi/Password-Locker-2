import unittest # Importing the unittest module
from user import User # Importing the User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User('mukhtarabdirahman','codePanther') # created user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'mukhtarabdirahman') 
        self.assertEqual(self.new_user.password,'codePanther') 
    def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into
        the user list
        '''
        self.new_user.save_user()# saving the new user
        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple user
            objects to our user_list
        """
        self.new_user.save_user()
        test_user = User('Ahmed','hajia')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User('Ahmed','hajia')
            test_user.save_user()
            
            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)
    
    def test_find_user_by_username(self):
        """
        Test to find out if we can find user by username and display information
        """
        self.new_user.save_user()
        test_user = User('Ahmed','hajia')
        test_user.save_user()
        
        found_user = User.find_by_username('Ahmed')
        self.assertEqual(found_user.password, test_user.password)
        
    def test_if_user_exists(self):
        """
        Test to see if a given user exists
        """
        self.new_user.save_user()
        test_user = User('Ahmed','hajia')
        test_user.save_user()
        
        user_exists = User.user_exist('Ahmed')
        self.assertTrue(user_exists)
        
    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        
        self.assertEqual(User.display_all_users(),User.user_list)
        
    
        
        
        
		
        
          
   
        
        
        
        
        
   

        
       
if __name__ == '__main__':
    unittest.main()