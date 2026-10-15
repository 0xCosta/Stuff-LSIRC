import re

str="O real teste de sistemas"

pattern = re.compile(r'[A-Z\s]*')
str2 = pattern.sub('',str)
print (str2, len(str2))
