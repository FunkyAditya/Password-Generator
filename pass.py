def generate_numbers(birthdate):
    day, month, year = birthdate.split("/")
    day = str(int(day))[:3].lstrip("0")
    month = str(int(month))[:3].lstrip("0")
    year = str(int(year))[:3].lstrip("0")
    numbers = []
    for i in range(1, 1000):
        if day:
            numbers.append(day + str(i))
        if month:
            numbers.append(month + str(i))
        if year:
            numbers.append(year + str(i))
    return numbers

username = input("Enter your username: ")
birthdate = input("Enter your birthdate (in the format dd/mm/yyyy): ")

numbers = generate_numbers(birthdate)

with open("usernames.txt", "w") as file:
    for number in numbers:
        file.write(username + "@" + number + "\n")

print("Usernames have been generated and saved to usernames.txt")
