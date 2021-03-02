import re

s = "11XXbybcbybXX22"

#m = re.search(r"(.*)(b.b)c\2\1", s)
#if m:
 #   print("group(0): ", m.group(2))
#else:
 #   print ("No")

#pattern = re.compile(r"(.*)(b.b)c\2\1")
#match = pattern.finditer(s)

#for matches in match:
   # print (matches)


#print (re.search (r"B(CdE)F", "AbcDefG").group(1))

print("Found multiple occurrence of: ", re.search 
(r"(\b\w+\b).*\b\1\b", "one two three four five\ndrei tre tres three trois", re.S)
.group(1))

#cdc= re.findall(r"[A-Z](\d)[A-Z]")

sla = "This is complicated"

slb = re.sub("complicated", "easy", sla)
print (slb)

s2 = "1 < 2 < 3 < 4 < 5"
(s2, num) = re.subn("<", ">", s2)
print (num)

#print(r'a(.*)b\1c',   'yes' if re.search(r'a(.*)b\1c', s)   else 'no')

s1 = "Firstname: Peter, Secondname: Ngure"
s2 = re.sub (r"Firstname: (\w+), Secondname: (\w+)", "Firstname: \g<2>, Secondname: \g<1>", s1)
print (s2)

s = "This almost-a-sentence is to be split"
wrd = re.split (r"\s| +",s)
print (wrd[3])

together = "-".join (wrd)
print (together)