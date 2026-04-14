class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def helper(index) -> bool:
            print(index)
            if index == 0:
                return True
            if index < 0:
                return False

            jumpable = False
            for i in range( index - 1, -1, -1 ):
                if nums[i] >= index - i:
                    jumpable |= helper( i )
            return jumpable

        return helper( len( nums ) - 1 )
            