hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
if h <= 40:
 	print( h  * r)
elif h > 40:
	print(40* r + (h-40)*1.5*r)