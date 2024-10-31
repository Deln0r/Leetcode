class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        Collections.sort(robot);
        Arrays.sort(factory,(a,b)->a[0]-b[0]);
        long[][] dp=new long[robot.size()+1][factory.length+1];
        for(int i=0;i<robot.size();i++){
            dp[i][factory.length]=Long.MAX_VALUE;
        }
        for(int j=factory.length-1;j>=0;j--){
            long prefix=0;
            Deque<pair<Integer,Long>> que=new ArrayDeque<>();
            que.offer(new pair<>(robot.size(),0L));
            for(int i=robot.size()-1;i>=0;i--){
                prefix+=Math.abs(robot.get(i)-factory[j][0]);
                while(!que.isEmpty() && que.peekFirst().getKey()>i+factory[j][1]){
                    que.pollFirst();
                }
                while(!que.isEmpty() && que.peekLast().getValue()>=dp[i][j+1]-prefix){
                    que.pollLast();
                }
                que.offerLast(new pair<>(i,dp[i][j+1]-prefix));
                dp[i][j]=que.peekFirst().getValue()+prefix;
            }
        }
        return dp[0][0];
    }
    private static class pair<k,v>{
        private k key;
        private v value;
        public pair(k key,v value){
            this.key=key;
            this.value=value;
        }
        public k getKey(){
            return key;
        }
        public v getValue(){
            return value;
        }
    }
}