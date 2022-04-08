print("hello word")
wr=input("hours:")
wp=input("rate pay:")
wp=float(wp)
wr=float(wr)
tp=wr*wp
print("final pay:",tp)
#conversion variable type from strung to int
name=input("the europe floor:")
name=int(name)
usf=name+1
print("us floor:",usf)
#finding out the remainder from expression
v=7
vc=v%3
vc=float(vc)
print("ans:",vc)
print(type(vc))
x=input("write down number:")
x=int(x)
if x>10:
    print("large number")
    if x<100:
        print("more effort")
    else:
        print("to the moon")
else:
    print("small figure")
print("ALL DONE")
dd=input("insert a number")
try:
    astro=int(dd)
except:
    astro=-1
if astro>0:
    print("its a number",astro)
else:
    print('try putting a figure')
