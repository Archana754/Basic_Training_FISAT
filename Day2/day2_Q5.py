# https://leetcode.com/problems/lemonade-change/description/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cfive = 0
        cten = 0

        for coin in bills:
            if coin == 5:
                cfive += 1
            elif coin == 10:
                if cfive > 0:
                    cfive -= 1
                    cten += 1
                else:
                    return False
            else:
                if cfive > 0 and cten > 0:
                    cfive -= 1
                    cten -= 1
                elif cfive >= 3:
                    cfive -= 3
                else:
                    return False
        return True





