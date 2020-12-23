"""Program to count and say the numbers."""


def count_n_say(number):
    return count_n_say_help('1', number - 1)


def count_n_say_help(start, number):
    if number == 0:
        return start
    char = None
    count = 0
    output = ''
    for i in range(len(start)):
        if char == start[i]:
            count += 1
        else:
            if char is None:
                char = start[i]
                count = 1
            else:
                output += str(count) + char
                char = start[i]
                count = 1
    output += str(count) + char
    return count_n_say_help(output, number - 1)
