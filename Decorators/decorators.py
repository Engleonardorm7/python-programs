PASSWORD="12345"


def password_required(func):
    def wrapper():
        password = input("Type your password")

        if password == PASSWORD:
            return func()
        else:
            print("Incorrect Password")

    return wrapper

@password_required
def needs_password():
    print("Correct")


if __name__=="__main__":
    needs_password()