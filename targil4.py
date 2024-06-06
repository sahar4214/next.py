import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character):
        self.illegal_character = illegal_character

    def __str__(self):
        return f"The username contains an illegal character: '{self.illegal_character}'"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self, missing_character_type):
        self.missing_character_type = missing_character_type

    def __str__(self):
        return f"The password is missing a character ({self.missing_character_type})"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    if not all(char.isalnum() or char == '_' for char in username):
        raise UsernameContainsIllegalCharacter([char for char in username if not (char.isalnum() or char == '_')][0])
    if len(username) < 3:
        raise UsernameTooShort
    if len(username) > 16:
        raise UsernameTooLong

    required_characters = [False, False, False, False]
    for char in password:
        if char.isupper():
            required_characters[0] = True
        elif char.islower():
            required_characters[1] = True
        elif char.isdigit():
            required_characters[2] = True
        elif char in string.punctuation:
            required_characters[3] = True

    if not all(required_characters):
        missing_characters = ["Uppercase" if not required_characters[0] else "",
                              "Lowercase" if not required_characters[1] else "",
                              "Digit" if not required_characters[2] else "",
                              "Special" if not required_characters[3] else ""]
        raise PasswordMissingCharacter(", ".join(filter(None, missing_characters)))

    if len(password) < 8:
        raise PasswordTooShort
    if len(password) > 40:
        raise PasswordTooLong

    print("OK")


def main():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_input(username, password)
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong, PasswordMissingCharacter,
                PasswordTooShort, PasswordTooLong) as e:
            print(e)


if __name__ == "__main__":
    main()
