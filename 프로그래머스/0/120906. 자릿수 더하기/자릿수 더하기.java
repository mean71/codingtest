class Solution {
    public int solution(int n) {
        int res = 0;
        while (n > 0) {
            res += n%10;
            n /= 10;
        }
        return res;
    }
}