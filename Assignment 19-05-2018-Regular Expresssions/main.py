import re
with open('facebook.txt', 'r') as file:
    file_data = file.readlines()
login_count = 0
comments_count = 0
ip_addrs_list = []
print(file_data)
login_pattern = re.compile(r'^login\sfrom\s([0-9]{3}\.[0-9]{3}\.[0-9]\.[0-9]{3})')
comments_pattern = re.compile(r'^comments\sfrom\s[0-9]{3}\.[0-9]{3}\.[0-9]\.[0-9]{3}')
for x in file_data:
    login_result = login_pattern.search(x)
    if login_result:
        ip_addrs_list.append(login_result.group(1))
        login_count += 1
    if comments_pattern.search(x):
        comments_count += 1
print("Total Login counts in a day: ", login_count)
print("Total unique login's in a day: ", len(set(ip_addrs_list)))
print("Total comments counts in a day: ", comments_count)


def no_of_likes_ip(ip_addrs,file_data):
    likes_cnt = 0
    likes_pattern = re.compile(r'^like\sfrom\s([0-9]{3}\.[0-9]{3}\.[0-9]\.[0-9]{3})')
    for x in file_data:
        likes_result = likes_pattern.search(x)
        if likes_result and likes_result.group(1) == ip_addrs:
            likes_cnt += 1
    print("No of likes from the ip-address "+ip_addrs+" : ",likes_cnt)


no_of_likes_ip("192.155.1.111", file_data)
