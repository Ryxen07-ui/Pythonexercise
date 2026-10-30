Name = input("enter your name: ")
print("Welcome Ryxen")
age = int(input("Enter your age: "))
# if/else
if age >= 18:
    print("You are adult")
else:
    print("You're still young")
# Lists (Access, Add, Change, remove )
Favfood = ["Pizza", "Noodle", "Ice cream", "Sticky Rice"]
Favfood.append("Fried Rice")
print(Favfood)
Favfood[2] = "Papaya Salad"
print(Favfood) 
Favfood.remove("Pizza")
print(Favfood)