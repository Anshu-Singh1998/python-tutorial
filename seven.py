# let us c
# Input cost price and sales price of an item through keyboard.
# wap to determine whether the seller made profit or loss
# and also determine profit or loss he made.
cp = int(input("Enter cost price:"))
sp = int(input("Enter selling price:"))
loss = 0
profit = 0
if cp > sp:
    loss = cp - sp
    print("business ran in loss", loss)
elif cp < sp:
    profit = sp - cp
    print("congratulations you are in profit", profit)
else:
    print("continue with what you are doing")
