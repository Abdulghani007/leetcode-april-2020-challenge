
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        d = binaryMatrix.dimensions()
        ans = 999
        high = d[1] - 1
        for i in range(0,d[0]):
            low = 0
            while low<=high:
                mid = (low+high)//2
                if binaryMatrix.get(i,mid) == 1:
                    if ans>mid:   
                        ans = mid
                    high = mid - 1
                else:
                    low=mid+1
            high = mid
        if ans == 999:
            return -1
        return ans
