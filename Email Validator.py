import re

def is_valid_email(email):
    # Define the regular expression for a basic email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the regular expression to check the format
    if re.match(email_regex, email):
        return True
    else:
        return False

# Example usage:
email = input("Enter an email address: ")
if is_valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
