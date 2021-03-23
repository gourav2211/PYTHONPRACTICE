#from collections import OrderedDict
class Solution():

    def ElectionWinner(self, arr):
        votes = {}

        for i in arr:
            if i in votes.keys():
                votes[i] += 1
            else:
                votes[i] = 1
        max_votes = max(votes.values())
        winner_list = [k for k,v in votes.items() if v == max_votes]
        return min(winner_list)

if __name__ == "__main__":
    T = [x for x in input().strip().split()]
    dict1 = Solution().ElectionWinner(T)
    print(dict1)
