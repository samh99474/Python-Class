parameters = [{"userName": "jj","userId":1}, {"userName": "sam","userId":2}]

for info in parameters:
    print("info: {}".format(info["userName"]))
    for info_dict, info_dict_value in info.items():
        print("info_dict: {}".format(info_dict))
        print("info_dict_value: {}".format(info_dict_value))
                    




