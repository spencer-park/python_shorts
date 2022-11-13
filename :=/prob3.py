nickname = "Spencer"
username = "스펜서"

if nickname:
    display_name = nickname
elif username:
    display_name = username
else:
    display_name = "Guest"
print(f"Access {display_name}")