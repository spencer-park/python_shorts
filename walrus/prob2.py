username = ""
while not username:
    username = input("Enter username : ")
    if not username:
        print(f"'{username}' cannot be username.")
print(f"Welcome! {username}")