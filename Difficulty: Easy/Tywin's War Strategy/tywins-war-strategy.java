import java.util.*;
class Solution {
    public int minSoldiers(int[] arr, int k) {
        int n = arr.length;
        int requiredLucky = (n + 1) / 2; 
        int luckyCount = 0;
        List<Integer> costs = new ArrayList<>();

        for (int soldiers : arr) {
            if (soldiers % k == 0) {
                luckyCount++;
            } else {
                costs.add(k - (soldiers % k));
            }
        }

        if (luckyCount >= requiredLucky) {
            return 0;
        }

        
        Collections.sort(costs);
        int soldiersNeeded = 0;
        for (int i = 0; i < requiredLucky - luckyCount; i++) {
            soldiersNeeded += costs.get(i);
        }

        return soldiersNeeded;
    }
}