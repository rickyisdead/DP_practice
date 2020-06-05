# import timeit

# code_to_test = """

# top-down solution, though bottom-up could be faster without function call overhead
def minSteps(array_in, index, step, memo):

  # check table
  if memo[index] > 0:
    return step + memo[index]
  else:
    length = len(array_in)

    # base case
    if index == length - 1:
      return step

    # recursive case
    else:
      ans = float('inf')

      for i in range(1, array_in[index] + 1):
        if index + i < length:
          ans = min(ans, minSteps(array_in, index + i, step + 1, memo))
      
      # add to table
      memo[index] = ans - step

      return ans

array_in = [3,4,2,1,2,3,7,1,1,1,3]
memo = [-1] * len(array_in)
answer = minSteps(array_in, 0, 0, memo)
print(answer)

# """

# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)

# Ave. runtime without print: 2.872e-05

# Test examples
# array_in = [1,3,2,2,4,2,1]
# array_in = [1,2,2,1]
# array_in = [1]
# array_in = [1,2,3,4,5,6,7,8,9]
# array_in = [9,8,7,6,5,4,3,2,1]