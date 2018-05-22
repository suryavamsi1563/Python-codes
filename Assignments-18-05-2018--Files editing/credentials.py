import os
list_dir = os.listdir(".")
print(list_dir)
for file_name in list_dir:
    if file_name.endswith(".txt"):
        with open(file_name, 'r') as file:
            file_data = file.readlines()
        print(file_data)
        credential_index = 0
        for x in file_data[:]:
            if x.startswith("credentials"):
                credential_index = file_data.index(x)
                print(credential_index)
                file_data.pop(credential_index)
                continue
            if file_data.index(x) in range(credential_index, credential_index + 3):
                if x.startswith("    "):
                    file_data.pop(file_data.index(x))
        print(file_data)
