class Solution {
    public int fib(int n) {
        double A = (1 + Math.sqrt(5)) / 2;
        double B = (1 - Math.sqrt(5)) / 2;

        double fb = (Math.pow(A, n) - Math.pow(B, n)) / Math.sqrt(5);
        return (int) Math.round(fb);
    }
}