import os
from email import policy
from email.parser import BytesParser

def analyze_eml(file_path):
    print(f"\n[*] Analyzing: {file_path}")
    print("-" * 50)
    
    try:
        with open(file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
    except Exception as e:
        print(f"[-] Error reading file: {e}")
        return
        
    # Extract basic routing headers
    sender = msg.get('From', 'Not Found')
    return_path = msg.get('Return-Path', 'Not Found')
    auth_results = msg.get('Authentication-Results', '')
    
    print(f"[+] From Header:        {sender}")
    print(f"[+] Return-Path Header: {return_path}")
    print("-" * 50)
    
    if not auth_results:
        print("[-] Warning: No 'Authentication-Results' header found.")
        print("    The email might lack server-side authentication headers entirely.\n")
        return

    results_lower = auth_results.lower()
    
    # Check SPF Status
    print("[*] SPF (Sender Policy Framework) Status:")
    if 'spf=pass' in results_lower:
        print("    [PASS] The sending IP is authorized by the domain owner.")
    elif 'spf=fail' in results_lower:
        print("    [FAIL] ALERT: The sending IP is NOT authorized. Possible spoofing attempt!")
    elif 'spf=softfail' in results_lower:
        print("    [WARNING] The sending IP is weakly authorized or policy is set to softfail.")
    elif 'spf=none' in results_lower:
        print("    [NONE] The sending domain has no published SPF record. Verification not possible.")
    else:
        print("    [UNKNOWN/NONE] SPF status could not be clearly verified.")

    # Check DKIM Status
    print("\n[*] DKIM (DomainKeys Identified Mail) Status:")
    if 'dkim=pass' in results_lower:
        print("    [PASS] The email signature is valid and message integrity is intact.")
    elif 'dkim=fail' in results_lower:
        print("    [FAIL] ALERT: DKIM signature verification failed. The email may have been altered.")
    else:
        print("    [UNKNOWN/NONE] No valid DKIM signature verification found.")

    # Check DMARC Status
    print("\n[*] DMARC (Domain-based Message Authentication) Status:")
    if 'dmarc=pass' in results_lower:
        print("    [PASS] DMARC policy aligned successfully. Message is verified authentic.")
    elif 'dmarc=fail' in results_lower:
        print("    [FAIL] ALERT: DMARC policy evaluation failed. High risk of impersonation/spoofing.")
    else:
        print("    [UNKNOWN/NONE] DMARC results not found or policy not enforced.")
    
    print("=" * 50 + "\n")

def main():
    print("=== Email Header Authentication Analyzer ===")
    print("Type 'exit' or 'quit' at any time to close the program.\n")
    
    while True:
        file_path = input("Enter path to the .eml file: ").strip()
        
        # Allow user to exit gracefully
        if file_path.lower() in ['exit', 'quit']:
            print("Exiting program. Stay safe out there!")
            break
            
        # Strip surrounding quotes if the user dragged and dropped the file into the terminal
        file_path = file_path.strip('"\'')
        
        # Check if file exists
        if not os.path.exists(file_path):
            print("[-] Error: The specified file does not exist. Please check the path and try again.\n")
            continue
            
        # Check if it has a .eml extension
        if not file_path.lower().endswith('.eml'):
            print("[-] Error: Invalid file type. Please provide a file ending with '.eml'.\n")
            continue
            
        # Run analysis if checks pass
        analyze_eml(file_path)

if __name__ == "__main__":
    main()
