import random
from utils import send_email
from file_manager import append, read

def register():
    full_name = input("full name: ")
    email1 = input("email: ")
    password1 = input("password1: ")
    password2 = input("password2: ")

    while password1 != password2:
        print("incorrect password")
        password1 = input("password1: ")
        password2 = input("password2: ")

    random_num = random.randint(1000, 10000)
    send_email(receiver_email=email1, body = str(random_num))
    append(filename = "users", data=[full_name, email1, password1, False])
    append(filename = "codes", data=[email1, random_num])
    return check_otp(random_num)

def check_otp(correct_code):
    code = input("enter the code: ")
    if code == str(correct_code):
        return True
    else:
        return False

def login():
    email2 = input("email: ").strip()
    password = input("password: ").strip()

    users = read("users.csv")
    for user in users:
        full_name, email1, password1, is_verified = [field.strip() for field in user]

        print(f"Checking: {email1=} {password1=} {is_verified=}")

        if email1.lower() == email2.lower() and password1 == password:
            if is_verified == "True":
                print(f"Welcome back, {full_name}!")
                return True
            else:
                print("Account not verified")
                return False

    print("Incorrect email or password")
    return False
