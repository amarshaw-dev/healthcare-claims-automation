# 1. Define a list of US medical billing codes (Data Batch)
claims_batch = ["ICD-10", "CPT", "ICD-9", "HCPCS"]

# 2. Initialize counter variables to track metrics
warning_count = 0
review_count = 0

print("--- Starting Claims Batch Processing ---")

# 3. Iterate through the batch using a loop to validate each billing code
for code in claims_batch:
    if code == "ICD-10":
        print(f"Success: {code} is a valid modern format.")
    elif code == "ICD-9":
        print(f"Warning: {code} is an outdated format!")
        warning_count = warning_count + 1  # Increment warning counter by 1
    else:
        print(f"Notice: {code} requires manual review.")
        review_count = review_count + 1    # Increment review counter by 1

# 4. Print the final execution summary totals
print("\n--- Final Claims Summary ---")
print(f"Total Outdated Formats Found: {warning_count}")
print(f"Total Manual Reviews Needed: {review_count}")
