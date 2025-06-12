# rule_decoder.py

import re

def decode_fare_rule(rule_text):
    result = []
    text = rule_text.upper()

    if "CHANGE" in text or "CHANGES" in text:
        if "NOT" in text and "CHANGE" in text:
            result.append("Change: ❌ Not allowed")
        elif "FEE" in text:
            result.append("Change: ✅ Allowed (with fee)")
        else:
            result.append("Change: ✅ Allowed")

    if "REFUND" in text:
        if "NOT" in text:
            result.append("Refund: ❌ Not allowed")
        elif "FEE" in text:
            result.append("Refund: ✅ Allowed (with fee)")
        else:
            result.append("Refund: ✅ Allowed")

    if "NO SHOW" in text:
        if "FEE" in text:
            result.append("No-show: ⚠ Fee applies")
        else:
            result.append("No-show: ⚠ Penalty may apply")

    return result

# Example usage
if __name__ == "__main__":
    example = "CHANGES PERMITTED WITH FEE - REFUND NOT ALLOWED - NO SHOW FEE APPLIES"
    print("\n".join(decode_fare_rule(example)))
