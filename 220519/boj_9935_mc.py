info_dict = {}


for i in range(3):
    if info_dict.get(1):
        info_dict[1].append(["world"])
    else:
        info_dict[1] = ["hello"]

