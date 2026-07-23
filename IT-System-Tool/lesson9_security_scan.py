print("="* 40)
print("     SECURITY SCAN")
print("="* 40)

devices = [
    "Laptop",
    "Server",
    "Unknown Device",
    "Router"
]

for device in devices:
    if device == "Unknown Device":
        print(device, "- WARNING\n")

    else:
        print(device, "- Secure\n")

print("Scan completed.")