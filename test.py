

str_list = [1,2,3,4,"test",5,6,"test",7,8]
for i in range(len(str_list) -1, -1, -1):
    if "test" in str(str_list[i]):
        str_list.remove(str_list[i])

print(str_list)
# print(str_list[-7:])