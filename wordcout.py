import re


# Split the string at every white-space character:

txt = "The rain in Spain the man who ,my screen rain 1212,2145"
txt=txt.lower()
x=re.findall('\w[a-z]+', txt)
print(x)
#x = re.split("\s", txt)
stopword= ['the', 'in' , 'a' , 'is' , 'a', 'has' , 'have']

for a in stopword:
    for b in x:
       if a==b:
           x.remove(a)



worddict = {}

y = 0
for i in x:
    # if worddict.keys() != None:
    #     keyslist = worddict.keys()
    #
    # elif i in worddict.keys() :
    #     worddict[i] += 1
    # else:
    #     worddict[i] = 1
    if y==0:

        worddict[i]= 1
        y +=1

    elif i in worddict.keys():

        worddict[i] += 1
    else:
        worddict[i] =1


print(worddict)
print(worddict.values())

val= worddict.values()

print(max(val) )

for key ,val1 in worddict.items():

    if val1 == max(val):
        print(key , val1)

