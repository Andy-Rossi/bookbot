def get_book_wordcount(a_book_text):
    word_list = a_book_text.split()
    wordcount = len(word_list)
    return wordcount

def count_characters(string):
    string = string.lower() #converts every letter to be lowercase
    character_dict = {}
    for char in string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def get_sorted_dicts(dict):
    #creates a sorted list of multiple dictionaries based on the input dictionary and its number.
    #one dictionary for each key.
    #each dictionary will have one key and one number paired with the key.
    sorted_dicts = []
    for key in dict:
        sorted_dicts.append({"char":key,"num":dict[key]})
    #print(sorted_dicts) #not sorted yet

    #print("============ test ============")    
    def sort_on(dict):
        return dict["num"]
    sorted_dicts.sort(reverse=True, key=sort_on)
    #print(sorted_dicts)

    return sorted_dicts