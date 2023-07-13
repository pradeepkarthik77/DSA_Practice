class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for word in strs:

            temp = word

            arr = []

            for i in word:
                arr.append(i)
            
            arr.sort()
            string = "".join(arr)
            if map.get(string,0.1) == 0.1:
                map[string] = [temp]
            else:
                map[string].append(temp)

        arr = []

        for item in map.values():
            arr.append(item)
        
        return arr
