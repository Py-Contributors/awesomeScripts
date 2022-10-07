import wikipedia

prompt = input("Please enter the topic for search: ")
numSentences = int(input("Please enther the number of sentences to search: "))
print(wikipedia.summary(prompt, sentences=numSentences))
