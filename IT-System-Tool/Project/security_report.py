print("=" * 40)
print("    SECURITY REPORT GENERATOR")
print("=" * 40)

def ask_user():
    name = input("Enter your name: ")
    department = input("Enter your department: ")

    return name, department

def scan_devices():
    devices = [
       {
           "name" : "Laptop",
           "ip" : "192.168.1.10",
           "status" : "Secure"
       },
       {
           "name" : "Server",
           "ip" : "192.168.1.20",
           "status" : "Secure"
       },
       {
           "name" : "Unknown Device",
           "ip" : "192.168.1.50",
           "status" : "Warning"
       },
       {
           "name" : "Router",
           "ip" : "192.168.1.1",
           "status" : "Secure"
       }
    ]
    return devices

def calculate_risk(devices):
    warnings = 0

    for device in devices:
        if device["status"] == "Warning":
            warnings += 1

    if warnings > 0:
        return "HIGH"
    else:
        return "LOW"

user_name, user_department = ask_user()

print()
print("User Information")
print("Name: ", user_name)
print("Department: ", user_department)

devices = scan_devices()

print()
print("Device Scan")

for device in devices:
    if device["status"] == "Warning":
        print(device["name"], "-",  device["status"])
    else:
        print(device["name"], "-", device["status"])

risk_level = calculate_risk(devices)

print()
print("Security Assessment")
print("Risk Level: ", risk_level)