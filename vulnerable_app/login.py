print("=== Employee Login Portal ===")

stored_username = "admin"
stored_password = "admin123"

username = input("Username: ")
password = input("Password: ")

if username == stored_username and password == stored_password:
    print("Access Granted")
else:
    print("Access Denied") 