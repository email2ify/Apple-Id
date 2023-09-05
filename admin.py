# Set the initial status to indicate the user is logged out
logged_out = True

# Begin a loop to handle the login process
while logged_out:
    # Get the username from the user
    username = input("Username: ")

    # Check if the username is 'admin'
    if username == "admin":
        # If the username is 'admin', request the password
        password = input("Password: ")

        # Check if the password is correct
        if password == "admin2":
            print("You've successfully logged in!")
        else:
            print("Wrong password")
            continue
    else:
        # If user is not admin
        print("You are not admin, try again")
        continue

    # If both username and password are correct
    print("Welcome admin!")

    # Change the status to indicate the user is logged in,
    # this will stop the loop from running
    logged_out = False


# The code below repeats the same logic,
# just a different approach for verifying password,
# so I won't comment it line by line.

while logged_out:
    username = input("Username: ")

    if username == "admin":
        password = input("Password: ")
        if password != "admin2":
            print("Wrong password")
            continue
        else:
            print("You've successfully logged in!")
    else:
        print("You are not admin, try again")
        continue

    print("Welcome admin!")
    logged_out = False
