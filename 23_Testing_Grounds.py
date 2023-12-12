import json

provinces_list = []

municipality_list = []


with open("countries-data.json") as data_file:
    data = json.load(data_file)

    # print(data["countries"][0]["provinces"][0]["name"])

    provinces = data["countries"][0]["provinces"][0:5]

    for province in provinces:
        provinces_list.append(province["name"].upper())

        # for municipality in province["municipalities"]:
        #     # municipality_list.append(municipality["name"].upper())
        #     print(municipality)


print(provinces_list)
# print(municipality_list)

num = input("Enter a number:\n")

n = int(num)

a = ["1", "2", "3", "4", "5", "6", "7", "8",
     "9", "10", "11", "12", "13", "14", "15"]

if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
