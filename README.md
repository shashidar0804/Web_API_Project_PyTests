# Web_API_Project_PyTests

# Packages and Programming tools Used

Python - Python 3.7.7

Libraries used - pytest , requests , json

# Test Cases Tested

Test Token Authentication

Review users list from URL

Test Valid user information based on token and test invalid user

Update valid user details based on valid token

# How to run the Test

py.test -v

To save the results to a log :  py.test -v | tee my_ouptut.log

# Method used to get the tokens 

POSTMAN has been used to get the token for the URL  http://localhost:8080/api/auth/token


# Negative Tests tested :

1. Test invalid user details with Token (GET user) -  Test case failed as expected 

2. Test invalid user in the URL -  Test assertion passed with 401 status code as expected

3. Test PUT user or Update user details with valid token - Test case failed with 500 status code as there is a bug in the code (dict.iteritems() will not work as it was removed in Python3 so the code need to be fixed to dict.items())

4. Test GET specific user with valid token and invalid userid - Test case failed with 500 status code as the server is throwing an error "payload = {'firstname': query[0][0],
IndexError: list index out of range"  This needs a fix.




