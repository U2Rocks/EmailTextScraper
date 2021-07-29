#Email Address Text Scraper
#escape or unescape characters in patterns if wierd errors
import re

text = " random string. My_Nam-e1-23@website.com. some more random text. YourName.8_8_8@company.net"

pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

result = pattern.findall(text)

print(result)