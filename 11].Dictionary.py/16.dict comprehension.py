        #  key:value   
        #    |   |
squares = {i:i*i for i in range(1,6)}
print(squares)

Marks = {'phy': 35, 'chem': 56, 'bio': 67, 'eng': 99}
top = {sub:mark for sub,mark in Marks.items() if mark>90}
print(f"Topper = {top}")

double = {sub:mark*2 for sub,mark in Marks.items()}
print(double)

## ZIP - pairs corresponding elements from multiple lists
Name = ['Diya','Navya','Maya']
Marks = [95,97,90]
result = {N:M for N,M in zip(Name,Marks)}
print(result)