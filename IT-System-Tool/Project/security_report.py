# Functions ==================================
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

def generate_report(name, department, devices, risk_level):
    print()
    print("=" * 40)
    print("    SECURITY REPORT GENERATOR")
    print("=" * 40)

    print("Name:", name)
    print("Department:", department)

    print()
    print("Device Scan")

    for device in devices:
        print(
            device["name"],
            "-",
            device["status"]
        )
    print()
    print("Security Assessment")
    print("Risk Level:", risk_level)

# Main program ========================
user_name, user_department = ask_user()

devices = scan_devices()

risk_level = calculate_risk(devices)

generate_report(
    user_name,
    user_department,
    devices,
    risk_level
)