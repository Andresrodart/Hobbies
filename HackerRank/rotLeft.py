# Complete the rotLeft function below.
#Proposal 1
def rotLeft(a, d):
    for x in range(d):
        aux = a[0]
        for i in range (len(a) - 1):
            a[i] = a[i+1]
        a[len(a)-1] = aux
    return a

#Proposal 2
def rotLeft(a, d):
    for x in range(d):
        a.append(a[0]);
        a.pop(0); #a = a[1:]; slice operation take much longer
    return a;

#Proposal 3, if deques can be use;
def rotLeft(a, d):
    a.rotate(-d);
    return a;