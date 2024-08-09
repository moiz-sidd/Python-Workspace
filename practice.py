# name ="moiz"
# friend = "harry"
# apple = '''he said,
# hi harry
# I am a good boy
# "I want an apple'''

# print("hello, " + name)

# for character in apple:
#     print(character)
# fruit = "mango" 
# len1 = len(fruit)
# print("mango is a",len1,
# "letter word.")
# nm = "fawad"
# print(nm[-4:-2])

#string are immutable
a = "Harry !!!!!!! Harry Harry!!!"
print(len(a))
#uppercase()
print(a.upper())
#lowercase()
print(a.lower())
#rstrip()
print(a.rstrip("!"))
#replace()
print(a.replace("Harry", "Moiz"))
#capitalize
blogHeading = "introduction to python"
print(blogHeading.capitalize())
#center()
str1 = "Welcome to the gamming zone "
print(str1.center(50))
#count()
print(a.count("Harry"))
#endswith
print(a.endswith("!!!"))
str2 = "Welcome to the console !!!"
print(str2.endswith("to", 4, 10))
#find()
str3 = "he's name is Dan. He is an honest man. "
print(str3.find("is"))
#isalnum()
str4 = "WelcomeToTheclub7"
print(str4.isalnum())
#isalpha
str5 = "Welcome"
print(str5.isalpha())
#islower
str6 = "hellow world"
print(str6.islower())
#isprintable
str7 = "We wish you Eid Mubarak"
print(str7.isprintable())
#isspace
str8 = "             "
print(str8.isspace())
str9 = "                "
print(str9.isspace())
#istitle
str10 = "To kill a Mocking bird"
print(str10.istitle())
#startswith
print(a.startswith("H"))
#swapcase
str11 = "We Wish You Eid Mubarak"
print(str11.swapcase())
#title()
str12 = "his name is Dan. He is an honest man. "
print(str12.title())