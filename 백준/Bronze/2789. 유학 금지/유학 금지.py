word = input()
text = ['C','A','M','B','R','I','D','G','E']

for i in text:
    word = word.replace(i, '')

print(word)