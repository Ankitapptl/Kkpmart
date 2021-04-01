import re

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "https://blog.microsoft.com/test.html"
#x = re.sub("(https?:\/\/)?([w]{3}\.)?(\w*.\w*)([\/\w]*)", "JIGAR", txt)

exp = "^(?:https?:)?(?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)"

x = re.sub(exp, "", txt)

print(x)
