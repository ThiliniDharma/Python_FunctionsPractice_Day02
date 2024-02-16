#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(x,y,z):
  return max([x,y,z])

print(max_num(1,2,3))
print(max_num(-5,-25,-87))
print(max_num(75,90,12))

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(first):

  if len(first) == 0:
    return 0
  ans = first[0]

  if len(first) > 1:
    for x in first[1:]:
      ans = ans * x

  return ans
    
print(mult_list([2,3,4,5]))

#Write a Python function called rev_string() to reverse a string.

def rev_string(input_string):
    return input_string[::-1]

input_str = "Hello, world!"
reversed_str = rev_string(input_str)
print(reversed_str)

#Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num, lower_bound, upper_bound):
    return lower_bound <= num <= upper_bound

number = 10
lower_bound = 5
upper_bound = 15
result = num_within(number, lower_bound, upper_bound)
print(result)
  
#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.The function accepts the number n, the number of rows to print

def pascal(n):
    for row in range(n):
         # Initialize the current row with the first element
        current_row = [1]
        
        for j in range(1, row + 1):
         # Calculate the element using the previous row
            current_element = current_row[j - 1] * (row - j + 1) // j
         # Append the element to the current row
            current_row.append(current_element)
    
        # Print the current row
        print(" ".join(str(x) for x in current_row).center(n * 2))

pascal(5)