import re

str="O real teste de sistemas"

pattern = re.compile(r'[a-z]')
str2 = pattern.findall(str)
print (len(str2))
