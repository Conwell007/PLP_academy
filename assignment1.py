#Let's code a simple calculator
#Step 1; Define our variables
num_1=input("Enter first number: ")
num_2=input("Enter second number: ")
#Step 2; Convert string inputs to integers
num_1=int(num_1)
num_2=int(num_2)
#Step 3; Perform the arithmetic operations
sum_result = num_1 + num_2
diff_result = num_1 - num_2
prod_result = num_1 * num_2
quot_result = num_1 / num_2 if num_2 != 0 else "undefined (division by zero)"

print("Results:, \nSum = ",sum_result,"\nDifference = ",diff_result,"\nProduct = ",prod_result,"\nQuotient = ",quot_result)
