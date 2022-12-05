nickname = "Spencer"
username = "스펜서"

if not (display_name := nickname or username):
    display_name = "Guest"
print(f"Access {display_name}")