# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""

    if ":" not in time_str or len(time_str) != 8:
        raise ValueError("String is not in the right format")

    list_of_nums = time_str.split(":")

    sum = 0

    for num in list_of_nums:
        if not num.isdigit():
            raise ValueError("Numbers must be valid digits")

        sum += int(num)

    return sum


print(sum_current_time('01:02:03'))
