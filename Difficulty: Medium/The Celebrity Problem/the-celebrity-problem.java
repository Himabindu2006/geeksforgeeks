class Solution {
    public int celebrity(int mat[][]) {
        int n = mat.length;
        int i = 0, j = n - 1;
        while (i < j) {
            if (mat[j][i] == 1) j--;
            else i++;
        }
        int c = i;
        for (int k = 0; k < n; k++) {
            if (k == c) continue;
            if (mat[c][k] != 0 || mat[k][c] != 1) return -1;
        }
        return c;
    }
}