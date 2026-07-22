class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictr={}
        for i in strs:
            keyr="".join(sorted(i))
            if keyr not in dictr:
                dictr[keyr]=[]
            dictr[keyr].append(i)
        return list(dictr.values())
        