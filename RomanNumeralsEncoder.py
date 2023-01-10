def roman_num_encoder(integer):
    if not(integer >= 1 and integer <= 3999):
        # non-valid input
        return "Please try again: 1 <= k <= 3999."
    else:
        # valid input

        str_of_integer = [int(i) for i in str(integer)]

        for i in range(len(str_of_integer)):

            remaining_result = str_of_integer.pop()
            print(remaining_result)


            a = integer / (10 ** i)

            final_string = ''

            if i == 0:
                if a != 0:
                    final_string += 'I'

            if i == 1:
                if a != 0:
                    final_string += 'X'

            if i == 2:
                if a != 0:
                    final_string += 'C'

            if i == 3:
                if a != 0:
                    final_string += 'M'

    return final_string

print(roman_num_encoder(1990))