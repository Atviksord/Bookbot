

def Main():
    path = 'books/frankenstein.txt'
    booklist = GetBook(path)
    letterdict= CountLetters(booklist)
    mydic = ShowLetters(letterdict)
    mydic.sort(reverse = True)
    print(f' -- Begin report of {path} ---')
    print(f'{CountWords(booklist)} words found in the document')
    print('-------------------------------------------------------')
    for entry in mydic:
        print(entry)
    

def CountWords(text):
    return len(text)


def GetBook(path):
    with open(path) as f:
        file_contents = f.read().lower()
        BookList = file_contents.split()
        return BookList

def CountLetters(text):
    CharDict = {}
    characters_list = [char for word in text for char in word]
    for letter in characters_list:
        if letter not in CharDict and letter.isalpha():
            CharDict[letter] = 1
        elif letter in CharDict:
            CharDict[letter] += 1
    return CharDict

def ShowLetters(letterdict):
    keylist = []
    for key in letterdict:
        keylist.append(f' The {key} character was found {letterdict[key]} times')
    keylist.append('--- End of report ---')
    return keylist
    
        

    



   

Main()
