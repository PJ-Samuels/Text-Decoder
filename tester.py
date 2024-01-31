def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    num_word = {}
    for line in lines:
        parts = line.split()
        num = int(parts[0])
        word = ' '.join(parts[1:])
        num_word[num] = word

    max_num = max(num_word.keys())

    decoded_numbers = []
    current_num = 1
    line_length = 1
    while current_num <= max_num:
        decoded_numbers.append(current_num)
        line_length += 1
        current_num += line_length

    decoded_message = [num_word[num] for num in decoded_numbers]
    return ' '.join(decoded_message)

message_file = 'your_file_name.txt'
decoded_message = decode(message_file)
print(decoded_message)

