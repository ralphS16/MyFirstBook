from math import sqrt, floor, ceil
w = 12
h = round(w*sqrt(2))-2

def rmlist(word):
    return ["\\textbf{"+c+"}" for c in word]

def arrow(x1,y1,x2,y2):
    return "\\arrow[from={}-{}, to={}-{}]".format(x1,y1,x2,y2)


####OBJECTS####
top = "&&".join(["\\bullet"]*round((w-len("CATEGORY"))/2) + rmlist("CATEGORY") + ["\\bullet"]*round((w-len("CATEGORY"))/2)) + "\\\\"
top2 = "&" + "&&".join(["\\bullet"]*ceil((w-1-len("THEORY"))/2) + rmlist("THEORY") + ["\\bullet"]*floor((w-1-len("THEORY"))/2)) + "\\\\"
bot = "&&".join(["\\bullet"]*round((w-len("SARKIS"))/2) + rmlist("SARKIS") + ["\\bullet"]*round((w-len("SARKIS"))/2)) + "\\\\"
bot2 = "&" + "&&".join(["\\bullet"]*ceil((w-1-len("RALPH"))/2) + rmlist("RALPH") + ["\\bullet"]*floor((w-1-len("RALPH"))/2)) + "\\\\"
even = "\\bullet"+"&"*((w-1)*2)+"\\bullet\\\\"
odd = "&\\bullet" + "&"*((w-2)*2)+"\\bullet\\\\"
print(top)
print(top2)
for i in range(h):
    print(even)
    print(odd)
print(even)
print(bot2)
print(bot)

##Horizontal Arrows
for i in range(w-1):
    print(arrow(1,2*i+1,1,2*i+3))
for i in range(w-2):
    print(arrow(2,2*i+2,2,2*i+4))
for i in range(w-2):
    print(arrow(4+2*h,2*i+4,4+2*h,2*i+2))
for i in range(w-1):
    print(arrow(5+2*h,2*i+3,5+2*h,2*i+1))

##Vertical Arrows
for i in range(h+2):
    print(arrow(2*i+3,1,2*i+1,1))
for i in range(h+1):
    print(arrow(2*i+4,2,2*i+2,2))
for i in range(h+2):
    print(arrow(2*i+1,2*w-1,2*i+3,2*w-1))
for i in range(h+1):
    print(arrow(2*i+2,2*w-2,2*i+4,2*w-2))

##Diagonal-Horizontal Arrows
for i in range(w-1):
    print(arrow(1,2*i+1,2,2*i+2))
for i in range(w-1):
    print(arrow(2,2*i+2,1,2*i+3))
for i in range(w-1):
    print(arrow(4+2*h,2*i+2,5+2*h,2*i+1))
for i in range(w-1):
    print(arrow(5+2*h,2*i+3,4+2*h,2*i+2))

##Diagonal-Vertical Arrows
for i in range(h+1):
    print(arrow(2*i+3,1,2*i+2,2))
for i in range(h+1):
    print(arrow(2*i+4,2,2*i+3,1))
for i in range(h+1):
    print(arrow(2*i+3,2*w-1,2*i+4,2*w-2))
for i in range(h+1):
    print(arrow(2*i+2,2*w-2,2*i+3,2*w-1))