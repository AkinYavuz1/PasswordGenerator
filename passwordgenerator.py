import random

with open('C:\Python Projects\Password Generator\Random Words.txt','r') as f:
    content = f.readlines()

wordlist = [x.strip().capitalize() for x in content]

for words in range(3):
    print(random.choice(wordlist), end = "")


input("\nPress Enter to close.")