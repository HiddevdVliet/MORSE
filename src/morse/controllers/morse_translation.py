def translation(message):
    letters = list(message)
    lijst_letters = []
    for i in range(len(letters)):
        if letters[i] == "a" or letters[i] == "A":
            k = list(".-")
            lijst_letters.append(k)
        if letters[i] == "b" or letters[i] == "B":
            k = list("-...")
            lijst_letters.append(k)
        if letters[i] == "c" or letters[i] == "C":
            k = list("-.-.")
            lijst_letters.append(k)
        if letters[i] == "d" or letters[i] == "D":
            k = list("-..")
            lijst_letters.append(k)
        if letters[i] == "e" or letters[i] == "E":
            k = list(".")
            lijst_letters.append(k)
        if letters[i] == "f" or letters[i] == "F":
            k = list("..-.")
            lijst_letters.append(k)
        if letters[i] == "g" or letters[i] == "G":
            k = list("--.")
            lijst_letters.append(k)
        if letters[i] == "h" or letters[i] == "H":
            k = list("....")
            lijst_letters.append(k)
        if letters[i] == "i" or letters[i] == "I":
            k = list("..")
            lijst_letters.append(k)
        if letters[i] == "j" or letters[i] == "J":
            k = list(".---")
            lijst_letters.append(k)
        if letters[i] == "k" or letters[i] == "K":
            k = list("-.-")
            lijst_letters.append(k)
        if letters[i] == "l" or letters[i] == "L":
            k = list(".-..")
            lijst_letters.append(k)
        if letters[i] == "m" or letters[i] == "M":
            k = list("--")
            lijst_letters.append(k)
        if letters[i] == "n" or letters[i] == "N":
            k = list("-.")
            lijst_letters.append(k)
        if letters[i] == "o" or letters[i] == "O":
            k = list("---")
            lijst_letters.append(k)
        if letters[i] == "p" or letters[i] == "P":
            k = list(".--.")
            lijst_letters.append(k)
        if letters[i] == "q" or letters[i] == "Q":
            k = list("--.-")
            lijst_letters.append(k)
        if letters[i] == "r" or letters[i] == "R":
            k = list(".-.")
            lijst_letters.append(k)
        if letters[i] == "s" or letters[i] == "S":
            k = list("...")
            lijst_letters.append(k)
        if letters[i] == "t" or letters[i] == "T":
            k = list("-")
            lijst_letters.append(k)
        if letters[i] == "u" or letters[i] == "U":
            k = list("..-")
            lijst_letters.append(k)
        if letters[i] == "v" or letters[i] == "V":
            k = list("...-")
            lijst_letters.append(k)
        if letters[i] == "w" or letters[i] == "W":
            k = list(".--")
            lijst_letters.append(k)
        if letters[i] == "x" or letters[i] == "X":
            k = list("-..-")
            lijst_letters.append(k)
        if letters[i] == "y" or letters[i] == "Y":
            k = list("-.--")
            lijst_letters.append(k)
        if letters[i] == "z" or letters[i] == "Z":
            k = list("--..")
            lijst_letters.append(k)
        if letters[i] == " ":
            k = "spatie"
            lijst_letters.append(k)

    print(lijst_letters)
    return lijst_letters
