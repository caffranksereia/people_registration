data_registration = []


def menu_registration() -> None:
    while True:
        print("\n===== PEOPLE REGISTRATION =====")
        print("1 - Register person")
        print("2 - List people")
        print("3 - Update person")
        print("4 - Delete person")
        print("0 - Exit")

        option = input("Choose an option: ")

        if option == "1":
            registration()

        elif option == "2":
            list_registration()

        elif option == "3":
            update_registration()

        elif option == "4":
            delete_registration()

        elif option == "0":
            print("Exiting application...")
            break

        else:
            print("Invalid option!")


def registration() -> None:

    data = data_registration

    name = input("What's your name: ")
    email = input("What's your email: ")
    password = input("What's your password: ")
    registered_person = input("CPF:")
    nick_name = input("nick name: ")

    is_duplicate = False

    new_person = {
        "name": name,
        "email": email,
        "password": password,
        "registered_person": registered_person,
        "nick_name": nick_name,
    }
    for person in data:
        if person["registered_person"] == registered_person:
            print("Exist!")
            continue

        if person["email"] == email:

            print("Email ja utilizado!")

        if person["nick_name"] == nick_name:
            print("nick name existente!")

    if not is_duplicate:
        data_registration.append(new_person)


def list_registration() -> None:
    for index, person in enumerate(data_registration):
        print("-" * 30)
        print("List Registration")
        print(f"Index: {index}")
        print(f"Name: {person['name']}")
        print(f"Email: {person['email']}")
        print("-" * 30)


def update_registration() -> None:
    update = int(input("What's registration update?  "))

    for index, people in enumerate(data_registration):
        if update == index:
            update_email = input("email:")
            update_nick_name = input("nick name:")

            people[index]["email"] = update_email
            people[index]["nick_name"] = update_nick_name

            print("Registration updated!")
            break
        else:
            print("Registration does not exist!")


def delete_registration() -> None:
    delete = int(input("What's registration update?  "))
    for index in range(len(data_registration)):
        if delete == index:
            data_registration.pop(index)
            print("Registration delete!")
            break
    else:
        print("Registration does not exist!")
