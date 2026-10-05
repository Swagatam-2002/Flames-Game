from collections import Counter


def calculate_flames(you, person):

    # Convert names to lowercase
    you = you.lower()
    person = person.lower()

    # Remove spaces
    you = you.replace(" ", "")
    person = person.replace(" ", "")

    # Count characters
    d1 = Counter(you)
    d2 = Counter(person)

    # Calculate remaining character count
    l = 0

    for i in d1:
        if i not in d2:
            l += d1[i]
        else:
            l += abs(d1[i] - d2[i])

    for i in d2:
        if i not in d1:
            l += d2[i]

    # FLAMES letters
    arr = ['F', 'L', 'A', 'M', 'E', 'S']

    i = 0

    while len(arr) != 1:
        i = i - 1
        j = 0

        while j < l:
            i += 1
            j += 1

            if i == len(arr):
                i = 0

        if i == 0:
            arr.pop(len(arr) - 1)
        else:
            arr.pop(i - 1)

    # Convert final letter into result
    if arr[0] == 'F':
        return "Friends"

    elif arr[0] == 'L':
        return "Lovers"

    elif arr[0] == 'A':
        return "Affectionate"

    elif arr[0] == 'M':
        return "Marriage"

    elif arr[0] == 'E':
        return "Enemies"

    else:
        return "Siblings"
