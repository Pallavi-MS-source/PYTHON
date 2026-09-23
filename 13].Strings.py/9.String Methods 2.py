"""CHECKING CONTENT (T/F)
# isalpha():All letters?
# isdigit():All digits?
# isalnum():Aiphanumeric only?
# isspace():All whitespace?
# startswith() and endswith()"""

text="hwjfwekjr"
# text="Pallavi Sunagar" #bcz of space o/p is false
print(text.isalpha())

num="123758"
#num="97.8"  #false
print(num.isdigit())

numalpha="12hue34fk" #true
# numalpha="3787484"   #true
# numalpha="uerieno"   #true
# numalpha="hei 49ke"  #false
print(numalpha.isalnum())

space="      "
# space="    \n\t"
print(space.isspace())

name="Pallavi"
print(name.startswith("P"))
print(name.endswith("v"))