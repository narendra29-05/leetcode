class Solution:
    def search(self, nums, target) :
        #nums= [-1,0,3,5,9,12], target = 13
        #        0 1 2 3 4 5
            #    l   m     h
            #          l m  h

                    #        hl



                    #3+5//2-->4

        #[-1,0] [3,9,2]
        #[-1,0,3] [9,2]

        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2   #answer (0+5)//2--->2
            if nums[mid]==target:#3==9
                return mid
            if target > nums[mid]:
                low=mid+1
            else:
                high=mid-1
            


        return -1


        

