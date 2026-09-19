marks = {
    'Riya':{'phy':43,'chem':12,'bio':98,'eng':10},
    'Diya':{'phy':76,'chem':55,'bio':34,'eng':89},
    'Shreya':{'phy':20,'chem':35,'bio':47,'eng':79},
    'Maya':{'phy':35,'chem':56,'bio':67,'eng':99},
}
ascending = dict(sorted(marks.items(),key=lambda x:x[1]['phy']))
print(ascending)
descending = dict(sorted(marks.items(),key=lambda x:x[1]['phy'],reverse='True'))
print(descending)
total = dict(sorted(marks.items(),key = lambda x:sum(x[1].values())))