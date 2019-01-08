class Solution:
    def mostCommonWord(self, paragraph,banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d = {}
        count = 1
        #p = re.sub(r'[^\w\s]','',paragraph.lower())
        p= paragraph.lower()
        for i in (p.split(' ')):
            if i in d and i not in banned:
               d[i] = d[i]+1
            elif i not in banned:
                d[i] =1
        print(max(d,key=d.get))


Solution().mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit','hit')