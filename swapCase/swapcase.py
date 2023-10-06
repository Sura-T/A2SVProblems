def swap_case(s):
    swapped = ""
    for char in s:
        if char.isupper():
            swapped += char.lower()
        else:
            swapped += char.upper()
    return swapped