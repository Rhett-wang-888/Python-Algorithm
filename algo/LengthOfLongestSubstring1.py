# @title: LengthOfLongestSubstring1
# @description: TODO 无重复字符的最长字符串
# @author  Rhett
# @date 2021/3/28 10:19

def LengthOfLongestSubstring(s:str)->int:
    occ=set()
    n=len(s)
    rk,ans=-1,0
    for i in range(n):
        if i !=0:
            occ.remove(s[i-1])
        while rk+1<n and s[rk+1] not in occ:
            occ.add(s[rk+1])
            rk +=1

        ans=max(ans,rk-i+1)
    return ans

    