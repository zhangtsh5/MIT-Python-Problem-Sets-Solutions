# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1,'*':0, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
#获取单词得分
def get_word_score(word, n):

    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_low=word.lower() #将单词转换成全小写
    word_length=len(word_low) #字母个数
    if word_length==0:  #单词为空字符串的情况
        return 0
    sum=0                 # component 1
    for key in word_low:
        sum+=SCRABBLE_LETTER_VALUES[key]
    temp=7*word_length-3*(n-word_length)
    second_com=max(1,temp)   # component 2
    
    score=sum*second_com     # 得分
    return score   


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    #将字典以一种更友好直观的方式输出
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3)) #向上取整

    for i in range(num_vowels-1): 
        x = random.choice(VOWELS) #获取随机元音字母
        hand[x] = hand.get(x, 0) + 1
    hand['*']=1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS) #获取随机辅音字母
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
            
        
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand=hand.copy()  #浅复制copy
    word_low=word.lower() #将单词全部转换成小写
    for x in word_low: #减去已经用掉的字母
        if x in new_hand and new_hand[x]>0:
            new_hand[x]-=1
    return new_hand
            

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand,word_list):

    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    
    
    
    word_low=word.lower()#word 转化为全小写 * 号不影响
    if '*' in word_low: #有*号的情况
        word_after=[]# 存储*号变成任一元音字母之后的结果
        word_arr=list(word_low)#将单词转换为数组形式，方便操作
        pos=word_arr.index('*') #找到 * 号的位置
        for i in range(5):#5个元音字母
            word_temp=word_arr
            word_temp[pos]=VOWELS[i] #将*号变成元音字母
            string_temp="" #用于将*号处理后的单词数组变成字符串形式
            word_after.append(string_temp.join(word_temp))
            
        #只要word_after中有一个字符串在word_list中，且满足后续条件，单词就是有效的
        flag=False
        for i in range(5):
            if word_after[i] in word_list:
                flag=True
        if not flag:
            return False
    #没有通配符情况
    elif word_low not in word_list:
        return False
    
    hand_array=[] #将hand转化成列表
    for key in hand:
        for i in range(hand[key]):
            hand_array.append(key)
    for x in word_low:
        #判断word 中字母是否都来自hand
        if x not in hand_array:
            return False
        
        else:#hand_array中减去已经用掉的字母
            pos=hand_array.index(x)
            hand_array[pos]='_'
    return True      
            

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    length=0
    for key in hand:
        length+=hand[key]
    return length
    

def play_hand(hand, word_list):
    
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    length=1 #赋大于0的初值，用于执行while循环
    total_score=0  #总分
    while length>=0:
        length=calculate_handlen(hand)
        if length==0: #hand中字符用光了的情况
            print("Ran out of letters. Total score: {} points".format(total_score))
            print("")
            break
        print("Current Hand: ",end=" ")
        display_hand(hand)
        print('Enter word, or "!!" to indicate that you are finished:',end=" ")
        word=input() #输入单词
        if word=="!!":#玩家结束游戏
            print("Total score: {} points".format(total_score))
            print("")
            break #输出总分后，跳出循环
        
        elif not is_valid_word(word,hand,word_list):
            #单词无效，继续下一次循环
            print("That is not a valid word. Please choose another word.")
            print("")
            hand=update_hand(hand,word) #更新hand
            continue
        
            
        temp_score=get_word_score(word,length) #当前单词得分
        total_score+=temp_score #该轮游戏总得分
        print('{} earned {} points. Total: {} points '.format(word,temp_score,total_score))
        print("") 
        hand=update_hand(hand,word) #更新hand
        

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    #随机获取一个新字母，用于替代
    new_letter=random.choice(VOWELS+CONSONANTS)
    #用户输入字符在hand中，则删除该键值对，并用new_letter替代
    if letter in hand:
        num=hand[letter] #先将数量保存起来
        del hand[letter] #删除要替代的键
        hand[new_letter]=num #添加新键值对，完成替换
        
    #letter不在hand中对hand 没有影响，所以无需操作，直接返回hand
    return hand  # 返回处理后的hand
    
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("Enter total number of hands:",end=" ")
    hand_number=int(input()) #hand 的数量
    sum_score=0 #玩hand_number次后的总得分
    sub_times=1 #替换hand中字母机会次数
    replay_times=1 #每一个hand都有一次重玩的机会
    flag_replay=False
    
    while hand_number>0:
        
        #用户选择重玩时不需要重新获取一个hand，非重玩时才需要重新随机获取hand
        if not flag_replay: 
            print("Please input a number as the size of the hand: ",end=" ")
            hand_size=int(input()) # hand中字符数量
            hand=deal_hand(hand_size) #获取一个随机hand，且字符数量为hand_size
        else: #重玩直接进行原来的hand,并更换状态，否则flag_replay=True 后会一直重玩一个hand
            flag_replay=False
            
        print("Current hand:",end=" ")
        display_hand(hand)
        if sub_times>0: #询问用户是否需要替换hand中某个字母
            print("Would you like to substitute a letter?",end=" ")
            ans=input() #用户回复
            #用户需要替换hand之中某个字母
            if ans=="yes":
                print("Which letter would you like to replace:",end=" ")
                letter=input()  #需要替换哪个字母
                hand=substitute_hand(hand, letter) #hand变成替换之后的hand
                sub_times-=1 #替换机会用掉
                print("")

        hand_init=hand #记录每个hand的初值，用于重玩
        #开始对每一个hand进行玩游戏过程
        length=1 #赋大于0的初值，用于执行while循环
        total_score=0  #总分
        total_score_first=0 #用于记录玩家重玩一个hand时第一次的得分,没有重玩则默认为0
        while length>=0:
            length=calculate_handlen(hand)
            if length==0: #hand中字符用光了的情况
                print("Ran out of letters. Total score for this hand:",total_score)
                print("----------")
                break
            print("Current Hand: ",end=" ")
            display_hand(hand)
            print('Please Enter word, or "!!" to indicate that you are finished:',end=" ")
            word=input() #输入单词
            if word=="!!":#玩家结束游戏
                print("Total score for this hand: ",total_score)
                print("----------")
                break #输出总分后，跳出循环
            
            elif not is_valid_word(word,hand,word_list):
                #单词无效，继续下一次循环
                print("That is not a valid word. Please choose another word.")
                print("")
                hand=update_hand(hand,word) #更新hand
                continue
            
            temp_score=get_word_score(word,length) #当前单词得分
            total_score+=temp_score #该word总得分
            print('{} earned {} points. Total: {} points '.format(word,temp_score,total_score))
            print("") 
            hand=update_hand(hand,word) #更新hand
        
        #当前hand结束后询问是否重新玩一次
        if replay_times>0:
            print("Would you like to replay the hand?",end=" ")
            ans_replay=input() #用户对于是否重玩hand的回复
            if ans_replay=="yes": #用户选择重玩
                total_score_first=total_score
                flag_replay=True
                hand=hand_init # hand复原，回到循环重新玩这个hand
                replay_times=0#重玩次数变为0
                continue
        #取两次得分中高的，如果hand只玩了换一次，则total_score_first为0，不影响总分计算
        total_score=max(total_score,total_score_first) 
            
        hand_number-=1 #一个hand结束
        sum_score+=total_score #所有hand的总分
    print("Total score over all hands:",sum_score) #输出本轮所有hand的总分
    
    

   
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
