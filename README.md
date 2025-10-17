# qa-analyst-assessment
# QA Analyst role assessment for SS&amp;C Technologies.
**Candidate:** Abigail Graham
**Language Used:** Python
**Completion Date:** October 17, 2025

## Part 1: Functional Programming
- **Time Spent:** 35 minutes
- **Approach:** 
The remove_duplicates function takes a list as an input and returns a new list containing only the unique elements from the original list, while preserving the order they appeared in. Using a set allows the program to keep track of the elements it has already added to the result list.


## Part 2: API Testing
- **Time Spent:** 40 minutes
- **Approach:** To begin, set up the environment to install necessary libraries to make API calls and structure tests. Identify API test points and create functions that make API requests. Run these tests to check if the API has behaved as expected.

## How to Run 
### Part 1
Go to the code cell containing remove_duplicates and execute the cell by clicking the run cell icon, or Shift + Enter. The output will return as a new list where all duplicates are removed, preserving order of first occurrences. 

### Part 2
Ensure you have executed the cell that downloads the necessary libraries. Then, go to the cell containing the test functions, and execute this cell to define the test functions and the class. Go to the cell containing !pytest to run the tests, or use the cell that manually calls the test functions. Check the output of the code, and if there are no AssertionError exceptions, all tests have passed.
