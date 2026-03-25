x = 10
y = 5
print("Is x greater than y?", x > y)
my_list = ["Nash", "Ericka", "Mark", "Rian", "Micah", "JC", 19, True]
print("My List:", my_list)

my_tuple = ("Nash", "Ericka", "Mark", "Rian", "Micah", "JC", 19, True)
print("My Tuple:", my_tuple)

my_set = {"Nash", "Ericka", "Mark", "Rian", "Micah", "JC", 19, True}
print("My Set:", my_set)

my_dict = {
    "Nash": 19,
    "Ericka": 19,
    "Mark": 19,
    "Rian": 19,
    "Micah": 19,
    "JC": 19,
    "is_student": True
}
print("My Dictionary:", my_dict)

if "JC" in my_list:
    print("JC is in the list: True")
else:
    print("JC is in the list: False")

if my_dict["Nash"] == 19 and my_dict["Ericka"] == 19:
    print("All of us are 19 years old: True")
else:
    print("All of us are 19 years old: False")
