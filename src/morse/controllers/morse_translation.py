def translation(text):
    letters = list(text)
    lijst_letters = []
    for i in range(len(letters)):
        if letters[i] == "a":
            k = list(".-")
            lijst_letters.append(k)
        if letters[i] == "b":
            k = list("-...")
            lijst_letters.append(k)
        if letters[i] == "c":
            k = list("- -.")
            lijst_letters.append(k)
        if letters[i] == "d":
            k = list("-..")
            lijst_letters.append(k)
        if letters[i] == "e":
            k = list(".")
            lijst_letters.append(k)
        if letters[i] == "f":
            k = list("..-.")
            lijst_letters.append(k)
        if letters[i] == "g":
            k = list("--.")
            lijst_letters.append(k)
        if letters[i] == "h":
            k = list("....")
            lijst_letters.append(k)
        if letters[i] == "i":
            k = list("..")
            lijst_letters.append(k)
        if letters[i] == "j":
            k = list(".---")
            lijst_letters.append(k)
        if letters[i] == "k":
            k = list("-.-")
            lijst_letters.append(k)
        if letters[i] == "l":
            k = list(".-..")
            lijst_letters.append(k)
        if letters[i] == "m":
            k = list("--")
            lijst_letters.append(k)
        if letters[i] == "n":
            k = list("-.")
            lijst_letters.append(k)
        if letters[i] == "o":
            k = list("---")
            lijst_letters.append(k)
        if letters[i] == "p":
            k = list(".--.")
            lijst_letters.append(k)
        if letters[i] == "q":
            k = list("--.-")
            lijst_letters.append(k)
        if letters[i] == "r":
            k = list(".-.")
            lijst_letters.append(k)
        if letters[i] == "s":
            k = list("...")
            lijst_letters.append(k)
        if letters[i] == "t":
            k = list("-")
            lijst_letters.append(k)
        if letters[i] == "u":
            k = list("..-")
            lijst_letters.append(k)
        if letters[i] == "v":
            k = list("...-")
            lijst_letters.append(k)
        if letters[i] == "w":
            k = list(".--")
            lijst_letters.append(k)
        if letters[i] == "x":
            k = list("-..-")
            lijst_letters.append(k)
        if letters[i] == "y":
            k = list("-.--")
            lijst_letters.append(k)
        if letters[i] == "z":
            k = list("--..")
            lijst_letters.append(k)
        if letters[i] == " ":
            k = "spatie"
            lijst_letters.append(k)

    print(lijst_letters)
    return lijst_letters
