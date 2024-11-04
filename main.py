def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    #print(file_contents);
    #print(count_all_chars)
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(text)} words found in the document \n")
    count_characters(text)
    print(f"--- End report ---")

# recup le contenu du livre
def get_text(path):
    with open(path) as f:
        return f.read()

#compte le nombre de mots dans le livre
def count_words(text):
    words = text.split()
    #return len(words)
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

#compte le nombre de fois que chaque caractere apparait dans le livre
def sort_on(dict):
    return dict["num"]

def count_characters(text):
    list_char = {}
    char_list = []
    for characters in text:
        lowered_char = characters.lower()
        if lowered_char.isalpha():
            if (lowered_char not in list_char):
                list_char[lowered_char] = 1
            else:
                list_char[lowered_char] +=1
    
    #print(f"imprime la liste: {list_char}")

    for char, count in list_char.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    #return list_char
    for item in char_list:
        print(f"The {item['char']} character was found {item['num']} times")
    
main()