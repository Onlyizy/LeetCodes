class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        else:
            i=0
            j=0
            ref=""
            for word in strs:
                ref = ref + word
            for i in range(len(strs)):
                if len(strs[i])<=len(ref):
                    ref=strs[i]
                else:
                    ref=ref
            for word in strs:
                j=0
                while j<len(ref) and j<len(word):
                    if ref[j]==word[j]:
                        j=j+1
                    else:
                        ref=ref[:j]
                        j=j+1
            return ref
