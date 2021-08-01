import json  # imports json module

TOP_EMAIL_DOMAINS = ['protonmail', 'gmail', 'outlook', 'hotmail', 'yahoo', 'icloud', 'zoho', 'hubspot', 'aol', 'gmx',
                     'yandex']  # stores the top 10 free email domain names

print('Welcome to the email slicer program')  # welcome message

is_on = True

while is_on:
    user_input = input("Please enter your email: ")  # prompts user to enter an email

    while True:
        if "@" not in user_input:  # check if the email entered contains a "@"
            print("Invalid email")
            user_input = input("Please enter your email: ")
        else:
            break

    user_name = user_input.split("@")[0]  # takes the part before the @ aka the username of the user
    user_mail = user_input.split("@")[1]  # takes the part after the @ aka the domain name
    name = ""

    if "." in user_name:
        name = user_name.split(".")[0]  # takes the first part before the dot, in this case the first name (ideally)
    else:
        name = user_name  # otherwise sets the name as the username

    email_domain = user_mail.split(".")[0]  # extracts the email domain name

    if email_domain in TOP_EMAIL_DOMAINS:  # outputs a message complimenting the user
        print(f"Hey {name.capitalize()} , I see your email is registered with {email_domain.capitalize()}."
              f"That's cool!")
    else:  # outputs a message complimenting the user
        print(f"Hey {name.capitalize()}, looks like you've got your own custom setup at {email_domain.capitalize()}. "
              f"Impressive")

    user_data = {  # schema for a user data (dictionary)
        'name': name,
        'email domain': email_domain,
        'email': user_input
    }

    with open('users.txt', 'a') as file:
        file.write(json.dumps(user_data) + "\n")  # converts the dictionary into a json format then writes to file

    user_choice = input("Do you wish to continue the program ? Y or N ? ")

    valid_choice = False

    # checks if the user has entered a valid input
    while not valid_choice:
        if user_choice == "Y" or user_choice == "y" or user_choice == "yes" or user_choice == "Yes":
            valid_choice = True
        elif user_choice == "N" or user_choice == "n" or user_choice == "no" or user_choice == "No":
            print("The program will now end")
            is_on = False
            valid_choice = True
        else:
            print("Choice not recognized ")
            user_choice = input("Do you wish to continue the program ? Y or N ? ")
            continue
