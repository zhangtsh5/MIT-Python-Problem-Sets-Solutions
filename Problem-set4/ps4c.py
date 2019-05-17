# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
    
    def get_message_text(self):
        return self.message_text


    def get_valid_words(self):
        return self.valid_words[:]

        
     #建立映射字典         
    def build_transpose_dict(self, vowels_permutation):
        # 字典键  原文字母
        plain=VOWELS_LOWER+VOWELS_UPPER+CONSONANTS_LOWER+CONSONANTS_UPPER
        #字典值   密文对应位置的字母
        cipher=vowels_permutation.lower()+vowels_permutation.upper()+CONSONANTS_LOWER+CONSONANTS_UPPER
        
        return {plain[i]: cipher[i] for i in range(len(plain))}


        
        
    #加密消息
    def apply_transpose(self, transpose_dict):
        text = self.message_text #原文
        ciphertext = [] #密文
        #字符逐个映射
        for ch in text:
            #返回指定键的值  不存在则返回key本身
            ciphertext.append(transpose_dict.get(ch,ch))
        return "".join(ciphertext)

        
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self, text)
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        

    def decrypt_message(self):
        #获取全排列
        perms = get_permutations(VOWELS_LOWER)
        max_counter = 0 #最大有效单词数量
        decrypt_msg = "" #解密后明文
        for perm in perms:
            temp_dict = self.build_transpose_dict(perm)
            temp_text = self.apply_transpose(temp_dict).split()
            counter=0 #计算有效单词数量
            for j in temp_text:
                if is_word(self.valid_words, j):
                    counter += 1
            #更新max_counter值  并且更新解密后明文
            if counter > max_counter:
                max_counter = counter
                
                decrypt_msg = self.apply_transpose(temp_dict)
        return decrypt_msg

        
        

        
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print("")
     
    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage("Quite easy!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Qiuta aosy!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print("")
    
    message = SubMessage("Follow your heart!")
    permutation = "uoiea"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Fellew year hourt!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

