# program login

def f(u, p):
    if u == "admin" and p == "123":
        print("Login berhasil")
        print("Selamat datang admin")
    else:
        print("Login gagal")
        print("Coba lagi")

user = input("Username: ")
pw = input("Password: ")

f(user, pw)