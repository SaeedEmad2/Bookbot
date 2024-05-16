def main():
    book_path="books/frankenstein.txt"
    text=get_book_text(book_path)
    num_words=get_num_words(text)
    dulicat_count= duplic(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    list_ofdic =to_list(dulicat_count)
    print_character_counts(list_ofdic)
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def duplic(text):
    lower_str =text.lower()
    dic={}
    for let in text:
        if let in dic:
            dic[let]+=1
        else:
            dic[let]=1
    return dic

def sort_on(d):
    return d["count"]

def to_list(dic):
    dic_lis = [] 
    for c , count in dic.items():
        if(c.isalpha()):
            dic_lis.append({"character": c  , "count": count})
    dic_lis.sort(reverse = True , key=sort_on )
    return dic_lis


def print_character_counts(char_counts_list):
    for char_count in char_counts_list:
        print(f"The '{char_count['character']}' character was found {char_count['count']} times")
        
main()

    
