with open(r'Depth_python\DAY26_List_comprehension\data_1.txt', mode='r') as data_1, open('Depth_python\DAY26_List_comprehension\data_2.txt', mode='r') as data_2:
    content_1 = data_1.read()
    content_2 = data_2.read()
    data_1_list = content_1.splitlines()
    data_2_list = content_2.splitlines()
    result = [eval(data) for data, newdata in zip(
        data_1_list, data_2_list) if data in data_1_list and data in data_2_list]
    print(result)
