bool isPalindrome(int x) {
    if (x < 0) return false;
    char str[12];  // Enough space for int range and '\0'
    sprintf(str, "%d", x);

    // Check if the string is a palindrome
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) {
            return false;
        }
    }
    return true;
}
