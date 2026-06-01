
#String Matching in an Array

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]

        for i in words:
            for j in words:
                if i!=j and i in j:
                    result.append(i)
                    break
        return result

        