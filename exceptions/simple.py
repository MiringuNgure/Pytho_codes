def countletters(word):
    result = len (word)
    if result > 5:
        raise Exception ("The passcode is too long: ", result)
    print ("passcode is okay")

Passcode = input("Enter a new passcode: ")

try:
    countletters(Passcode)
except Exception as e:
    print(e)
