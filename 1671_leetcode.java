class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int n = nums.length, lbs = 0; // lbs -> longest bitomic subsequence
        int [] dp = new int[n], dp2 = new int[n]; // dp[i] -> lis end at index i, dp2[i] -> lds end at index i
        List<Integer> lis = new ArrayList<>();
        for (int i = 0; i<n-1; i++) { // calculate longest increasing subsequence
            if (lis.isEmpty() || lis.get(lis.size()-1)<nums[i]) lis.add(nums[i]);
            else {   
                int idx = Collections.binarySearch(lis, nums[i]);
                if (idx<0) {
                    lis.set(-idx-1, nums[i]);
                }
            }
            dp[i] = lis.size();
        }
        lis = new ArrayList<>();
        for (int i = n-1; i>=1; i--) { // calculate longest decreasing subsequence
            if (lis.isEmpty() || lis.get(lis.size()-1)<nums[i]) lis.add(nums[i]);
            else {   
                int idx = Collections.binarySearch(lis, nums[i]);
                if (idx<0) {
                    lis.set(-idx-1, nums[i]);
                }
            }
            dp2[i] = lis.size();
            if (dp[i]>1 && dp2[i]>1) lbs = Math.max(lbs, dp[i]+dp2[i]-1);
        }
        return n-lbs;
    }
    
}