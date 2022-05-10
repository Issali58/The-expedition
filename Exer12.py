import string
fname=input('enter the file name:')
fhand=open(fname)
count=dict()
for line in fhand:
    line=line.translate(line.maketrans('', '', string.punctuation))#removes the punctuation marks of the comma
    line=line.lower()
    b=line.split()#lines are split into words as b is a list of split lines
    for word in b:#creating a dictionary from the word
        count[word]=count.get(word,0)+1
print(count)
wds=input('type any string')#typing any word to see if the key is found in the dictionary
wds=str(wds)
if wds in count:
    print('present')
else:
    print('absent')
