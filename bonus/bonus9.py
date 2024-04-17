# Check password strength

# Conditions for password strength:
# 1) 8 characters or more
# 2) At least one digit
# 3) At least one uppercase letter
# 4) At least one lowercase letter

password_good = True
password = input("Enter new password: ")

if len(password) >= 8 and \
    any([char.isdigit() for char in password]) and \
    any([char.isupper() for char in password]) and \
    any([char.islower() for char in password]):
    print("Password is strong")
else:
    print("Password is weak")



