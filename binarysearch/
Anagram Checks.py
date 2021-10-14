#Java solution

import java.util.*;

class Solution {
    public boolean solve(String s0, String s1) {
        if (s0.length() != s1.length())
            return false;

        int[] store = new int[256];

        for (int i = 0; i < s0.length(); i++) {
            store[s0.charAt(i)]++;
            store[s1.charAt(i)]--;
        }

        for (int n : store)
            if (n != 0)
                return false;

        return true;
    }
}


bool solve(string s0, string s1) {
    if (s0.length() != s1.length()) return false;

    unordered_map<char, int> freq;

    for (auto i : s0) {
        freq[i]++;
    }

    for (auto i : s1) {
        freq[i]--;
        if (freq[i] == 0) freq.erase(i);
    }

    return freq.size() == 0;
}
