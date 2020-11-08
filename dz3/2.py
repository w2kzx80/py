
def print_user(**kwargs):
    print(f"Name: {kwargs.get('name')}\r\nSurname: {kwargs.get('surname')}\r\nYear: {kwargs.get('year')}\r\nCity: {kwargs.get('city')}\r\nE-mail: {kwargs.get('email')}")

print_user(name="Roman",surname="Apanovici",city="Suncity",email="somebody@gmail.com",year=0)