

x = int(input("Enter your Number: "))
y = x
rev = 0
rem = 0
if x == 0:
    print("True")
elif x < 0:
    print("False")
else:
    while x > 0:
        rem = x % 10
        rev = rev * 10 + rem
        x = x // 10
        
    if y == rev:
        print("True")
    else:
        print("False")
