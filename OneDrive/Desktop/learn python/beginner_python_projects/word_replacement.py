#Word replacement program 
def replace_word():

    str = "hi guys. I am Susan. And hi hi hi"
    word_to_replace = input("Enter word to replace: ")
    word_replacement = input("Enter word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()

