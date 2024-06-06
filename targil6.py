class IDIterator:
    def __init__(self, id_number):
        self.id_number = id_number
        self.current_id = id_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_id >= 999999999:
            raise StopIteration
        self.current_id += 1
        return self.current_id


def check_id_valid(id_number):
    id_str = str(id_number)
    total = 0
    for i in range(1, 10):
        digit = int(id_str[i - 1])
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit = sum(map(int, str(digit)))
        total += digit
    return total % 10 == 0


def id_generator(id_number):
    current_id = id_number
    while current_id < 999999999:
        current_id += 1
        yield current_id


def main():
    id_input = int(input("Enter ID: "))
    valid = check_id_valid(id_input)
    if not valid:
        print("Invalid ID number")
        return

    choice = input("Generator or Iterator? (gen/it)? ")
    if choice == "it":
        id_iterator = IDIterator(id_input)
        for _ in range(10):
            print(next(id_iterator))
    elif choice == "gen":
        generator = id_generator(id_input)
        for _ in range(10):
            print(next(generator))


if __name__ == "__main__":
    main()
