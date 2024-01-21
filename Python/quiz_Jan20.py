sample_text = "The first parameter is the required variables in this function."

words = sample_text.split()
# print(words)

for word in words:
    if len(word) <= 5:
        words.remove(word)
        
print(words)