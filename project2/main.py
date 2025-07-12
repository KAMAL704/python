import random
n = random.randint(1, 100)
a =-1
guesses = 1

while(a != n):
    a = int(input("Enter your guesses"))
    if(a>n):
        print("Lower no please")
        guesses +=1
        
    
    elif(a<n):
        print("Higher no please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")

