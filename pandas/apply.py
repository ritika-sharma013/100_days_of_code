#Understanding apply() fucntion in pandas 

#  Using DATAFRAME to apply a function to each row or column

# import pandas as pd
# s = 'geeksforgeeks'
# df = pd.DataFrame([list(s)] * 5)

# print("Original dataFrame:\n")
# print(df.to_string(index=False, header=False))

# new_df = df.apply(lambda x: ''.join(x), axis=1)

# print("\nTransformed dataFrame:\n")
# print('\n'.join(new_df.tolist()))

# When axis =0, columns are passed as Series to the function. 
# ggggg
# eeeee
# eeeee
# kkkkk
# sssss
# fffff
# ooooo
# rrrrr
# ggggg
# eeeee
# eeeee
# kkkkk
# sssss

# when axis =1, ros are passed as Series to the function.
# g e e k s f o r g e e k s
# g e e k s f o r g e e k s
# g e e k s f o r g e e k s
# g e e k s f o r g e e k s
# g e e k s f o r g e e k s


# Using SERIES to apply a function to each element

s = pd.Series(list("ritsincapital"))

print("Original Series:\n")
print('\n'.join(s.tolist()))

new_s = s.apply(lambda x: x.upper())

print("\nTransformed Series:\n")
print('\n'.join(new_s.tolist()))

# output 
# R
# I
# T
# S
# I
# N
# C
# A
# P
# I
# T
# A
# L