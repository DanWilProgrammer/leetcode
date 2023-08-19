// a function which returns true if a number is the same reversed as it is forwards

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isPalindrome(int x) {
    string s = to_string(x);
    string s2 = s;
    reverse(s2.begin(), s2.end());
    return s == s2;
}