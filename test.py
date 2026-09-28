

    
def bill():
    return float(input("how much is the bill?"))

def tip():
    return [bill * 1.00, bill * 1.15, bill * 1.20, bill *1.25]

x=(input("how much is the bill?"))
print(f"the bill is ${x}")

print("\nhow was the service? (bad, okay, good, great)")
service = input("your choice:  ")

def service(input):
    input["bad", "okay", "good", "great"]
if service == "bad":
    print (f"total bill: ${tip[0]}")
elif service == "okay":
    print (f"total bill: ${tip[1]}")
elif service == "good":
    print (f"total bill: ${tip[2]}")
elif service == "great":
    print (f"total bill: ${tip[3]}")
else:
    print (f"invalid choice entered")

