# Array, HashMap & String Problems - LeetCode Solutions

This folder contains solutions to various LeetCode problems focusing on **Arrays**, **Hash Maps**, and **String** manipulation. Each solution demonstrates different algorithmic approaches and optimization techniques.

## 📋 Complete List of Problems

### Array Problems
| Problem | File | Key Approach | Time Complexity | Space Complexity |
|---------|------|--------------|-----------------|------------------|
| Two Sum | `two_sum.py` | HashMap for O(1) lookup | O(n) | O(n) |
| Contains Duplicate | `contains_duplicate.py` | Set comparison, HashMap, Sorting | O(n) / O(nlogn) | O(n) / O(1) |
| Contains Duplicate II | `contains_dup_2.py` | Sliding window with HashMap | O(n) | O(k) |
| Product of Array Except Self | `product_array_except_self.py` | Prefix/Suffix products | O(n) | O(1) |
| Maximum Subarray | `max_subarray.py` | Kadane's Algorithm | O(n) | O(1) |
| Best Time to Buy and Sell Stock II | `buy_and_sell_stock_2.py` | Greedy approach | O(n) | O(1) |
| Rotate Array | `rotate_array_k.py` | Array reversal technique | O(n) | O(1) |
| Jump Game II | `jump_games_2.py` | Greedy BFS approach | O(n) | O(1) |
| H-Index | `h_index.py` | Sorting or counting sort | O(nlogn) | O(1) |
| Gas Station | `gas_station.py` | Single pass greedy | O(n) | O(1) |
| Candy | `candy.py` | Two-pass greedy | O(n) | O(n) |
| Remove Duplicates from Sorted Array | `remove_dup_sorted.py` | Two pointers | O(n) | O(1) |
| Remove Duplicates from Sorted Array II | `remove_dup_sorted_2.py` | Two pointers with counter | O(n) | O(1) |
| Remove Element | `remove_el.py` | Two pointers | O(n) | O(1) |
| Majority Element | `majority_element.py` | Boyer-Moore Voting | O(n) | O(1) |
| Find Maximum Average Subarray | `find_max_av_array.py` | Sliding window | O(n) | O(1) |

### HashMap Problems
| Problem | File | Key Approach | Time Complexity | Space Complexity |
|---------|------|--------------|-----------------|------------------|
| Group Anagrams | `group_annagrams.py` | Sort as key in HashMap | O(n*mlogm) | O(n*m) |
| Top K Frequent Elements | `top_k_frequent_elements.py` | Counter + Heap/Bucket sort | O(nlogk) | O(n) |
| Longest Consecutive Sequence | `longest_consecutive_sequence.py` | Set for O(1) lookup | O(n) | O(n) |
| Valid Sudoku | `valid_sudoku.py` | HashSet for rows/cols/boxes | O(1) | O(1) |
| Random O(1) Insert/Delete | `random_o1.py` | Array + HashMap | O(1) | O(n) |
| Is Isomorphic | `is_isomorphic.py` | Bidirectional mapping | O(n) | O(1) |
| Word Pattern | `word_pattern.py` | Bidirectional mapping | O(n) | O(n) |
| Is Happy Number | `is_happy.py` | Cycle detection with set | O(logn) | O(logn) |
| Ransom Note | `ransom_note.py` | Character frequency count | O(n) | O(1) |

### String Problems
| Problem | File | Key Approach | Time Complexity | Space Complexity |
|---------|------|--------------|-----------------|------------------|
| Valid Anagram | `valid_anagram.py` | Character frequency/sorting | O(nlogn) | O(1) |
| Encode and Decode Strings | `decode_encode_str.py` | Length-based encoding | O(n) | O(1) |
| Longest Common Prefix | `longest_prefix.py` | Vertical/horizontal scanning | O(S) | O(1) |
| Length of Last Word | `length_last_word.py` | Reverse traversal | O(n) | O(1) |
| Reverse Words in String | `reverse_word_in_str.py` | Split and reverse | O(n) | O(n) |
| ZigZag Conversion | `zigzag.py` | Pattern-based indexing | O(n) | O(n) |
| Integer to Roman | `int_to_roman.py` | Greedy with value mapping | O(1) | O(1) |
| Roman to Integer | `roman_to_int.py` | Left-to-right parsing | O(n) | O(1) |
| Index of First Occurrence | `index_first_occur.py` | KMP or sliding window | O(n+m) | O(m) |
| Is Subsequence | `is_sub_str.py` | Two pointers | O(n) | O(1) |
| Text Justification | `text_justify.py` | Greedy line packing | O(n) | O(1) |

## 🔑 Key Algorithmic Approaches

### 1. **HashMap/HashSet Techniques**
- **Frequency Counting**: Track element occurrences
- **Fast Lookup**: O(1) contains/get operations
- **Bidirectional Mapping**: Map keys to values and vice versa
- **Cycle Detection**: Use set to detect revisited states

### 2. **Two Pointers**
- **Same Direction**: For in-place array modifications
- **Opposite Direction**: For sorted array problems
- **Fast/Slow**: For cycle detection and finding middle elements

### 3. **Sliding Window**
- **Fixed Size**: For subarray problems with fixed length
- **Variable Size**: For subarray problems with conditions
- **Character Frequency**: For string pattern matching

### 4. **Greedy Algorithms**
- **Local Optimal Choice**: Make best choice at each step
- **Kadane's Algorithm**: For maximum subarray problems
- **Interval Problems**: For scheduling and merging

### 5. **Prefix/Suffix Techniques**
- **Cumulative Operations**: Build prefix/suffix arrays
- **Product Arrays**: Avoid division by using prefix/suffix products
- **Range Queries**: Answer queries in O(1) time

### 6. **String Processing**
- **Pattern Matching**: KMP, sliding window
- **Character Mapping**: For anagram and isomorphic problems
- **Parsing**: For conversion and validation problems

## 🎯 Key Optimization Moments

### Space Optimization
- **In-place modifications**: Reduce space from O(n) to O(1)
- **Reuse input arrays**: Modify input instead of creating new arrays
- **Bit manipulation**: Use integers as sets for small ranges

### Time Optimization
- **Early termination**: Stop when answer is found
- **Avoid nested loops**: Use HashMap for O(1) lookups
- **Sort when beneficial**: Sometimes O(nlogn) sorting simplifies to O(n) overall

### Common Patterns
- **Check edge cases first**: Empty arrays, single elements
- **Use appropriate data structures**: Set for uniqueness, HashMap for mapping
- **Consider multiple approaches**: Brute force → Optimized → Space-optimized

## 🚀 Problem-Solving Strategies

1. **Understand the problem**: Read carefully, identify constraints
2. **Start with brute force**: Get a working solution first
3. **Identify bottlenecks**: Where can we optimize time/space?
4. **Choose right data structure**: Array, HashMap, Set, Heap, etc.
5. **Consider edge cases**: Empty input, single element, duplicates
6. **Test with examples**: Verify logic with given test cases

## 📈 Complexity Analysis Guide

- **Time Complexity**: Focus on the dominant operation in loops
- **Space Complexity**: Count auxiliary space, not input space
- **Amortized Analysis**: For operations that are occasionally expensive
- **Best/Average/Worst Case**: Consider all scenarios

## 🔧 Implementation Notes

- Most solutions include multiple approaches for comparison
- Comments explain the key insights and optimizations
- Time and space complexity documented for each approach
- Edge cases and constraints considered in implementations

---

*This collection demonstrates fundamental algorithmic techniques essential for technical interviews and competitive programming.*
