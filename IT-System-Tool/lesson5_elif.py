print("=" * 40)
print("     AGE CATEGORY CHECKER")
print("=" * 40)

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

print("Program finished.")