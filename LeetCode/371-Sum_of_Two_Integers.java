class Solution {
    public int getSum(int a, int b) {
        while(b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}

// Time Complexity: O(1) - fixed number of bits (32 or 64)
// Space Complexity: O(1)