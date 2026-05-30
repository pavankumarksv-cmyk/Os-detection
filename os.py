import platform

def detect_os():
    print("Detecting Operating system...\n")
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    machine_type = platform.machine()

    print("-----SYSTEM INFORMATION-----")
    print(f"Operating System: {os_name}")
    print(f"OS Version: {os_version}")
    print(f"OS Release: {os_release}")
    print(f"Machine Type: {machine_type}")
    
    print("\n-----OS TYPE DETECTION-----")
    
    if os_name.lower() == "windows":
        print("This system is running Microsoft windows.")
    
    elif os_name.lower() == "linux":
        print("This system is running Linux")
    
    elif os_name.lower() == "darwin":
        print("This system is running macOS")
    
    else:
        print("Unknown Operating System.")
    
if __name__ == "__main__":
    detect_os()