class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        di={}
        for i in numbers:
            di[i]=numbers.index(i)
        temp=list(di.keys())
        res=[]
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if temp[i] + temp[j] == target:
                    res.append(di.get(temp[i]) + 1)
                    res.append(di.get(temp[j]) +1 )
                    return res
        if len(res)==0:
            res.append(di.get(target/2)+1)
            res.append(di.get(target/2)+2)
            return res
