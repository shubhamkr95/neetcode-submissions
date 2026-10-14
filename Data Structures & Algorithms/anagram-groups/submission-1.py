class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        check_anagram = {}
        
        for i,word in enumerate(strs):
            sort_temp = ''.join(sorted(word))

            if sort_temp in check_anagram:
                check_anagram[sort_temp].append(word) 
            else:
                check_anagram[sort_temp] = [word]

        return list(check_anagram.values())
        