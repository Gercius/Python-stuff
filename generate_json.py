# monstrosity for generating json

# import random
# import string

# # generate random string, k = string length
# def randomStr():
#     return ''.join(random.choices(string.ascii_lowercase, k=10))

id = "\"id\": "
title= "\"title\": "


with open('stuff.json', 'w') as file:
    file.write(
        f"[\n\t{{\n\t\t{id}{str(1)},\n\t\t{title}\"1st item\"\n\t}},\n"+
        f"\t{{\n\t\t{id}{str(2)},\n\t\t{title}\"2nd item\"\n\t}},\n"+
        f"\t{{\n\t\t{id}{str(3)},\n\t\t{title}\"3rd item\"\n\t}},\n"
    )
    for x in range(4, 50):
        file.write(
            f"\t{{\n\t\t{id}{str(x)},\n\t\t{title}\"{str(x)}th item\"\n\t}},\n"
        )
    file.write("]")
                             
  


