file = open("sample.txt", "r")
vowels, consonants, upper, lower = 0, 0, 0, 0

for line in file.readlines():
    for letter in line:
        if letter.isalpha():
            if letter.lower() in "aeiou":
                vowels += 1
            if letter.isupper():
                upper += 1
            if letter.islower():
                lower += 1
            if letter.lower() not in "aeiou":
                consonants += 1
        else:
            continue

print(f"Number of vowels: {vowels}\nNumber of consonants: {consonants}\nNumber of Upper characters: {upper}\nNumber of Lower characters: {lower}")
