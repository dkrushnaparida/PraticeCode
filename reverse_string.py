def reverse_string(st):
    reverst_val = ""
    index = len(st)-1   # Start from the last character
    
    while index >=0:
        reverst_val += st[index]
        index -=1

    return reverst_val

print(reverse_string("Dwiti krushna"))


##reverse the characters within each word, but the position of the words remains the same.

def reverse_each_word(sentence):
    words = sentence.split(" ")  # Split the sentence into words
    reversed_words = []          # List to hold reversed words

    for word in words:
        reversed_word = ''       # Manually reverse each word
        for i in range(len(word)-1, -1, -1):
            reversed_word += word[i]
        reversed_words.append(reversed_word)

    return ' '.join(reversed_words)  # Join words with space


print(reverse_each_word("Dwiti krushna"))