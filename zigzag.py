# Tehtävä:
# Listalle lisätään luvut 1,2,…,n, ensin luku 1 ja sitten seuraavat luvut vuorotellen oikealle ja vasemmalle puolelle. 
# Esimerkiksi kun n=5, tuloksena on lista [5,3,1,2,4].
# Millainen lista tulee tietyllä n:n arvolla?

def create(n):
    n=n
    a = []
    c=[]
    for i in range(n,0,-1):
        if i%2!=0:
            a.append(i)
        else:
            c.append(i)
            c.sort()
    return a+c

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]