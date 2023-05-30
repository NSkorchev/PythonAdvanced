name = input()
password = input()

with open("users_db.txt", "a") as file:
    file.write(f"Username: {name}, password: {password}\n")
