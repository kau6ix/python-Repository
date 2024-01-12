# get sentence from user

original=input("Please enter you favourite sentence :) ").strip().lower()

# split sentence into words

words=original.split()

#loop through words and convert to pig latin
new_words=[]

for word in words:
    #print(word)
    if word[0] in "aeiou":
        new_word=word+"yay"
        new_words.append(new_word)
    else:
        vowel_pos=0
        for i in word:
            if i not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break
        cons=word[:vowel_pos]
        therest=word[vowel_pos:]
        new_word=therest+cons+"ay"
        new_words.append(new_word)

output=" ".join(new_words)
print(output)
            
#print(new_words)

# if starts with vowel, just add "Yay"

#otherwise, move the first consonant cluster to end and add "ay"

#stick words back together

# Output the final String
