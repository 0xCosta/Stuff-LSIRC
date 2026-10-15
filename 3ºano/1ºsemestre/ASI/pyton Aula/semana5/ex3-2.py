import re

str="Isto E um Teste"

pattern = re.compile(r'[a-z]')
str2 = pattern.findall(str)
print (len(str2))
