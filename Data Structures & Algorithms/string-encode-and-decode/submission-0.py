class Solution:

    def encode(self, strs: List[str]) -> str:
     string = ''

     '''
     ["hello", "world"]
     length of array 2
     string += 5 + # 
     '''
     for i in range(len(strs)):
        string += repr(len(strs[i])) + "#" 
        '''
            k = 0
            strs[0] = hello
            k loop through hello
            string = 5# 
            string += h
        '''
        for k in range(len(strs[i])):
         string += strs[i][k]

     return string

    '''
       res = [], i = 0 
    '''
    def decode(self, strs: str) -> List[str]:
        res, i = [], 0 
        '''
         while  i < len(s) -> 14 5#hello5#world
         j = i -> j = 0
        '''
        while i < len(strs):
          j = i   

          '''
            j = 0 , so at index 0 is 5
            j = 1, so index 1 is # loop breaks
          '''   
          while strs[j] != '#':
            j += 1

          '''
            5 # h e l l o 
            0 1 2 3 4 5 6
            length = strs[0:1] -> 5  so length = 5      
            slice from 0 to < 1 so it will be index 0 and value is 5
          '''   
          length = int(strs[i:j]) 
          '''
            strs[j+1 -> J is at index 1 : j + 1 + length -> 1+1 + 5
            strs[2: 7]
          '''
          res.append(strs[j+1: j+1 + length])
          '''
            i = 1 + 1 + 5 
            5 # H e l l o 5 # w o r l d 
                          i
            so i will be set to index 7
          '''
          i = j + 1 + length

        return res
        
