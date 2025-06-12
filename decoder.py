# decoder.py

import re

def decode_fare_rule(rule):
    result = []
    if "CHANGE" in rule.upper() or "CHANGES" in rule.upper():
        if "NOT ALLOWED" in rule.upper():
            result.append("✈ Change: Not allowed")
        elif "PERMITTED WITH FEE" in rule.upper():
            result.append("✈ Change: Allowed (with fee)")
        else:
            result.append("✈ Change: Allowed")
    if "REFUND" in rule.upper() or "REFUNDS" in rule.upper():
        if "NOT ALLOWED" in rule.upper():
            result.append("❌ Refund: Not allowed")
        elif "PERMITTED WITH FEE" in rule.upper():
            result.append("💸 Refund: Allowed (with fee)")
        else:
            result.append("💸 Refund: Allowed")
    if not result:
        result.append("No recognized fare rules.")
    return result

if __name__ == "__main__":
    sample = "CHANGES PERMITTED WITH FEE - REFUNDS NOT ALLOWED"
    print("Input:", sample)
    print("Decoded:")
    for line in decode_fare_rule(sample):
        print("-", line)
