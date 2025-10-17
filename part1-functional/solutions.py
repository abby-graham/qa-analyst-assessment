# **Take-Home Assignment Part 1: "Functional Programming - Remove Duplicates"**

## **Problem**
Write a **pure function** that removes duplicates from a list/array while preserving the original order of first occurrences.

**Choose ONE language:** JavaScript, Python, C#, or Go
Language chosen: Python 
**Example:**
```
Input:  [1, 2, 3, 2, 4, 1, 5]
Output: [1, 2, 3, 4, 5]
```

## **Requirements**
1. **Pure function** - same input always gives same output, no side effects
2. **Don't modify** the original input 
3. **Use functional programming approaches** (built-in methods like filter, map, etc.)
4. **Test your solution** with the provided test cases

## **Test Cases**
Your function should handle these cases:

```javascript
// JavaScript example:
removeDuplicates([1, 2, 3, 2, 4, 1, 5])  // [1, 2, 3, 4, 5]
removeDuplicates([1, 1, 1])              // [1]
removeDuplicates([])                     // []
```

```python
# Python example:
remove_duplicates([1, 2, 3, 2, 4, 1, 5])  # [1, 2, 3, 4, 5]
remove_duplicates([1, 1, 1])              # [1]
remove_duplicates([])                     # []
```

## **Deliverables**
- Working function that passes the test cases
- Brief comment explaining your approach

## **Evaluation Focus**
- **Functional Programming**: Uses FP concepts (pure functions, immutability)
- **Code Quality**: Clean, readable implementation
- **Correctness**: Function works as specified

**Time Estimate:** 30 minutes

## **Notes**
- Focus on demonstrating functional programming understanding
- Simple, clear solutions are preferred over complex ones

# Functional Programming using Python - Remove Duplicates
def remove_duplicates(input_list):
  """
  Removes duplicate elements from a list while preserving the order of the first occurrences.
  
  Args:
    input_list: The list from which to remove duplicates. 
  Returns:
    A new list with all duplicates removed, and preserving the order of the first occurrences. 
  """
  # Above, I created a function to remove duplicates from a list as an input and return the new list with duplicates removed. 
  # This is also explained in the docstring directly below the definition of the function.
  seen = set() # Initializes an empty set defined as seen to keep track of elements we have already encountered from input_list.
  result = [] # Initializes an empty set called result which will store each unique element from input_list, and this will be the list that will return at the end. 
  for item in input_list: # Start of loop that iterates through each element.
    if item not in seen: # Checks if the current item element has already been present in seen. If it is not in the seen set, it means it is the first time we are seeing this value and it must be added.
      seen.add(item) # If the item is not in seen, this line adds the value to the set.
      result.append(item) # This line adds the unique item to the end of the result list.
  return result #The loop has finished processing the elements in input_list, and this returns the new result list.

# Usage Examples
my_list1 = [1, 2, 3, 2, 4, 1, 5]
unique_list1 = remove_duplicates(my_list1)
print(unique_list1)

my_list2 = [1, 1, 1]
unique_list2 = remove_duplicates(my_list2)
print(unique_list2)

my_list3 = []
unique_list3 = remove_duplicates(my_list3)
print(unique_list3)
