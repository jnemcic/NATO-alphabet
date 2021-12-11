import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
user_word = input("Enter a word to be converted to NATO alphabet: ").upper()
nato_list = [data_dict[letter] for letter in user_word]
print(nato_list)
