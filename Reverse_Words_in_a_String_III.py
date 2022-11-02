def reverse(sentence):

    words = sentence.split(" ")
    
   
    reversed_words = [w[::-1] for w in words]
    
    
    new_sentence = " ".join(reversed_words)
    
    print(new_sentence)

sentence=input()
reverse(sentence)