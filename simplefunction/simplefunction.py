
def countVowels(word):
    count = 0;
    for i in range(len (word)):
        if (word[i]=="a" or word[i] == "e" or word[i]=="i" or word[i] =="o" or word[i]=="u"):
            count+=1
    return count
def countConsonants(word):
    count = 0;
    for i in range(len (word)):
        if not (word[i]=="a" or word[i] == "e" or word[i]=="i" or word[i] =="o" or word[i]=="u"):
            count+=1
    return count


def countletters(word):
   return print (countConsonants(word)+ countVowels(word))

countletters("bonjour")

