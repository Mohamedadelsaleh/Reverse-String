while True:
    text = input("Enter Your String : ").strip()
    if text.isalpha():
        text = str(text)
        break


def reverseText(userText):
    userText = userText[::-1]
    return userText


myNewText = reverseText(text)
print(myNewText)