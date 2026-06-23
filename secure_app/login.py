import hashlib
def is_strong_password(password):
    
    if len(password) < 8:
        return False
        
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum()  for c in password)

    return has_upper and has_lower and has_digit and has_special

print("=== Secure Employee Login Portal ===")

stored_username = "admin"
stored_password_hash = hashlib.sha256("Admin@123".encode()).hexdigest()

max_attempts = 3
attempt = 0

while attempt < max_attempts:

    username = input("Username: ")
    password = input("Password: ")
    if not is_strong_password(password):
            print("Weak Password Format!")
            continue

    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and entered_password_hash == stored_password_hash:
        print("Access Granted")
        break

    else:
        attempt += 1
        remaining = max_attempts - attempt
        print(f"Access Denied. Attempts left: {remaining}")

if attempt == max_attempts:
    print("Account Locked. Too many failed attempts.")
