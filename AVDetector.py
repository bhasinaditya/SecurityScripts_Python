"""
Detects AV product on device
"""
import wmi
import os


def check_antivirus():
    try:
        # Initialize WMI connection for SecurityCenter2 namespace
        wmi_obj = wmi.WMI(namespace="root\\SecurityCenter2")

        # Query for antivirus products
        antivirus_products = wmi_obj.AntiVirusProduct()

        if not antivirus_products:
            print("No antivirus software detected.")
        else:
            # Output details for each antivirus product found
            for product in antivirus_products:
                product_name = product.displayName
                product_state = product.productState
                # Attempt to retrieve product version (may not always be available)
                product_version = getattr(product, 'productVersion', 'Version not available')
                # Check if the antivirus is enabled (productState bitmask analysis)
                is_enabled = (product_state & 0x1000) == 0x1000

                if is_enabled:
                    print(f"Running Antivirus: {product_name}, Version: {product_version}")
                else:
                    print(f"Detected Antivirus (Not Running): {product_name}, Version: {product_version}")

    except Exception as e:
        print(f"Error checking antivirus status: {e}")
        if not os.name == 'nt':
            print("This script is designed to run on Windows systems only.")


def check_active_directory():
    try:
        # Initialize WMI connection for default namespace
        wmi_obj = wmi.WMI()

        # Query for computer system information
        for system in wmi_obj.Win32_ComputerSystem():
            domain_role = system.DomainRole
            # DomainRole values:
            # 0 = Standalone Workstation, 1 = Member Workstation,
            # 2 = Standalone Server, 3 = Member Server,
            # 4 = Backup Domain Controller, 5 = Primary Domain Controller
            if domain_role in [1, 3, 4, 5]:
                print("Active Directory is installed. System is part of a domain.")
            else:
                print("Active Directory is not installed. System is not part of a domain.")

    except Exception as e:
        print(f"Error checking Active Directory status: {e}")
        if not os.name == 'nt':
            print("This script is designed to run on Windows systems only.")


if __name__ == "__main__":
    print("Checking for installed antivirus software...")
    check_antivirus()
    print("\nChecking for Active Directory installation...")
    check_active_directory()