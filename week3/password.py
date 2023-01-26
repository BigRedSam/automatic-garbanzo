secret_password = "kittens"     # Super top secret password

password = input("Enter the secret password: ")

if password == secret_password:
    print("Welcome, authorized user")
else:
    print("Sorry wrong password")
    