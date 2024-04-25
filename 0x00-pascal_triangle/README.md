# Pascal's Triangle

## Description
This is a solution to the Pascal's Triangle interview question. Pascal's Triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it. The triangle starts with a single 1 at the top, and each subsequent row is constructed by adding adjacent numbers in the row above.

## Implementation
The solution to this problem involves generating Pascal's Triangle up to a given number of rows. Here's a high-level overview of the implementation:

1. Create an empty list to store the rows of Pascal's Triangle.
2. Iterate from 0 to the given number of rows.
3. For each row, create a new list to store the numbers in that row.
4. For the first and last numbers in each row, set them to 1.
5. For the remaining numbers, calculate the sum of the two numbers directly above them in the previous row.
6. Append the row to the list of rows.
7. Return the list of rows.
