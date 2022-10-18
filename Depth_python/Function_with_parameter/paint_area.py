# paint area calculator

def paint_calc(height,width,cover):
    result = round((height*width)/cover)
    print (f"number of can = {result}")
    print(f"You\'ll  need {result} cans of paint.")



test_height = int(input("Height of wall: "))
test_width = int(input("Height of width: "))
coverage = 5
paint_calc(height=test_height,width=test_width,cover=coverage)


