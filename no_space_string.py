def no_space_str(string):
    spaces = []
    final = ''

    for i in range(len(string)):
        if string[i] == ' ':
            spaces.append(i)

    for i in range(len(string)):
        if i not in spaces:
            final += string[i]


    return final


print(no_space_str('Давай уже ложиться спать'))