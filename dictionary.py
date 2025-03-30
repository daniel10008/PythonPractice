my_details = {"first_name": "Daniel", "Last_Name": "Ivron", "age": 14,
              "address": {"street_name": "Wyckoff", "county": "Bergin", "state": "New Jersy", "country": "USA",
                          "zipcode": "07482"},
              "education": {"grade": 9, "high_school_name": "ramapo", "major": "computer science"}}
# print(my_details)
# print(my_details.keys())
# print(my_details.get("address"))
# print(my_details.get("address").keys())
# print(my_details.get("address").values())
my_details.update({"hobbies":["fencing","piano","drawing"]})
# my_details.update({"age":15})
# print(my_details.items())

# for key in my_details.keys():
#     print(my_details.get(key))
#     if my_details.get("address") is not None:
#         my_details.get("address").update({"county":"pasaic"})
for key in my_details.keys():
    if type(my_details.get(key))== dict:
        for key2 in my_details.get(key).keys():
            print(key2,":",my_details.get(key).get(key2))
    elif type(my_details.get(key))==list:
        for i, value in enumerate(my_details.get(key)):
            print(i+1,":",value)
    else:
        print(key,":",my_details.get(key))

# my_details["Last_Name"] = "Evron"
# my_details.pop("age")
# my_details.popitem()
# my_details.clear()
# print(my_details)