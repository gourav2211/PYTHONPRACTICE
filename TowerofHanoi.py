class Solution():
    def TowerOfHanoi(self,n,f_rod,t_rod,a_rod):
        if n == 1:
            print ("Move disk 1 from disk {} to {}".format(f_rod, t_rod))
            return
        self.TowerOfHanoi(n-1,f_rod,a_rod,t_rod)
        print("Move disk {} from {} to {}".format(n,f_rod,t_rod))
        self.TowerOfHanoi(n-1,a_rod,t_rod,f_rod)

if __name__=="__main__":
    Solution().TowerOfHanoi(4,'A','B','C')