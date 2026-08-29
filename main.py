"""
US Healthcare Claims Batch Processing & Validation Engine
Author: Amar Shaw
Description: Automated auditing tool to parse medical billing claims,
detect deprecated ICD-9 codes, and flag revenue risks.
"""

# Sample batch containing realistic medical claim data
claims_batch = [
    {"claim_id": "CLM-1001", "patient_id": "PT-883", "code": "E11.9", "type": "ICD-10", "charge": 250.00},
    {"claim_id": "CLM-1002", "patient_id": "PT-904", "code": "250.00", "type": "ICD-9", "charge": 180.00},
    {"claim_id": "CLM-1003", "patient_id": "PT-311", "code": "99213", "type": "CPT", "charge": 120.00},
    {"claim_id": "CLM-1004", "patient_id": "PT-452", "code": "G0438", "type": "HCPCS", "charge": 95.00},
    {"claim_id": "CLM-1005", "patient_id": "PT-119", "code": "UNKNOWN_CODE", "type": "OTHER", "charge": 310.00}
]

def process_claim(claim):
    code_type = claim.get("type", "").upper()
    
    if code_type in ["ICD-10", "CPT", "HCPCS"]:
        return {
            "status": "APPROVED",
            "action": "Clean claim ready for clearinghouse submission.",
            "risk_amount": 0.00
        }
    elif code_type == "ICD-9":
        return {
            "status": "REJECTED (DEPRECATED)",
            "action": "Outdated ICD-9 detected. Crosswalk to modern ICD-10 required.",
            "risk_amount": claim["charge"]
        }
    else:
        return {
            "status": "MANUAL REVIEW",
            "action": "Unrecognized code format. Route to Senior RCM Specialist.",
            "risk_amount": claim["charge"]
        }

def run_batch_audit(batch):
    print("==================================================")
    print("      HEALTHCARE CLAIMS AUDIT BATCH EXECUTION     ")
    print("==================================================")
    
    total_claims = len(batch)
    approved_count = 0
    flagged_count = 0
    total_revenue_at_risk = 0.00

    for index, claim in enumerate(batch, 1):
        audit_result = process_claim(claim)
        
        if audit_result["status"] == "APPROVED":
            approved_count += 1
        else:
            flagged_count += 1
            total_revenue_at_risk += audit_result["risk_amount"]
            
        print(f"[{index}/{total_claims}] Claim ID: {claim['claim_id']} | Code: {claim['code']} ({claim['type']})")
        print(f"       Status: {audit_result['status']}")
        print(f"       Action: {audit_result['action']}\n")

    print("--------------------------------------------------")
    print("BATCH SUMMARY REPORT")
    print(f"Total Claims Processed : {total_claims}")
    print(f"Clean Claims (Approved): {approved_count}")
    print(f"Flagged / Action Needed: {flagged_count}")
    print(f"Total Revenue at Risk  : ${total_revenue_at_risk:.2f}")
    print("==================================================")

if __name__ == "__main__":
    run_batch_audit(claims_batch)

