bill = float(input("how much is the bill? $"))
tip = [1.00, 1.15, 1.20, 1.25]
service = input("how was the service? (bad, okay, good, great)")
service = input("your choice:  ")
print("the bill is $")
if service == "bad":
    print (tip[0]*bill)
elif service == "okay":
    print (tip[1]*bill)
elif service == "good":
    print (tip[2]*bill)
elif service == "great":
    print (tip[3]*bill)

