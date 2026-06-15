class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int min_price = prices[0];

        for(int i=0; i<prices.length; i++){
            if (min_price > prices[i]){
                min_price = prices[i];
            }
            int profit = prices[i] - min_price;
            if (profit > max_profit){
                max_profit = profit;
            }
        }

    return max_profit;
    }
}
