# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    #长度为1 递归截止条件
    if len(sequence)==1:
        return [sequence]
    
    result=[] #储存返回的结果
    for i in range(len(sequence)):
        # 每次取出i位置元素
        string_temp=sequence[:i]+sequence[i+1:] # 剩下元素组成的新字符串
        # 剩下元素的全排列 （列表）
        perm_after=get_permutations(string_temp)
        for x in perm_after:
            #将取出的元素放到字符串最前面，再添加到结果返回列表中
            result.append(sequence[i]+x)
    return result    
    
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''


    

if __name__ == '__main__':
    case=3
    example_input = ['abc','cd','x']
    expected_output=[
                        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],
                        ['cd','dc'],
                        ['x']
                    ]
    for i in range(case):
        print('Input:', example_input[i])
        print('Expected Output: ',expected_output[i])
        print('Actual Output:', get_permutations(example_input[i]))
        print("")
        
    
    #print(get_permutations('abc'))
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))
        
    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a 
    #    sequence of length n)
    
        

