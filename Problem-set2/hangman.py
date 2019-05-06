# Problem Set 2, hangman.py
# Name: zhangtieshan/15352418
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist=load_words()


#判断玩家猜测是否正确
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    list_secret=list(secret_word)
    #只要目标中出现一个字母不在玩家猜测结果中，返回False,都在的话，返回True
    for i in list_secret:
        if i not in letters_guessed:
            return False
    return True


#获取玩家已猜对字母
def get_guessed_word(secret_word, letters_guessed):
                
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    length=len(secret_word)
    list_secret=['_ ']*length #列表元素先全部初始化为'_'
    for i in letters_guessed:
        for j in range(length): 
            if i==secret_word[j]: #用猜对的字母替换掉对应位置的'_'
                list_secret[j]=secret_word[j]
    
    string="".join(map(lambda x:str(x),list_secret)) #列表转字符串
    return string
  


#获取剩余可猜测字母范围
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    #初始化可猜字母为全部小写字母
    letters_all="abcdefghijklmnopqrstuvwxyz"
    for i in letters_all:
        if i in letters_guessed: #如果玩家已经猜过 i 则将其替换为'_ '
            letters_all=letters_all.replace(i,'')
    return letters_all
   
 
    

def hangman(secret_word):
    list_unique=[] #用于secret_word去重
    for i in secret_word:
        if i not in list_unique:
            list_unique.append(i)
    unique_numbers=len(list_unique) #目标单词中不同字符的数量，用于计算玩家分数
    vowels="aeiou" #元音字母
    print("Welcome to the game hangman!")
    length=len(secret_word) #目标单词长度
    print("I'm thinking of a word that is {} letters long!".format(length))
    times_left=6 #玩家剩余猜测次数
    warning_left=3 #玩家剩余警告次数
    print("You have {} warnings left.".format(warning_left))
    print("------------- ")
    list_guessed=[]
    while times_left>0: #玩家猜测次数没用完
        print("You have {} guesses left.".format(times_left))
        print("Available letters:",get_available_letters(list_guessed))
        char=input("Please guess a letter:")
        x=str.lower(char)
        if x in list_guessed:#玩家已经猜过这个字母
            if warning_left>0:  #警告次数没用完
                warning_left-=1
                print("Oops! You've already guessed that letter.You have {} warnings left:".format(warning_left),get_guessed_word(secret_word,list_guessed))
            else:           #警告次数为0了 减少猜测次数
                times_left-=1
                print("Oops! You've already guessed that letter.You have no warnings left,so you lose one guess:",get_guessed_word(secret_word,list_guessed))
            
        else: #玩家尚未猜测过这个字母
            list_guessed.append(x) #先存储玩家猜测结果
            if not str.isalpha(x): #玩家输入不是是字母
                if warning_left>0:
                    warning_left-=1
                    print("Oops!That is not a valid letter.You have {} warnings left:".format(warning_left),get_guessed_word(secret_word,list_guessed))
                else:
                    times_left-=1
                    print(" Oops! That is not a valid letter. You have no warnings left,so you lose one guess:",get_guessed_word(secret_word,list_guessed))
            #玩家输入是字母时
            elif x in secret_word:#玩家猜测字母在目标中
                print("Good guess:",get_guessed_word(secret_word,list_guessed))
                # 玩家猜出全部字母
                if secret_word==get_guessed_word(secret_word,list_guessed):
                    print("------------- ")
                    print("Congratulations, you won!")
                    total_score=times_left*unique_numbers
                    print("Your total score for this game is:",total_score)
                    return 
            else: #玩家猜测字母不在目标中
                print("Oops! That letter is not in my word.",get_guessed_word(secret_word,list_guessed))
                if x in vowels: #没有猜中，且是元音字母
                    times_left-=2
                else:
                    times_left-=1 
        print("------------- ")
    print("Sorry, you ran out of guesses.The word was {}".format(secret_word)) #玩家失败，游戏结束
    return 
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def del_space(string): #将字符串去除空格后转化成列表
    lst=[]
    for i in string:
        if i!=' ':
            lst.append(i)
    return lst
        


#检验两个单词是否按规则匹配
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
     #先将字符串转换成列表，方便操作
    list_my_word=del_space(my_word)
    list_other_word=list(other_word)
    if len(list_my_word)!=len(list_other_word): #长度不一致
        return False
    else:
        length=len(list_my_word)
        for i in range(length): #对应位置均是字母且不相等
            if list_my_word[i]!='_' and list_my_word[i]!=list_other_word[i]:
                return False
        #list_my_word[i]=='_'时
        for i in range(length): 
            j=i+1
            for j in range(length):
                if list_other_word[i]==list_other_word[j] and list_my_word[i]!=list_my_word[j]:
                    return False
    return True


def show_possible_matches(my_word):
        
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    flag=0 #用于标记是否存在可能匹配的单词
    possible_word=[] #存储可能匹配的单词
    for i in wordlist:
        if match_with_gaps(my_word,i):
            flag=1
            possible_word.append(i)
    if flag==0:#不存在可能匹配的单词
        print("No matches found.")
    else:
        print("Possible word matches are:")
        for i in possible_word:
            print(i,end=' ')
    print("")
    




def hangman_with_hints(secret_word):
    list_unique=[] #用于secret_word去重
    for i in secret_word:
        if i not in list_unique:
            list_unique.append(i)
    unique_numbers=len(list_unique) #目标单词中不同字符的数量，用于计算玩家分数
    vowels="aeiou" #元音字母
    print("Welcome to the game hangman!")
    length=len(secret_word) #目标单词长度
    print("I'm thinking of a word that is {} letters long!".format(length))
    times_left=6 #玩家剩余猜测次数
    warning_left=3 #玩家剩余警告次数
    print("You have {} warnings left.".format(warning_left))
    print("------------- ")
    list_guessed=[]
    while times_left>0: #猜测次数没没有用完时
        print("You have {} guesses left.".format(times_left))
        print("Available letters:",get_available_letters(list_guessed))
        char=input("Please guess a letter:")
        x=str.lower(char)
        if x in list_guessed:#玩家已经猜过这个字母
            if warning_left>0: 
                warning_left-=1
                print("Oops!You've already guessed that letter.You have {} warnings left:".format(warning_left),get_guessed_word(secret_word,list_guessed))
            else:           #警告次数为0了 减少猜测次数
                times_left-=1
                print("Oops! You've already guessed that letter.You have no warnings eft,so you lose one guess:",get_guessed_word(secret_word,list_guessed))
            
        else: #玩家尚未猜测过这个字母
            list_guessed.append(x) #先存储玩家猜测结果
            if x=='*': #是 '*' 的情况
                my_word=get_guessed_word(secret_word,list_guessed)
                show_possible_matches(my_word)
            elif not str.isalpha(x): #玩家输入不是是字母且不是 * 号
                if warning_left>0:
                    warning_left-=1
                    print("Oops!  That is not a valid letter.You have {} warnings left:".format(warning_left),get_guessed_word(secret_word,list_guessed))
                else:
                    times_left-=1
                    print(" Oops! That is not a valid letter.You have no warnings left,so you lose one guess:",get_guessed_word(secret_word,list_guessed))
            #玩家输入是字母时
            elif x in secret_word:#玩家猜测字母在目标中
                print("Good guess:",get_guessed_word(secret_word,list_guessed))
                # 玩家猜出全部字母
                if secret_word==get_guessed_word(secret_word,list_guessed):
                    print("------------- ")
                    print("Congratulations,you won!")
                    total_score=times_left*unique_numbers
                    print("Your total score for this game is:",total_score)
                    return
            else: #玩家猜测字母不在目标中
                print("Oops! That letter is not in my word.",get_guessed_word(secret_word,list_guessed))
                if x in vowels: #没有猜中，且是元音字母
                    times_left-=2
                else:
                    times_left-=1 
        print("------------- ")
    print("Sorry,you ran out of guesses.The word was {}".format(secret_word)) #玩家失败，游戏结束
    return 
  


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word=choose_word(wordlist)
    hangman(secret_word)
    
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints("apple")
