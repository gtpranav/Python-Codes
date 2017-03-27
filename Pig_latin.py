#get sentence from user
sentence = raw_input().strip().lower()

#slit it into words
words = sentence.split()

#loop through words
new_words = []
for word in words:

    if word[0] in 'aeiou':
        new_word = word + 'yay'
        new_words.append(new_word)
        #print new_words
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos += 1
            else:
                break;
        cons = word[:vowel_pos]
        vowel = word[vowel_pos:]
        new_wordl = vowel + cons + 'ay'
        new_words.append(new_wordl)
output = " ".join(new_words)
print output
