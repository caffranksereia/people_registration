data_registration = []


def process_registration() -> None:
    registration()


def registration() -> list[dict[str, str]]:
    i = 0

    data = data_registration
    while i < 3:
        name = input("What's your name: ")
        email = input("What's your email: ")
        password = input("What's your password: ")
        registered_person = input("CPF:")
        nick_name = input("nick name: ")

        person = {
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

        data_registration.append(person)
        i += 1

    return data


def list_registration(data: list) -> list:
    data = data_registration

    return data


def update_registration() -> None:
    return None


def delete_registration() -> None:
    return None
