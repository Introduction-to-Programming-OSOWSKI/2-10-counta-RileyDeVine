#WRITE YOUR CODE IN THIS FILE

#define function
def countA(w):
    total = 0
    for i in range(0,len(w)):
        if w[i] == "a":
            total = total + 1
    return total

print(countA("baseball"))

