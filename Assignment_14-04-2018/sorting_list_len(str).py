data_list = ["Python", "Java", "Dot net", "Javascript", "HTML", "CSS", "C"]

# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if len(x) < len(minimum):
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
del data_list
print(new_list)

