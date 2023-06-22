

sentence = input("Please enter a sentence: ")
brokenletters = ""

for char in sentence:
    if char in ["y","p","c","d","t","f","a","e","z"]:
        continue
    else:
        brokenletters += char

    print(brokenletters)