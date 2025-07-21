char* longestCommonPrefix(char** strs, int strsSize) {
    static char a[200];  
    int i, j;

    for (j = 0; strs[0][j] != '\0'; j++) {
        for (i = 1; i < strsSize; i++) {
            if (strs[i][j] != strs[0][j]) {
                a[j] = '\0';  
                return a;
            }
        }
        a[j] = strs[0][j];  
    }
    a[j] = '\0';  
    return a;
}
