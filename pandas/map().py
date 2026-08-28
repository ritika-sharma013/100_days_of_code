# Understanding map() function in pandas.

# Using DATAFRAME 
import pandas as pd

df = pd.DataFrame([list("geeksforgeeks")] * 5) #coverts string to list, then multiply it 5 times to create a DataFrame
print("Original DataFrame:\n")
print(df.to_string(index=False, header=False)) #remvoes row and column number

new_df = df.map(str.upper) #usage of map() fucn to convert all the elements of df into upper characters

print("\nTransformed DataFrame:\n")
print(new_df.to_string(index=False, header=False))



# Using SERIES to apply a function to each element

s = pd.Series(list("ritsincapital"))
print("Original series:\n")
print('\n'.join(s.tolist()))

new_s = s.map(str.upper)

print("\nTransformed series:\n")
print('\n'.join(new_s.tolist()))