failed_attempts = {}
MAX_ATTEMPTS = 3

def login(username, password):
    real_password = "SecurePass123!"

    if username not in failed_attempts:
        failed_attempts[username] = 0

    if failed_attempts[username] >= MAX_ATTEMPTS:
        print(f"ALERT: Account '{username}' is locked due to too many failed attempts.")
        return

    if password == real_password:
        print(f"Access granted. Welcome, {username}!")
        failed_attempts[username] = 0
    else:
        failed_attempts[username] += 1
        remaining = MAX_ATTEMPTS - failed_attempts[username]
        print(f"Access denied. Incorrect password. {remaining} attempt(s) remaining.")

        if failed_attempts[username] >= MAX_ATTEMPTS:
            print(f"ALERT: Account '{username}' has been locked after {MAX_ATTEMPTS} failed attempts.")

print("Login Monitor Demo")
print("------------------")
print("Hint: the correct password is SecurePass123!")
print()

while True:
    username = input("Enter username (or 'quit' to exit): ")
    if username.lower() == "quit":
        break
    password = input("Enter password: ")
    login(username, password)
    print()
