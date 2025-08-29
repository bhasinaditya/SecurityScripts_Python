"""
Detects AV product on device
"""

import wmi
import os


def check_antivirus():
    try:
        # Initialize WMI connection
        wmi_obj = wmi.WMI(namespace="root\\SecurityCenter2")

        # Query for antivirus products
        antivirus_products = wmi_obj.AntiVirusProduct()

        if not antivirus_products:
            print("No antivirus software detected.")
            return

        # Output details for each antivirus product found
        for product in antivirus_products:
            product_name = product.displayName
            product_state = product.productState
            # Check if the antivirus is enabled (productState bitmask analysis)
            is_enabled = (product_state & 0x1000) == 0x1000

            if is_enabled:
                print(f"Running Antivirus: {product_name}")
            else:
                print(f"Detected Antivirus (Not Running): {product_name}")

    except Exception as e:
        print(f"Error checking antivirus status: {e}")
        if not os.name == 'nt':
            print("This script is designed to run on Windows systems only.")


if __name__ == "__main__":
    print("Checking for installed antivirus software...")
    check_antivirus()