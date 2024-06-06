def find_longest_name(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.readlines()

    longest_name = max(names, key=len).strip()
    return longest_name


def sum_of_name_lengths(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.readlines()

    total_length = sum(len(name.strip()) for name in names)
    return total_length


def write_name_lengths(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        names = [name.strip() for name in file.readlines()]

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for name in names:
            file.write(f"{len(name)}\n")