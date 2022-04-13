fhands=input('enter file name:')
fhand=open(fhands)#file handle
w=['and','is','sun','the']#repeated words, the program is produce a list of words that are not repeated
for line in fhand:
    ty=line.split()#lines are split into a list of words
    for i in ty:#loop to look through each list of string produced
        if i not in w:
            w.append(i)#one argu is added to the list

w.sort()#sorts the words alphabetically starting with capital letters
print(w)

#program to find the receivers of the EmailUser
ehand=input('enter file name:')
ehands=open(ehand)
count=0
for line in ehands:
    if line.startswith('From:'):#skips a from with the semi colons
        continue
    elif line.startswith('From'):
        p=line.split()#splits line into words
        rt=p[1]#index position of split
        print(rt)
        count=count+1

print('the number of emails received:',count)

#program to produce the maximum and minimum numbers
r=list()
while True:
    inp=input('enter the number')
    if inp=='done':
        break
    inp=float(inp)
    r.append(inp)#adding a number to the list after specifying the data type

print(r)

print('maximum:',max(r),'minimum',min(r))
