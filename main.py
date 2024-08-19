import pandas
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_data_frame = pandas.DataFrame(alphabet_data)
alphabet_dict = {}
for (index, row) in alphabet_data_frame.iterrows():
    alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}

word = input("Enter a Word : ")
answer = [alphabet_dict[letter.upper()] for letter in word]
print(answer)

