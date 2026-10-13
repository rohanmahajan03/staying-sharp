from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array: [0]*26
        #array ord(curr) - ord(a) += 1
        letters_to_words = defaultdict(list)
        for word in strs:
            arr = [0]*26
            for curr in word:
                arr[ord(curr) - ord("a")] += 1
            letters_to_words[tuple(arr)].append(word)
        
        grouped_anagrams = []
        for l in letters_to_words:
            grouped_anagrams.append(letters_to_words[l])
        return grouped_anagrams

