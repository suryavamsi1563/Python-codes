import os
# addition of the first line with the second line and giving result to the third line
# data_file = open('data.txt', 'r')
# list_of_integers = []
# while True:
#     x = data_file.readline()
#     print(x)
#     if not x:
#         for line in x:
#             string_of_numbers = line.split(' ')
#             for num in string_of_numbers:
#                 if num.isdecimal():
#                     list_of_integers.append(int(num))
#     break


# connect program--changing the connect line to only connect
os.chdir(r".\connectfiles")
print(os.listdir("."))
list_of_files = ["demo.txt"]
for x in list_of_files:
    if x[-4::] == '.txt':
        print("Now reading a text file")
        with open(x, 'r+') as file:
            while True:
                print("Position before the read: ", file.tell())
                position = file.tell()
                read_data = file.readline()
                print("read data having", read_data[-2:-1:1])
                if read_data[-2:-1:1] == "\n":
                    print("Read data has a new line at the end.")
                    read_data = read_data[:-2]
                print(read_data)
                print("Length of data is : ", len(read_data))
                print("Position after the read: ", file.tell())
                if not read_data:
                    print("breaking the loop")
                    break
                data = read_data.split("    ")
                print(data)
                if ("connect", "username", "password", "host") == tuple(read_data.split("    ")):
                    print("Got the match of connect at position: ", position)
                    print("changing the current position to our position: ", file.tell(), position)
                    file.seek(position)
                    file.write('connect')



