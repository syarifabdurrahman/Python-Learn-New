import pandas

data_file = pandas.read_csv(
    r'Depth_python\C_NATO_Alphabet_Project\nato_phonetic_alphabet.csv')
# data_file_dict = data_file.to_dict()
data_file_dict = {row.letter: row.code for (
    index, row) in data_file.iterrows()}

print(data_file_dict)


def generate_phonetic():
    user_input = input("Enter word: ").upper()
    try:
        phonetic_list = [data_file_dict[word]
                         for word in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
    else:
        print(phonetic_list)


generate_phonetic()
