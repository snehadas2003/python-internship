username=input("enter a user name:")
def clean_name(name):
    return name.strip()
corrected_name=clean_name(username)
print(corrected_name)