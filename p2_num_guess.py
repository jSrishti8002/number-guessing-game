import random

n = random.randint(0,100)
print("🎮 Welcome to Number Guessing Game!")

a = None
guesses = 0

while(a != n):
    guesses += 1
    a = int(input("Guess the number 😈 "))

    if(a > n):
        print("Enter a smaller number 🔻")
    elif(a < n):
        print("Enter a greater number 🔺")

print(f"Congrats! 🎉 You won...You guessed the correct number {n} in {guesses} guesses ✅")