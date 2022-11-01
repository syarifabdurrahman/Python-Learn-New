sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
result = {char: len(char) for char in sentence_list}

# print(len(sentence_list[0]))

print(result)
