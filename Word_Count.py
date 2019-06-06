#!/usr/bin/env python3

def word_stats(file_directory, num):

    f = open(file_directory, "r")
    contents = f.read()
    list_of_things_in_txt = list(contents) #puts all the separate letters into a list

    list_of_characters = []
    for char in list_of_things_in_txt:
        if char.isalnum() or char == " ": #if its a letter or number or space, append to new list
            list_of_characters.append(char.lower())
    
    all_words = ("".join(list_of_characters)) #join them back together as words using space as separator
    
    all_word_list = all_words.split(" ") #split them back again into a list of actual words

    count = {}
    for word in all_word_list:
        count[word] = count.get(word, 0) + 1 #dictionary to count the occurence of each word

    sorted_descending_dictionary = sorted(count.items(), key=lambda x: x[1], reverse=True) #sort dictionary by descending order
    return sorted_descending_dictionary[0:num] #return top 5 by splicing

if __name__ == "__main__":
    print(word_stats("/Users/AaronKo/w1d2/article.txt", 5))
