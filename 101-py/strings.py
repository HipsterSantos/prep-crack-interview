"""Unicode and scape sequences ASCII representation"""

print("\333 this octal number")
print("\x3434333 this is decimal number")
print("\b3333 this a binary one")

unicode_a = '\N{LATIN SMALL LETTER A}'
print(unicode_a)

print('a\n\tb')

#strtings methods 

nothing = "".join(["hey","nomade","element","heaaer"])
nothing += "::".join("homer")
empty = "".join(['hey jessica','how you\'re  doing '])
empty +="".join("hey jessica how you're doing ")
print(empty)

"""time to split """
splitted = nothing.split('::')
#quick test with splits 
toSplit = 'this is a test'
# splitted = (toSplit.split(' '))+"-".join('this is a test')
# print(splitted) printing system whitespaces

import string 
print(string.whitespace)

