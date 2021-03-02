import re 

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):

. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

"""
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r"[A-Z][A-Z]")
matches = pattern.finditer(text_to_search)

with open("data.txt", "r") as infile:
    contents = infile.read()

#pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d")
#matches = pattern.finditer(contents)

for match in matches:
    print (match)