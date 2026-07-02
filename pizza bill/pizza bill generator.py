import random

amt = 0

print("1.Normal\n2.Deluxe")
p = int(input("Enter Pizza Choice: "))

print("1.Veg\n2.NonVeg")
o = int(input("Enter option:"))

if p==1:
    if o==1:
        amt=300
    else:
        amt=400

else:
    if o == 1:
        amt = 600
    else:
        amt = 800

ch = int(input("Do you want extra Cheese?(1.Yes / 2.No):"))
if ch == 1:
    amt += 100

tp = int(input("Do you want extra Topping? (1.Yes 2.No): "))
if tp == 1:
    amt += 100

wb = int(input("Do you want water bottle? (1.Yes / 2.No):"))
if tp == 1:
    n = int(input("How many bottles? "))
    amt += n * 20

kp = int(input("Do you want ketchup packets? (1.Yes / 2.No):"))
if kp == 1:
    m = int(input("How many packets? "))
    amt += m * 5

sd = int(input("Do you want soft drinks? (1.Yes / 2.No):"))
if sd == 1:
    d = int(input("How many bottles? "))
    amt += d * 75

ta = int(input("Take Away? (1.Yes 2.No): "))
if ta == 1:
    amt += 20

gst = amt * 0.18
net = amt + gst

if net > 5000:
    dis = net * 0.20
elif net > 3000:
    dis = net * 0.12
elif net > 2000:
    dis = net * 0.10
elif net > 1000:
    dis = net * 0.05
else:
    dis = 0

pay = net-dis

print("\n******** PIZZA BILL ********")
print("Bill No.:", random.randint(1000,9999))
print("Total Amount :", amt)
print("GST (18%)    :", round(gst,2))
print("Net Amount   :", round(net,2))
print("Discount     :", round(dis,2))
print("Amount Pay   :", round(pay,2))
print("****************************")
