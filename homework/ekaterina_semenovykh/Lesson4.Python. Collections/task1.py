my_dict = {}
my_dict["tuple"] = ("Sasha", "Kim", 25, "student", 36.6)
my_dict["list"] = [5, 3, 2.8, 3.15, False, "Good"]
my_dict["dict"] = {"weight": 75, "height": 170, "hair colour": "brown", "eyes": "blue", "email": "alex@example.com"}
my_dict["set"] = {"PE", "Maths", "Chemistry", "Ecology", "Biology"}
print(my_dict["tuple"][-1])
my_dict["list"].append("Passed")
my_dict["list"].pop(1)
my_dict["dict"][("i am a tuple",)] = True
my_dict["dict"].pop("eyes")
my_dict["set"].add("Computer Science")
my_dict["set"].pop()
print(my_dict)
