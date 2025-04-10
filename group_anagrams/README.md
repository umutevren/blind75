# Group Anagrams

## Problem Description

[LeetCode - Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples:

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

### Constraints:

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

## Solution Approach

The solution uses a dictionary to group strings that are anagrams of each other:

1. Iterate through each string in the input array
2. Sort the characters of each string (a key insight: anagrams will have the same sorted string)
3. Use the sorted string as a key in a dictionary:
   - If the key already exists, append the original string to the list of anagrams
   - If the key doesn't exist, create a new list with the original string
4. Return all the values (groups of anagrams) from the dictionary

This approach has:
- Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string
- Space Complexity: O(n * k) for storing the dictionary of anagrams

## Code Explanation

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_groups = {}  
    for word in strs:
        sorted_word = "".join(sorted(word))  

        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)  
        else:
            anagram_groups[sorted_word] = [word]      

    return list(anagram_groups.values())
```

The solution efficiently identifies anagrams by using the fact that two anagrams will have the same characters when sorted. By using this sorted string as a key in our dictionary, we can easily group together all words that are anagrams of each other. 