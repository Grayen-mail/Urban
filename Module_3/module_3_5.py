def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)

print(get_multiplied_digits(0))
print(get_multiplied_digits(10))
print(get_multiplied_digits(0b010))
print(get_multiplied_digits(0o010))
print(get_multiplied_digits(0x010))
