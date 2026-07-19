print("=" * 40)
print("   SECURITY ACCESS CHECK")
print("=" * 40)

username = input("Enter Username: ")
password = input("Enter password: ")


if username == "admin" and password == "Python123":
    print("Access granted.")
else:
    print("Access denied.")

print("Security check complete.")