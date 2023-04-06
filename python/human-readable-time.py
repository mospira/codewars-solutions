# 5 kyu

# TAGS {DATE TIME} {MATHEMATICS} {ALGORITHMS}

# DESCRIPTION:
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):
    minutes = seconds//60
    seconds = seconds-(60*minutes)
    hours = minutes//60
    minutes = minutes%60
    # Adding a 0 to the front of the number if it is less than 10.
    hours = add_padding(hours)
    minutes = add_padding(minutes)
    seconds = add_padding(seconds)
    return f'{hours}:{minutes}:{seconds}'

def add_padding(int):
    if int<10:
        return f'0{int}'
    return f'{int}'

