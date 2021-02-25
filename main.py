import pandas

csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in csv_data.iterrows()}

not_end = True

while not_end:
    print("\n\nExit with 'exit")
    user_input = input("Enter a word: ").upper()
    phonetic_struc = [nato_alphabet[letter] for letter in user_input]
    print(phonetic_struc)
    if user_input == "EXIT":
        not_end = False