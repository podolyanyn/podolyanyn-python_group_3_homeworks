enter_sent = input("Enter sentence: ")

words = []
current_word = ""


for char in enter_sent:
    if char != " ":
        current_word += char

    elif current_word != "":
         words.append(current_word)
         current_word = ""

if current_word != "":
    words.append(current_word)

word_count = {}

for word in words:

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)