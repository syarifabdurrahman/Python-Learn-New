import pandas

data_file = pandas.read_csv(
    r'Depth_python\C_NATO_Alphabet_Project\nato_phonetic_alphabet.csv')
# data_file_dict = data_file.to_dict()
data_file_dict = {row.letter: row.code for (
    index, row) in data_file.iterrows()}

print(data_file_dict)

user_input = input("Enter word: ").upper()
phonetic_list = [data_file_dict[word]
                 for word in user_input if word in data_file_dict]
print(phonetic_list)
