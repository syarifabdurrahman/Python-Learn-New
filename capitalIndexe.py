
def capital_indexes(string:str):
   result = [i for i, char in enumerate(string) if char.isupper()]
   print(result)




capital_indexes("HeLlO")