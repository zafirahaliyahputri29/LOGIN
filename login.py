# program login

USERS = {
    "admin": "123",
    "user1": "abc",
}

def validate_login(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False

def show_success(username):
    print("Login berhasil")
    print(f"Selamat datang {username}")

def show_error():
    print("Login gagal")
    print("Coba lagi")   

username_input = input("Username: ")    
password_input = input("Password: ")

is_valild = validate_login(username_input, password_input)

if is_valild:
    show_success(username_input)
else:
    show_error()