# looper program
# Ashton Pankey
# 09/15/2024

# creates a list of strings and prints it
sentences = ["rewriting programs","stepping on a lego","repacking parachutes","checking specific impulse","seting gravitational acceleration to zero", "adding k to every word","combobulating discombobulator"]
print(sentences)
# creates an empty string called new_sentences
new_sentence = []
# has two for loops, the first to go through each string in the list, and the second is nested to go through each character in the strings and removes all vowels (other than y)
for i in sentences:
    sentence = i
    for v in "aeiouAEIOU":
        sentence = sentence.replace(v,"")
    # adds the modified strings to the new list
    new_sentence.append(sentence)
# prints the new string
print(new_sentence)