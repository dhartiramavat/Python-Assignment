'''Write a python program to find the longest words. '''
sentence = "my self dharti ramavat."
words = sentence.split()
longest = ""
for i in words:
    if len(i) > len(longest):
        longest = i
print("Longest word:", longest)