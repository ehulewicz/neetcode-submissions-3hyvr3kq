class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        def helper(index) -> bool:
            if index in mem:
                return mem[index]
            if index == 0:
                return True

            for i in range( index - 1, -1, -1 ):
                if nums[i] >= index - i and helper( i ):
                    mem[index] = True
                    return True
            return False

        return helper( len( nums ) - 1 )
            