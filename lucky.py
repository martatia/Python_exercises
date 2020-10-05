# Tehtävä:
# Positiivinen kokonaisluku on onnenluku, jos sen numeroiden summa on jaollinen 7:llä. 
# Esimerkiksi luku 25743 on onnenluku, koska 2+5+7+4+3=21, joka on jaollinen 7:llä.
# Tehtäväsi on tarkastaa, onko annettu luku n onnenluku.

def check(n):
    x=[int(i) for i in str(n)]
    summa=sum(x)
    if summa%7==0:
        return True
    return False
        
if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True