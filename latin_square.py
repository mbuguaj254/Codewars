def make_latin_square(n):
    # Create an empty list to store the Latin square
    list = []

    # Generate each row of the Latin square
    for i in range(n):
        # Append an empty list for the current row
        list.append([])

        # Generate each cell in the current row
        for j in range(n):
            # Calculate the value for the current cell
            value = (i + j) % n + 1

            # Append the value to the current row
            list[i].append(value)

    # Return the generated Latin square
    return list


print(make_latin_square(4))
